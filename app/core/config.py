import os

import yaml
from pydantic import BaseSettings, HttpUrl


# ref: https://qiita.com/ninomiyt/items/ee676d7f9b780b1d44e8
class Settings(BaseSettings):
    OPEN_AI_API_KEY: str
    SENTRY_DSN: HttpUrl | None
    ENV: str | None = None

    class Config:
        case_sensitive = True


# YAMLをロードする
# https://gist.github.com/ericvenarusso/dcaefd5495230a33ef2eb2bdca262011
def read_yaml(file_path: str) -> Settings:
    with open(file_path) as stream:
        config = yaml.safe_load(stream)

    return Settings(**config)


env = os.environ["ENV"]
settings = read_yaml(f"{os.getcwd()}/core/yaml_configs/{env}.yaml")
