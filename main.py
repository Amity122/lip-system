import os
from datetime import datetime
from abc import ABC, abstractmethod
from config import settings
from playsound3 import playsound
import time
from alarm import validate_time, play_alarm


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
        if current_time == settings.WAKEUP_TIME:
            playsound(settings.WAKEUP_ALARM)

    def time_to_sleep(self):
        current_time = datetime.now().strftime("%H:%M")
        alarm_hour, alarm_minutes = validate_time(int(settings.NAP_TIME.split(
            ":")[0]), int(settings.NAP_TIME.split(":")[1]) - 30)
        print(f"Alarm set for: {alarm_hour}:{alarm_minutes}")
        if current_time == f"{alarm_hour:02d}:{alarm_minutes:02d}":
            print("\nIt's almost time to sleep! Please go to bed.")
            play_alarm(settings.NAP_ALARM)

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
    while True:
        day_routine = DayRoutine()
        night_routine = NightRoutine()
        night_routine.time_to_sleep()
        day_routine.get_ready()
        day_routine.time_to_sleep()
        time.sleep(60)  # Check every minute
