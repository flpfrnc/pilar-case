from http import HTTPStatus

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.api.models.request_models import WordsRequest, SortWordsRequest, VowelCountResponse, SortWordsResponse
from app.api.services.words import count_vowels, sort_words


router = APIRouter()


@router.post("/vowel_count", response_model=VowelCountResponse)
async def vowel_count(request: WordsRequest):
    try:
        return {word: count_vowels(word) for word in request.words}
    except Exception:
        return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            content={"message": "An internal error has occurred"})


@router.post("/sort", response_model=SortWordsResponse)
async def sort(request: SortWordsRequest): 
    try:    
        return sort_words(request.words, request.order)
    except Exception:
        return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            content={"message": "An internal error has occurred"})

