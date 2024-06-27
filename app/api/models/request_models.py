from pydantic import BaseModel
from typing import List


class WordsRequest(BaseModel):
    words: List[str]
