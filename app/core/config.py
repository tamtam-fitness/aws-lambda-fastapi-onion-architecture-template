from typing import Union

from pydantic import BaseSettings, HttpUrl, validator


# ref: https://qiita.com/ninomiyt/items/ee676d7f9b780b1d44e8
class Settings(BaseSettings):
    OPEN_AI_API_KEY: str
    SENTRY_DSN: Union[
        HttpUrl,
        None,
    ] = "https://fa15f4da6f7f4adbb2009a1c0f956625@o29226.ingest.sentry.io/4504988107210752"
    ENV: Union[str, None] = None

    @validator("SENTRY_DSN", pre=True)
    def sentry_dsn_can_be_blank(cls, v: str) -> Union[str, None]:
        if len(v) == 0:
            return None
        return v

    class Config:
        case_sensitive = True


settings = Settings()
