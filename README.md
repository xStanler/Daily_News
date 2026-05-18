# **Daily News**

**Welcome to the Daily News project.** Daily News to aplikacja webowa, której głównym zadaniem jest automatyczne agregowanie, selekcjonowanie oraz podsumowywanie najważniejszych informacji z poprzedniego dnia. Narzędzie pobiera dane z wybranych stron internetowych oraz dziedzin, pozwalając użytkownikowi na szybki przegląd najważniejszych wydarzeń bez konieczności przeglądania dziesiątek portali informacyjnych.

Project Lead: *Stanisław Chmielewski*

Participants: *Antoni Rafał Masłowski* i *Paweł Zapała*

**Table of Contents**
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Team & Roles](#team--roles)
- [Future Plans](#future-plans)
- [FAQ](#faq)

## Technology Stack:
Backend: Python (FastAPI)

Scripts/Scraping: Beautiful Soup, Requests

Frontend: HTMX, HTML/CSS

DevOps: Docker, Kubernetes

## Project Structure:
*Struktura katalogów jest w trakcie rozwoju.*

:computer: **[app-entry]**: *Główny plik uruchomieniowy aplikacji FastAPI.*

:computer: **[ui-templates]**: *Warstwa wizualna aplikacji wykorzystująca HTMX do dynamicznego ładowania treści bez przeładowywania strony.*

:computer: **[scraper-core]**: *Skrypty odpowiedzialne za crawlery i scraping danych z zewnętrznych serwisów informacyjnych.*


## Team & Roles:

* **Stanisław (Stachu)** – Project Lead, DevOps & Frontend
* **Antek** – Backend & README.md
* **Paweł** – Scripts (Scraping) & Research

---

## Future Plans:

### 1. Database Integration
* Wdrożenie bazy danych (SQL/NoSQL) do logowania i przechowywania artykułów.
* Sekcje dla powiązanych oraz najnowszych artykułów (*Podobne artykuły / Recent*).

### 2. Rozbudowa Kategorii Tematycznych
* Filtrowanie i podział wiadomości na kluczowe dziedziny:
  * Sport
  * Polityka
  * Świat
  * IT
  * Zdrowie
  * Nauka

### 3. AI Integration
* Wykorzystanie sztucznej inteligencji do generowania dynamicznych podsumowań.
* Implementacja zaawansowanego filtra duplikatów, aby unikać powtarzających się wiadomości z różnych źródeł.

---

## FAQ:

>### 1. Dlaczego tworzycie tę aplikację?
> Głównym celem projektu jest nauka nowoczesnych technologii (FastAPI, HTMX, Docker/Kubernetes) w praktyce, podwyższenie naszych kompetencji programistycznych oraz po prostu dobra zabawa przy wspólnym projekcie.

>### 2. Skąd wziął się pomysł na Daily News?
> Pomysłodawcą projektu jest Stanisław, który dostrzegł potrzebę stworzenia prostego, spersonalizowanego agregatora newsów pozbawionego szumu informacyjnego i clickbaitów.
