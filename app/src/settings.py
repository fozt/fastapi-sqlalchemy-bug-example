import os
from typing import Union

from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_USER: str = os.environ.get("DATABASE_USER")
    DATABASE_PASSWORD: str = os.environ.get("DATABASE_PASSWORD")
    DATABASE_HOST: str = os.environ.get("DATABASE_HOST")
    DATABASE_PORT: Union[int, str] = os.environ.get("DATABASE_PORT")
    DATABASE_NAME: str = os.environ.get("DATABASE_NAME")
    ASYNC_DATABASE_URI: str = (
        f"postgresql+asyncpg://"
        f"{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )


settings = Settings()
