from fastapi import APIRouter

from .endpoints import english_words

v1_router = APIRouter()
v1_router.include_router(
    english_words.router, prefix="/english-words", tags=["english_words"]
)
