from fastapi import APIRouter

from container_config.di_container import DIContainer
from schemas.english_word import (
    ImageGet,
    ImageGetResponse,
    MeaningGet,
    MeaningGetResponse,
)
from usecase.english_word.get_image_usecase import GetImageUseCase
from usecase.english_word.get_meaning_usecase import GetMeaningUseCase

router = APIRouter()


@router.get("/generate-meaning", response_model=MeaningGetResponse)
def get_meaning(word: str) -> MeaningGetResponse:
    usecase = DIContainer().resolve(GetMeaningUseCase)
    response = usecase.handle(meaning_get=MeaningGet(english_word=word))  # type: ignore
    return response


@router.get("/generate-image", response_model=ImageGetResponse)
def get_image(word: str) -> ImageGetResponse:
    usecase = DIContainer().resolve(GetImageUseCase)
    response = usecase.handle(image_get=ImageGet(english_word=word))  # type: ignore
    return response
