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
RESEARCH_FILE = BASE_DIR.parent / "research.json"

# CSS / Static files
app.mount("/frontend", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

# index.html
@app.get("/")
async def root():
    return FileResponse(FRONTEND_DIR / "index.html", status_code=200)

@app.get("/home")
async def get_home():
    return HTMLResponse("""
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
                        """, status_code=200)

def Procesor(link, name, headers):
    try:
        response = requests.get(link, headers=headers, timeout=5)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            temp = BeautifulSoup(response.text, 'html.parser')
            title = temp.title.text if temp.title else "Nie znaleziono tytułu"
            
            all_p = temp.find_all('p')
            tresc = ""
            for p in all_p[:3]:
                tresc += p.text.strip() + " "
            
            return {
                "Portal": name,
                "Tytuł": title,
                "Link": link,
                "Treść": tresc.strip() + "..." if tresc else "Nie znaleziono tekstu",
                "Status": "Sukces!"
            }
        else:
            return {"Portal": name, "Status": f"Błąd czytania: HTTP {response.status_code}"}
    except Exception as e:
        return {"Portal": name, "Status": f"Awaria przy czytaniu: {str(e)}"}
def Download_arts(category):
    try:
        with open(RESEARCH_FILE, 'r', encoding='utf-8') as plik:
            all = json.load(plik)
    except Exception as e:
        return {"kategoria": category, "Status": f"Błąd wczytywania research.json: {str(e)}"}

    to_visit = all.get(category)
    if not to_visit:
        return {"kategoria": category, "Status": "Błąd: Brak kategorii w pliku JSON"}
    
    results = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    for page in to_visit:
        nazwa = page.get("Nazwa") or page.get("nazwa") or "Nieznany portal"
        link = page.get("Link") or page.get("link") or ""
        selektor = page.get("Selektor") or page.get("selektor") or ""

        try:
            response = requests.get(link, headers=headers, timeout=5)
            response.encoding = 'utf-8'
            if response.status_code == 200:
                temp = BeautifulSoup(response.text, 'html.parser')
                
                article = None
                try:
                    if selektor:
                        article = temp.select_one(selektor)
                except Exception as sel_err:
                    results.append({"Portal": nazwa, "Status": f"Błąd składni selektora CSS ('{selektor}'): {str(sel_err)}"})
                    continue

                tag = None
                if article:
                    if article.name == 'a':
                        tag = article
                    else:
                        tag = article.find('a')
                elif not selektor:
                    tag = temp.find('a')

                if tag and 'href' in tag.attrs:
                    article_link = tag['href']
                    if article_link.startswith('/'):
                        article_link = link.rstrip('/') + article_link

                    ready = Procesor(article_link, nazwa, headers)
                    results.append(ready)
                else:
                    results.append({"Portal": nazwa, "Status": "Nie znaleziono linku pod wskazanym selektorem"})
            else:
                results.append({"Portal": nazwa, "Status": f"błąd kod: {response.status_code}"})
        except Exception as e:
            results.append({"Portal": nazwa, "Status": f"błąd połączenia ze stroną główną: {str(e)}"})
            
    return {"kategoria": category, "rezultaty": results}

@app.get("/articles/{category}")
async def get_articles_category(category: str):
    datas = Download_arts(category)
    
    results = datas.get("rezultaty", [])
    if not results:
        status_msg = datas.get("Status", "Nie znalezniono artykułów")
        return HTMLResponse(f"""
            <article>
                <div class="article">
                    <h1>Błąd / Brak danych</h1>
                    <p>{status_msg}</p>
                </div>
            </article>
        """, status_code=404)

    html_content = ""
    for item in results:
        if item.get("Status") == "Sukces!":
            tytul = item.get("Tytuł", "Brak tytułu")
            tresc = item.get("Treść", "")
            link = item.get("Link", "#")
            portal = item.get("Portal", "Nieznane źródło")
            
            html_content += f"""
            <article>
                <div class="article">
                    <h1>
                        <a href="{link}" target="_blank" style="text-decoration: none; color: inherit;">{tytul}</a>
                    </h1>
                    <p style="font-size: 13px; color: #666; margin-bottom: 8px;">Źródło: <strong>{portal}</strong></p>
                    <p>{tresc}</p>
                </div>
            </article>
            """
        else:
            portal = item.get("Portal", "Nieznany portal")
            status_blad = item.get("Status", "Błąd")
            html_content += f"""
            <article>
                <div class="article">
                    <h1>Problem z pobraniem ({portal})</h1>
                    <p>Status: {status_blad}</p>
                </div>
            </article>
            """

    return HTMLResponse(html_content, status_code=200)