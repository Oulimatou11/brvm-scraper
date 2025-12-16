from fastapi import APIRouter
from app.service.marketService import MarketService

router = APIRouter()
service = MarketService()

@router.get("/indices")
def get_indices():
    return service.get_indices()

@router.get("/stocks")
def get_stocks():
    return service.get_stocks()
