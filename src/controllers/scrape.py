import re

import requests
from bs4 import BeautifulSoup
from fastapi import Depends, HTTPException

from src.models import schemes as schemas
from src.utils.web_scraper import WebScraper


def get_scrape(item: str):
    param = re.sub(r" ", "+", item).lower()
    try:
        scraper = WebScraper(f"?termoCdGtin=&descricaoProd={param}")
        return schemas.ScrapeResponseList(data=scraper.get_data())

    except requests.HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"HTTP Error: {e.response.status_code}",
        )

    except requests.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=f"Request Exception: {str(e)}",
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
