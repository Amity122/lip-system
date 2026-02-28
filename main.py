import os
from datetime import datetime
from abc import ABC, abstractmethod


class DailyRoutine(ABC):
    @abstractmethod
    def time_to_sleep(self):
        pass


class NightRoutine(DailyRoutine):
    def time_to_sleep(self):
        current_time = datetime.now().strftime("%H:%M")

        print(f"Current time: {current_time}")
        if current_time == settings.SHUTDOWN_TIME:
            os.system("shutdown /s /t 1")


# Run this program upon windows startup
if __name__ == "__main__":
    night_routine = NightRoutine()
    night_routine.time_to_sleep()
