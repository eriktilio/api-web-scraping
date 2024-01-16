import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from config import Config
from src.views.scrape import router as scrape_router

app = FastAPI()
app.include_router(scrape_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
