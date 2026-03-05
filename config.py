from decouple import config
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SHUTDOWN_TIME: str = "23:00"
    ALARM_FILE: str = "./audio/alarm.wav"
    WORK_TIME: str = "09:00"
    SKIN_CARE_TIME: str = "20:00"

    class Config:
        env_file = ".env"


settings = Settings()
