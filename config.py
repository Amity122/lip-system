from decouple import config
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SHUTDOWN_TIME: str = config("SHUTDOWN_TIME", default="23:00")
    ALARM_FILE: str = config("ALARM_FILE", default="./audio/alarm.wav")


settings = Settings()
