from domain.english_word.english_word import EnglishWord
from domain.english_word.i_meaning_repository import IMeaningCacheRepo


class MeaningDynamodbRepositoryImpl(IMeaningCacheRepo):
    def get(self, english_word: EnglishWord) -> str:
        # TODO: 実装する
        return "ギリシア文字の第11字母"
