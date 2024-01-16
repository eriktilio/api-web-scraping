from fastapi import APIRouter, Depends, HTTPException

from src.controllers import scrape as scrape_controller
from src.models import schemes as schemas

router = APIRouter(tags=["Scrape Methods"])


@router.post("/scrape/")
async def post_scrape(request_data: schemas.ScrapeRequest):
    try:
        url = request_data.url
        result = scrape_controller.get_scrape(url)
        return result

    except HTTPException as e:
        return e
