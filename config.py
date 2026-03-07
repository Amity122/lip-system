from decouple import config
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SHUTDOWN_TIME: str = "23:00"
    WAKEUP_TIME: str = "07:30"
    WAKEUP_ALARM: str = "./audio/alarm.wav"
    NAP_ALARM: str = "./audio/nap.wav"
    NAP_TIME: str = "11:00"
    BREAKFAST_TIME: str = "09:00"
    SKIN_CARE_TIME: str = "20:00"

    class Config:
        env_file = ".env"


settings = Settings()
