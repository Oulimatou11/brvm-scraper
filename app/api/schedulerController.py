from fastapi import APIRouter
from app.service.marketService import MarketService

router = APIRouter()
service = MarketService()

@router.post("/scrape")
def trigger_scrape():
    service.refresh_data()
    return {"status": "Scraping initialise avec succes"}