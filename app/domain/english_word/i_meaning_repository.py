from abc import ABCMeta, abstractmethod

from domain.english_word.value_object import EnglishWord


class IMeaningCacheRepo(metaclass=ABCMeta):
    @abstractmethod
    def get(self, english_word: EnglishWord) -> str:
        raise NotImplementedError()


class IMeaningOriginRepo(metaclass=ABCMeta):
    @abstractmethod
    def get(self, english_word: EnglishWord) -> str:
        raise NotImplementedError()
