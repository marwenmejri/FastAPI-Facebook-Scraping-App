from datetime import datetime
from pydantic import BaseModel


class ScrapingRequest(BaseModel):
    url: str


class PostSchema(BaseModel):
    id: int
    page: str
    url: str
    text: str
    date: datetime
    nbr_emojis: str
    nbr_comments: str

    class Config:
        orm_mode = True


class PostCreate(BaseModel):
    page: str
    url: str
    text: str
    date: datetime
    nbr_emojis: str
    nbr_comments: str
