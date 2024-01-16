from typing import List

from pydantic import BaseModel


class ScrapeRequest(BaseModel):
    item: str


class ScrapeResponse(BaseModel):
    title: str
    price: str
    local: str
    updated: str
    address: str


class ScrapeResponseList(BaseModel):
    data: List[ScrapeResponse]


class ErrorResponse(BaseModel):
    error: str
