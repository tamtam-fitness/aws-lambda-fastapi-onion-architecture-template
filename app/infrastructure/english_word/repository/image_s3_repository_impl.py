from domain.english_word.english_word import EnglishWord
from domain.english_word.i_image_repository import IImageCacheRepo


class ImageS3RepositoryImpl(IImageCacheRepo):
    def get(self, english_word: EnglishWord) -> str:
        # TODO: 実装する
        return "https://example.com/image.png"
