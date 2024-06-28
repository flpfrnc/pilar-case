from pydantic import BaseModel, RootModel
from typing import List, Literal, Dict


class WordsRequest(BaseModel):
    words: List[str]


class SortWordsRequest(WordsRequest):
    order: Literal["asc", "desc"]


class VowelCountResponse(RootModel):
    Dict[str, int]


class SortWordsResponse(RootModel):
    List[str]
