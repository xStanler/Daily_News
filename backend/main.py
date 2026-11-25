from pathlib import Path
import json
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"
RESEARCH_FILE = BASE_DIR.parent / "skrypty" / "research.json"

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# CSS / Static files
app.mount("/frontend", StaticFiles(directory=str(FRONTEND_DIR)), name="static")


@app.get("/")
def root():
    return FileResponse(FRONTEND_DIR / "index.html", status_code=200)


@app.get("/home")
def get_home():
    return HTMLResponse(
        """
        <article>
            <div class="article">
                <p style="text-align: center; font-size: 24px; font-weight: bold;">Welcome to the Daily News project.</p>
                <p>
                    <br>
                    Daily News to aplikacja webowa, której głównym zadaniem jest automatyczne agregowanie, selekcjonowanie oraz podsumowywanie najważniejszych informacji z poprzedniego dnia.<br>
                    Narzędzie pobiera dane z wybranych stron internetowych oraz dziedzin, pozwalając użytkownikowi na szybki przegląd najważniejszych wydarzeń bez konieczności przeglądania dziesiątek portali informacyjnych.
                </p>
            </div>
        </article>
        """,
        status_code=200,
    )


def render_error_card(title: str, message: str) -> str:
    return f"""
    <article>
        <div class="article">
            <h1>{title}</h1>
            <p>{message}</p>
        </div>
    </article>
    """


def render_article_card(portal: str, title: str, link: str, summary: str) -> str:
    return f"""
    <article>
        <div class="article">
            <h1>
                <a href="{link}" target="_blank" style="text-decoration: none; color: inherit;">{title}</a>
            </h1>
            <p style="font-size: 13px; color: #666; margin-bottom: 8px;">Źródło: <strong>{portal}</strong></p>
            <p>{summary}</p>
        </div>
    </article>
    """


def fetch_article_summary(article_url: str, portal_name: str) -> dict:
    try:
        response = requests.get(article_url, headers=DEFAULT_HEADERS, timeout=5)
        response.encoding = "utf-8"
        if response.status_code != 200:
            return {
                "ok": False,
                "error": f"Błąd czytania: HTTP {response.status_code}",
            }

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.text.strip() if soup.title and soup.title.text else "Nie znaleziono tytułu"

        paragraphs = soup.find_all("p")
        summary = " ".join(p.text.strip() for p in paragraphs[:3] if p.text.strip())

        return {
            "ok": True,
            "portal": portal_name,
            "title": title,
            "link": article_url,
            "summary": f"{summary}..." if summary else "Nie znaleziono tekstu",
        }
    except Exception as exc:
        return {
            "ok": False,
            "error": f"Awaria przy czytaniu: {exc}",
        }


def resolve_article_link(page_soup: BeautifulSoup, base_url: str, selector: str, portal_name: str) -> dict:
    target_element = None
    if selector:
        try:
            target_element = page_soup.select_one(selector)
        except Exception as sel_err:
            return {
                "ok": False,
                "error": f"Błąd składni selektora CSS ('{selector}'): {sel_err}",
            }

    link_tag = None
    if target_element:
        link_tag = target_element if target_element.name == "a" else target_element.find("a")
    elif not selector:
        link_tag = page_soup.find("a")

    if not link_tag or "href" not in link_tag.attrs:
        return {
            "ok": False,
            "error": "Nie znaleziono linku pod wskazanym selektorem",
        }

    href = (link_tag["href"] or "").strip()
    if not href or href.startswith("#") or href.startswith("javascript:"):
        return {
            "ok": False,
            "error": "Błędny format linku artykułu",
        }

    if href.startswith("/"):
        href = base_url.rstrip("/") + href

    return {"ok": True, "url": href}


@app.get("/articles/{category}")
def get_articles_category(category: str):
    try:
        with open(RESEARCH_FILE, "r", encoding="utf-8") as file:
            config = json.load(file)
    except Exception as exc:
        html = render_error_card("Błąd / Brak danych", f"Błąd wczytywania research.json: {exc}")
        return HTMLResponse(html, status_code=404)

    sources = config.get(category)
    if not sources:
        html = render_error_card("Błąd / Brak danych", "Błąd: Brak kategorii w pliku JSON")
        return HTMLResponse(html, status_code=404)

    html_chunks = []

    # Jedna pętla po źródłach: pobierz stronę -> znajdź link -> pobierz treść -> od razu zbuduj HTML
    for page in sources:
        portal_name = page.get("Nazwa") or page.get("nazwa") or "Nieznany portal"
        base_url = page.get("Link") or page.get("link") or ""
        selector = page.get("Selektor") or page.get("selektor") or ""

        try:
            response = requests.get(base_url, headers=DEFAULT_HEADERS, timeout=5)
            response.encoding = "utf-8"
            if response.status_code != 200:
                html_chunks.append(
                    render_error_card(f"Problem z pobraniem ({portal_name})", f"Status: błąd kod: {response.status_code}")
                )
                continue

            page_soup = BeautifulSoup(response.text, "html.parser")
            link_res = resolve_article_link(page_soup, base_url, selector, portal_name)
            if not link_res["ok"]:
                html_chunks.append(
                    render_error_card(f"Problem z pobraniem ({portal_name})", f"Status: {link_res['error']}")
                )
                continue

            article_res = fetch_article_summary(link_res["url"], portal_name)
            if not article_res["ok"]:
                html_chunks.append(
                    render_error_card(f"Problem z pobraniem ({portal_name})", f"Status: {article_res['error']}")
                )
                continue

            html_chunks.append(
                render_article_card(
                    portal=article_res["portal"],
                    title=article_res["title"],
                    link=article_res["link"],
                    summary=article_res["summary"],
                )
            )
        except Exception as exc:
            html_chunks.append(
                render_error_card(
                    f"Problem z pobraniem ({portal_name})",
                    f"Status: błąd połączenia ze stroną główną: {exc}",
                )
            )

    return HTMLResponse("".join(html_chunks), status_code=200)