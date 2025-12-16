from fastapi import FastAPI
from app.api.marketController import router
from app.api.schedulerController import router as scheduler_router

app = FastAPI(title="BRVM Microservice")

app.include_router(router, prefix="/api/market")
app.include_router(scheduler_router, prefix="/api/scheduler")