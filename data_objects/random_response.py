from typing import List

from pydantic import BaseModel


class RandomPoemResponse(BaseModel):
    title: str
    author: str
    lines: List[str]
    linecount: str


class PoemListResponse(BaseModel):
    root: List[RandomPoemResponse]
