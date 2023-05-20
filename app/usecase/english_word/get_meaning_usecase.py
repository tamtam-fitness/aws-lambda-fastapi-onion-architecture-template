from injector import inject

from domain.english_word.english_word import EnglishWord
from domain.english_word.i_meaning_repository import IMeaningOriginRepo
from schemas.english_word import MeaningGet, MeaningGetResponse


class GetMeaningUseCase:
    @inject
    def __init__(self, meaning_repository: IMeaningOriginRepo) -> None:
        self.__meaning_repository = meaning_repository

    def handle(self, meaning_get: MeaningGet) -> MeaningGetResponse:
        english_word = EnglishWord(value=meaning_get.english_word)
        meaning = self.__meaning_repository.get(english_word)

        return MeaningGetResponse(meaning=meaning)
