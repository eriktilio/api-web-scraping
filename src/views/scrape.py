from fastapi import APIRouter, Depends, HTTPException

from src.controllers import scrape as scrape_controller
from src.models import schemes as schemas

router = APIRouter(tags=["Scrape Methods"])


@router.post("/scrape/")
async def post_scrape(request_data: schemas.ScrapeRequest):
    try:
        item = request_data.item
        result = scrape_controller.get_scrape(item)
        return result

    except HTTPException as e:
        return e
