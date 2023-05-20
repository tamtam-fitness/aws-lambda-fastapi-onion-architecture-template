from injector import inject

from domain.english_word.english_word import EnglishWord
from domain.english_word.i_image_repository import IImageOriginRepo
from schemas.english_word import ImageGet, ImageGetResponse


class GetImageUseCase:
    @inject
    def __init__(self, image_repository: IImageOriginRepo) -> None:
        self.__image_repository = image_repository

    def handle(self, image_get: ImageGet) -> ImageGetResponse:
        english_word = EnglishWord(value=image_get.english_word)
        image_url = self.__image_repository.get(english_word)

        return ImageGetResponse(image_url=image_url)
