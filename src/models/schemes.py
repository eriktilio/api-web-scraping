from typing import List, Optional

from pydantic import BaseModel


class ScrapeRequest(BaseModel):
    item: str
    page: Optional[int] = 1


class ScrapeResponse(BaseModel):
    title: str
    price: str
    local: str
    url_image: Optional[str] = None
    last_update: str
    address: str


class ScrapeResponseList(BaseModel):
    current_page: int
    total_pages: int
    data: List[ScrapeResponse]


class ErrorResponse(BaseModel):
    error: str
