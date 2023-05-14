from pydantic import BaseModel, Field, HttpUrl


# Shared properties
class WordBase(BaseModel):
    english_word: str = Field(max_length=20)


class MeaningGet(WordBase):
    pass


class MeaningGetResponse(BaseModel):
    meaning: str


class ImageGet(WordBase):
    pass


class ImageGetResponse(BaseModel):
    image_url: HttpUrl
