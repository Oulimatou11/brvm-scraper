# BRVM Scraper Microservice

## Déscription
Ce microservice permet de récupérer les données boursières
du marché BRVM (Bourse Régionale des Valeurs Mobilières).

Les données collectées incluent :
- `Indices boursiers`
- `Cours des actions`

## Technologies
- `Python`
- `FastAPI`
- `Requests / BeautifulSoup / Playwright`
- `REST API`

## Fonctionnalités
- `Scraping des indices BRVM`
- `Scraping des cours des actions`
- `Exposition des données via une API REST`
- `Planification via WSO2`

## Démarrage
### Prérequis
- Python 3.10+
- pip

### Installation
```bash
pip install -r requirements.txt
```

## Lancement
```bash
 uvicorn app.main:app --reload
```

## Endpoints
- Récupération des indices BRVM: `GET /api/market/indices`
- Liste des cours actions: `GET /api/market/stocks`
- Scheduler WSO2: `POST http://127.0.0.1:8000/api/scheduler/scrape`
