from typing import List

import requests
from pydantic import TypeAdapter

from data_objects.author_title_response import AuthorTitleResponse
from data_objects.random_response import PoemListResponse
from urls.urls import RANDOM_POEM_URL, AUTHOR_TITLES_URL


class PoemController:
    @staticmethod
    def get_random_poem():
        poem = requests.get(RANDOM_POEM_URL)
        return PoemListResponse(root=poem.json())

    @staticmethod
    def remove_empty_lines(poem):
        poem.lines = [line for line in poem.lines if line]

    @staticmethod
    def get_titles_of(author):
        poems = requests.get(AUTHOR_TITLES_URL.format(author))
        return TypeAdapter(List[AuthorTitleResponse]).validate_python(poems.json())
