from typing import List
from pydantic import BaseModel, Field
from pets_api.src.schemas.tag import Tag
from pets_api.src.schemas.category import Category


class Pet(BaseModel):
    id: int
    category: Category
    name: str
    photo_urls: List[str] = Field(..., alias='photoUrls')
    tags: List[Tag]
    status: str
