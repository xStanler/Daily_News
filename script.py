import requests 
import json
from bs4 import BeautifulSoup

with open('research.json','r', encoding='utf-8')as plik:
    wszystkie=json.load(plik)


def pobierz_artykuly(kategoria:  str):
    strony_do_odwiedzenia=wszystkie.get(kategoria)
    print(strony_do_odwiedzenia) 
    if not strony_do_odwiedzenia:
        return {"błąd": f"Nie znaleziono kategorii: {kategoria}"}
    
    wyniki=[]

    naglowki = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    for strona in strony_do_odwiedzenia:
        nazwa=strona["Nazwa"]
        link=strona["Link"]

        try:
            odpowiedz=requests.get(link, headers=naglowki, timeout=5)

            if odpowiedz.status_code==200:

                html=odpowiedz.text
                wyniki.append({
                    "Nazwa":nazwa,
                    "Status": "Kod pobrany"
                    })
            else:
                wyniki.append({
                    "Nazwa":nazwa,
                    "Status": f"błąd kod: {odpowiedz.status_code}"
                    })
        except Exception as e:
            wyniki.append({
                "Nazwa": nazwa,
                "Status": f"błąd połączenia: {str(e)}"
                })
    return {"kategoria": kategoria, "rezultaty": wyniki}

if __name__=="__main__":
        

