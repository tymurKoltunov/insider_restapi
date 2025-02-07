from typing import List

from pydantic import BaseModel


class AuthorTitleResponse(BaseModel):
    title: str
