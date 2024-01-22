import re

import requests
from fastapi import Depends, HTTPException

from src.models import schemes as schemas

# from src.utils.search_image import SearchImageGoogle
from src.utils.web_scraper import WebScraper


def get_scrape(item: str, page: int):
    param = re.sub(r" ", "+", item).lower()

    try:
        scraper_url = f"{page}?termoCdGtin=&descricaoProd={param}&latitude=-3.041560057837038&longitude=-59.9972124545962&consultaExata=true&_consultaExata=on&tipoConsulta=0&distancia=99999&municipio=Manaus&action="
        scraper = WebScraper(scraper_url)

        # seeker_image = SearchImageGoogle()
        data = scraper.get_data()
        pagination = scraper.get_pagination()

        # for result in data:
        #     result["url_image"] = seeker_image.get_url_image(result["title"])

        return schemas.ScrapeResponseList(
            current_page=page,
            total_pages=pagination["total_pages"],
            data=data,
        )

    except requests.HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"HTTP Error: {e.response.status_code}",
        )

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Request Exception: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
