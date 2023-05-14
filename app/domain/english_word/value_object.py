from pydantic import BaseModel, Field, validator

from exceptions.core import APIException
from exceptions.error_messages import ErrorMessage


class EnglishWord(BaseModel, frozen=True): # type: ignore
    value: str = Field(max_length=20)

    @validator("value")
    def is_english(cls, v: str) -> str:
        if not v.isascii():
                raise APIException(ErrorMessage.WORD_IS_NOT_ENGLISH)
        return v
