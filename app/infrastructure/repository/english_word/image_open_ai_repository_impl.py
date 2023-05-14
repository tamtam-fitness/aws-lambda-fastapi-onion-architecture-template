from domain.english_word.i_image_repository import IImageOriginRepo
from domain.english_word.value_object import EnglishWord


class ImageOpenAIRepositoryImpl(IImageOriginRepo):
    def get(self, english_word: EnglishWord) -> str:
        # TODO: 実装する
        return "https://example.com/image.png"
