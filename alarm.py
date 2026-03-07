import os
from playsound3 import playsound


def validate_time(hour, minutes):
    if minutes < 0:
        minutes = 60 + minutes
        hour -= 1

    return hour, minutes


def play_alarm(alarm):
    playsound(alarm)
    # Put PC to sleep (Windows)
    if os.name == 'nt':
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
