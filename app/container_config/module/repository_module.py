from injector import Binder, Module

import infrastructure.english_word.repository as impl
from domain.english_word.i_image_repository import IImageCacheRepo, IImageOriginRepo
from domain.english_word.i_meaning_repository import (
    IMeaningCacheRepo,
    IMeaningOriginRepo,
)


class RepositoryModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(IMeaningCacheRepo, to=impl.MeaningDynamodbRepositoryImpl)
        binder.bind(IMeaningOriginRepo, to=impl.MeaningOpenAIRepositoryImpl)
        binder.bind(IImageCacheRepo, to=impl.ImageS3RepositoryImpl)
        binder.bind(IImageOriginRepo, to=impl.ImageOpenAIRepositoryImpl)
