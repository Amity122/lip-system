import datetime
import time
import winsound
from config import settings


def validate_time(hour, minutes):
    if minutes < 0:
        minutes = 60 + minutes
        hour -= 1

    return hour, minutes


alarm_hour = int(settings.SHUTDOWN_TIME.split(":")[0])
alarm_minutes = int(settings.SHUTDOWN_TIME.split(":")[1] - 30)

alarm_hour, alarm_minutes = validate_time(alarm_hour, alarm_minutes)

while True:
    now = datetime.datetime.now()
    if now.hour == alarm_hour and now.minute == alarm_minutes:
        print("\nIt's almost time to sleep! Please go to bed.")
        # Play a sound
        winsound.PlaySound("./audio/alarm.wav", winsound.SND_FILENAME)
        break
    time.sleep(60)  # Wait for 1 minute before checking again
