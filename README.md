# **Daily News**

**Welcome to the Daily News project.** Daily News is a web application whose main purpose is to automatically aggregate, select, and summarize the most important information from the previous day. The tool retrieves data from selected websites and fields, allowing users to quickly review the most important events without having to browse dozens of news portals.

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
*The directory structure is under development.*

:computer: **[app-entry]**: *The main FastAPI application runtime file.*

:computer: **[ui-templates]**: *The visual layer of the application uses HTMX to dynamically load content without reloading the page.*

:computer: **[scraper-core]**: *Scripts responsible for crawlers and scraping data from external news services.*


## Team & Roles:

* **Stanisław (Stachu)** – Project Lead, DevOps & Frontend
* **Antek** – Backend & README.md
* **Paweł** – Scripts (Scraping) & Research

---

## Future Plans:

### 1. Database Integration
* Implementation of a database (SQL/NoSQL) for logging and storing articles. *
*  Sections for related and recent articles (*Similar Articles / Recent*).

### 2. Expansion of Thematic Categories
* Filtering and categorizing news into key areas:
  * Sports
  * Politics
  * World
  * IT
  * Health
  * Science

### 3. AI Integration
* Using artificial intelligence to generate dynamic summaries. *
* Implementing an advanced duplicate filter to avoid duplicate messages from different sources.

---

## FAQ:

>### 1. Why are you creating this app?
> The main goal of the project is to learn modern technologies (FastAPI, HTMX, Docker/Kubernetes) in practice, improve our programming skills, and simply have fun working on a collaborative project.

>### 2. Where did the idea for Daily News come from?
> The project was conceived by Stanisław, who recognized the need to create a simple, personalized news aggregator free of noise and clickbait.
