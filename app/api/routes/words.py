from fastapi import APIRouter
from app.api.models.request_models import WordsRequest
from app.api.services.words import count_vowels

router = APIRouter()

@router.post("/vowel_count")
async def vowel_count(request: WordsRequest):
    return {word: count_vowels(word) for word in request.words}