from domain.english_word.i_meaning_repository import IMeaningOriginRepo
from domain.english_word.value_object import EnglishWord


class MeaningOpenAIRepositoryImpl(IMeaningOriginRepo):
    def get(self, english_word: EnglishWord) -> str:
        # TODO: 実装する
        return "ギリシア文字の第11字母"
