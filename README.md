# Daily News

Welcome to the **Daily News** project. Daily News is a web application designed to automatically aggregate, curate, and summarize the most important news from the previous day. The tool fetches data from selected websites and domains, allowing users to quickly catch up on key events without having to browse through dozens of news portals.

**Project Lead:** Stanisław Chmielewski  
**Contributors:** Antoni Rafał Masłowski & Paweł Zapała  

---

## Table of Contents
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Team & Roles](#team--roles)
- [Future Plans](#future-plans)
- [FAQ](#faq)

---

## Technology Stack
- **Backend:** Python (FastAPI)
- **Scripts / Scraping:** BeautifulSoup, Requests
- **Frontend:** HTMX, HTML / CSS
- **DevOps:** Docker, Kubernetes

---

## Project Structure
*Note: Directory structure is currently under development.*

- 💻 `[app-entry]`: Main entry-point script for the FastAPI application.
- 💻 `[ui-templates]`: Visual layer using HTMX for dynamic content loading without full page reloads.
- 💻 `[scraper-core]`: Scripts responsible for web crawlers and scraping data from external news services.

---

## Team & Roles
- **Stanisław (Stachu)** – Project Lead, DevOps & Frontend
- **Antek** – Backend & README.md
- **Paweł** – Scripts (Scraping) & Research

---

## Future Plans

1. **Database Integration**
   - Implement a database (SQL/NoSQL) for logging and storing articles.
   - Add sections for related and recent articles (*Related Articles* / *Recent*).

2. **Expanding Subject Categories**
   - Filtering and categorizing news into core domains:
     - Sports
     - Politics
     - World
     - IT
     - Health
     - Science

3. **AI Integration**
   - Utilize Artificial Intelligence to generate dynamic summaries.
   - Implement an advanced duplicate filter to eliminate redundant stories from different sources.

---

## FAQ

**1. Why are you creating this application?**  
The main goal of this project is to learn modern technologies (FastAPI, HTMX, Docker/Kubernetes) in practice, improve our programming skills, and simply have fun working on a project together.

**2. Where did the idea for Daily News come from?**  
The idea was originated by Stanisław, who saw the need for a simple, personalized news aggregator free of information noise and clickbait.