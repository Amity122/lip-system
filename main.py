import os
from datetime import datetime
from abc import ABC, abstractmethod
import winsound
from config import settings
from winsound import SND_FILENAME


class DailyRoutine(ABC):

    @abstractmethod
    def time_to_sleep(self):
        pass

    @abstractmethod
    def get_ready(self):
        pass

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def relax(self):
        pass


class DayRoutine(DailyRoutine):

    def get_ready(self):
        current_time = datetime.now().strftime("%H:%M")

        if current_time == settings.WORK_TIME:
            winsound.PlaySound(settings.ALARM_FILE, SND_FILENAME)

    def time_to_sleep(self):
        pass

    def work(self):
        pass

    def study(self):
        pass

    def relax(self):
        pass


class NightRoutine(DailyRoutine):
    def time_to_sleep(self):
        current_time = datetime.now().strftime("%H:%M")

        print(f"Current time: {current_time}")
        if current_time == settings.SHUTDOWN_TIME:
            os.system("shutdown /s /t 1")

    def get_ready(self):
        pass

    def work(self):
        pass

    def study(self):
        pass

    def relax(self):
        pass


# Run this program upon windows startup
if __name__ == "__main__":
    day_routine = DayRoutine()
    night_routine = NightRoutine()
    night_routine.time_to_sleep()
