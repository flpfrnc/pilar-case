from fastapi import APIRouter

from app.api.models.request_models import (
    WordsRequest,
    SortWordsRequest,
    VowelCountResponse,
    SortWordsResponse,
)
from app.api.services.words import count_vowels, sort_words


router = APIRouter()


@router.post("/vowel_count", response_model=VowelCountResponse)
async def vowel_count(request: WordsRequest):
    return {word: count_vowels(word) for word in request.words}


@router.post("/sort", response_model=SortWordsResponse)
async def sort(request: SortWordsRequest):
    return sort_words(request.words, request.order)
