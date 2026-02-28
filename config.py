from decouple import config
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SHUTDOWN_TIME: str = config("SHUTDOWN_TIME", default="23:00")


settings = Settings()
