from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class Category(BaseModel):
    id: int
    name: str


class Tag(BaseModel):
    id: int
    name: str


class Pet(BaseModel):
    id: int
    category: Optional[Category] = None
    name: str
    photoUrls: List[HttpUrl]
    tags: Optional[List[Tag]] = None
    status: Optional[str] = None

