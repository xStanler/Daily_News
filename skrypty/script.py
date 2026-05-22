import requests
import uvicorn
from bs4 import BeautifulSoup
from fastapi import FastAPI 
import json

app=FastAPI()

with open('research.json','r',encoding='utf-8') as plik:
    wszystkie=json.load(plik)

def obrobka(link, nazwa, naglowki):
    try:
        response=requests.get(link, headers=naglowki, timeout=5)
        response.encoding='utf-8'
        if response.status_code==200:
            temp=BeautifulSoup(response.text, 'html.parser')

            if temp.title:
                title=temp.title.text
            else:
                title="Nie znaleziono tytułu"
            
            all_p=temp.find_all('p')
            tresc=""
            for p in all_p[:3]:
                tresc+=p.text.strip()+ " "
            
            return {
                "Portal": nazwa,
                "Tytuł": title,
                "Link": link,
                "Treść": tresc.strip() + "..." if tresc else "Nie znaleziono tekstu",
                "Status": "Sukces!"
            }
            
        else:
            return {"Portal": nazwa, "Status": f"Błąd czytania: HTTP {response.status_code}"}
            
    except Exception as e:
        return {"Portal": nazwa, "Status": f"Awaria przy czytaniu: {str(e)}"}

@app.get("/szukaj")

def pobierz_artykul(kategoria):
    to_visit=wszystkie.get(kategoria)

    if not to_visit:
        return {"błąd"}
    wyniki=[]

    naglowki = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    for strona in to_visit:
        nazwa=strona["Nazwa"]
        link=strona["Link"]
        selektor=strona["Selektor"]

        try:
            response=requests.get(link, headers=naglowki, timeout=5)
            response.encoding='utf-8'
            if response.status_code==200:
                html=response.text
                temp=BeautifulSoup(html, 'html.parser')

                article=temp.select_one(selektor)
                tag=None

                if article:
                    if article.name=='a':
                        tag=article
                    else:
                        tag=article.find('a')

                if tag and 'href' in tag.attrs:
                    article_link=tag['href']

                    if article_link.startswith('/'):
                        article_link=link.rstrip('/')+article_link

                    ready=obrobka(article_link, nazwa, naglowki)

                    wyniki.append(ready)

                else:
                    wyniki.append({"Portal": nazwa, "Status": "Nie znaleziono linku"})
            else:
                wyniki.append({"Portal": nazwa, "Status": f"błąd kod: {response.status_code}"})
        except Exception as e:
            wyniki.append({"Portal": nazwa, "Status": f"błąd połączenia ze stroną główną: {str(e)}"})
            
    return {"kategoria": kategoria, "rezultaty": wyniki}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
