from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

#CSS
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
                                <p>
                        Litwo! Ojczyzno moja! ty jesteś jak zdrowie.
                        Ile cię trzeba cenić, ten tylko się dowie,
                        Kto cię stracił. Dziś piękność twą w całej ozdobie
                        Widzę i opisuję, bo tęsknię po tobie.<br>

                        Panno Święta, co Jasnej bronisz Częstochowy
                        I w Ostrej świecisz Bramie! Ty, co gród zamkowy
                        Nowogródzki ochraniasz z jego wiernym ludem!
                        Jak mnie dziecko do zdrowia powróciłaś cudem
                        (Gdy od płaczącej matki pod Twoję opiekę
                         Ofiarowany, martwą podniosłem powiekę
                         I zaraz mogłem pieszo do Twych świątyń progu
                         Iść za wrócone życie podziękować Bogu),
                        Tak nas powrócisz cudem na Ojczyzny łono.
                                </p>
                            </div>
                        </article>
                        """, status_code=200)

#NOTE: W ostatecznym produkcie będziemy robić @app.get("/articles/{category}") i automatycznie to generować

@app.get("/articles/sport")
async def get_aricles_sport():
    return HTMLResponse("""
                        <article>
                            <div class="article">
                                <h1>
                                    2025-26 NBA Awards: Finalists and winners for league accolades
                                </h1>
                                <p>
                                    Listing every award winner from the 2025-26 regular season, including Kia MVP and other major awards.
                        Below is a complete list of all the major NBA Awards for the 2025-26 season:<br><br>

                        Kia NBA Most Valuable Player<br>
                        > Winner: Shai Gilgeous-Alexander, Oklahoma City Thunder<br>

                        Finalists:<br>

                        Shai Gilgeous-Alexander, Oklahoma City Thunder [winner]<br>
                        Nikola Jokić, Denver Nuggets<br>
                        Victor Wembanyama, San Antonio Spurs<br>
                                </p>
                            </div>
                        </article>
                        """, status_code=200)

@app.get("/articles/ekonomia")
async def get_aricles_ekonomia():
    return HTMLResponse("""
                        <article>
                            <div class="article">
                                <h1>
                                    SpaceX idzie na giełdę. To może być największe IPO świata
                                </h1>
                                <p>
                                    Firma SpaceX Elona Muska oficjalnie zmierza na giełdę i może zadebiutować na Nasdaq w przyszłym miesiącu. Jak pisze CNBC, prawdopodobnie będzie to rekordowa oferta publiczna, po której najbogatszy człowiek na świecie stanie na czele dwóch odrębnych spółek publicznych wartych biliony dolarów.
                                </p>
                            </div>
                        </article>

                        <article>
                            <div class="article">
                                <h1>
                                    Zwrot akcji w Samsungu. Decyzja zapadła w ostatniej chwili. Wystrzał na giełdzie
                                </h1>
                                <p>
                                    Samsung Electronics nieoczekiwanie zawarł wstępne porozumienie ze związkami zawodowymi, które wywalczyły gigantyczne premie. Giełda w Seulu natychmiast zareagowała wzrostami.
                                </p>
                            </div>
                        </article>
                        """, status_code=200)

@app.get("/articles/polityka")
async def get_aricles_polityka():
    return HTMLResponse("""
                        <article>
                            <div class="article">
                                <h1>
                                    Trump o żołnierzach USA w Polsce. Ważna decyzja
                                </h1>
                                <p>
                                    Prezydent USA Donald Trump poinformował, że Stany Zjednoczone wyślą do Polski dodatkowe pięć tysięcy żołnierzy. Wskazał na kluczową rolę prezydenta Karola Nawrockiego.
                                </p>
                            </div>
                        </article>

                        <article>
                            <div class="article">
                                <h1>
                                    Fałszywe zamówienia w Republice. Kebab i pizza na adres Kaczyńskiego
                                </h1>
                                <p>
                                    Podczas środowego programu TV Republika do studia dzwonili pracownicy lokali z pytaniami o dostawę kebaba i dużego zamówienia pizzy. Zamówienia miały trafić pod adres przy ul. Mickiewicza 49 w Warszawie, który w studiu wskazano jako dom Jarosława Kaczyńskiego. Jak wskazuje portal gazeta.pl, stacja wiąże incydent z serią fałszywych zgłoszeń wobec swoich pracowników.
                                </p>
                            </div>
                        </article>

                        <article>
                            <div class="article">
                                <h1>
                                    Jacek Ż. zatrzymany. Fala komentarzy. "To zapewne nie koniec"
                                </h1>
                                <p>
                                    Były wiceminister Jacek Ż. został zatrzymany w związku ze śledztwem dotyczącym afery w Narodowym Centrum Badań i Rozwoju. Sprawę komentują jego dotychczasowi rywale z koalicji rządowej. "To nie są dobre czasy dla świętych krów, ani politycznych, ani biznesowych" - napisała europosłanka KO Kamila Gasiuk-Pihowicz. "Będzie jeszcze milej, gdy dołączy do niego ten, który pociągał za sznurki w NCBiR" - napisał poseł Koalicji Obywatelskiej Robert Kropiwnicki.
                                </p>
                            </div>
                        </article>
                        """, status_code=200)

@app.get("/articles/zdrowie")
async def get_aricles_zdrowie():
    return HTMLResponse("""
                        <article>
                            <div class="article">
                                <h1>
                                    Serce traci rytm i zagraża sprawności mózgu. Nowe wytyczne kardiologiczne chronią przed udarem
                                </h1>
                                <p>
                                    Niespodziewane kołatanie serca budzi ogromny lęk i uczucie bezsilności. To często symptom migotania przedsionków, które przyczynia się do prawie jednego na trzy udary mózgu w Polsce. Najnowsze wytyczne kardiologiczne podkreślają, że właściwie dobrana profilaktyka przeciwzakrzepowa skutecznie chroni mózg przed udarem.
                                </p>
                            </div>
                        </article>
                        """, status_code=200)

@app.get("/articles/technologia")
async def get_aricles_technologia():
    return HTMLResponse("""
                        <article>
                            <div class="article">
                                <h1>
                                    Te okulary wyglądają niepozornie. W środku ukrywają prywatne kino z gigantycznym ekranem
                                </h1>
                                <p>
                                    Mobilny gaming i oglądanie filmów na smartfonie lub laptopie mogą wkrótce wejść na zupełnie nowy poziom. Do sprzedaży w Polsce trafiły okulary Viture XR Beast, które generują gigantyczny wirtualny ekran przypominający prywatne kino. Urządzenie waży zaledwie 88 gramów, współpracuje z konsolami, komputerami i telefonami, a producent przekonuje, że może stać się czymś więcej niż gadżetem dla fanów technologii.
                                </p>
                            </div>
                        </article>

                        <article>
                            <div class="article">
                                <h1>
                                    Gmail bez 15 GB dla każdego? Google testuje zmianę, która może zaboleć nowych użytkowników
                                </h1>
                                <p>
                                    Przez lata konto Google kojarzyło się z prostą obietnicą: zakładasz Gmaila i dostajesz 15 GB miejsca na pocztę, Dysk i Zdjęcia Google. Teraz ta zasada zaczyna się chwiać. Google potwierdziło, że testuje nową politykę pamięci dla części nowych kont. W praktyce niektórzy użytkownicy widzą tylko 5 GB, chyba że dodadzą numer telefonu.
                                </p>
                            </div>
                        </article>
                        """, status_code=200)
