from fastapi import APIRouter
from app.api.models.request_models import WordsRequest, SortWordsRequest
from app.api.services.words import count_vowels, sort_words

router = APIRouter()

@router.post("/vowel_count")
async def vowel_count(request: WordsRequest):
    return {word: count_vowels(word) for word in request.words}



@router.post("/sort")
async def sort(request: SortWordsRequest):
    return sort_words(request.words, request.order)