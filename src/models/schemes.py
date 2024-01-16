from pydantic import BaseModel


class ScrapeRequest(BaseModel):
    url: str


class ScrapeResponse(BaseModel):
    title: str
    content: str


class ErrorResponse(BaseModel):
    error: str
