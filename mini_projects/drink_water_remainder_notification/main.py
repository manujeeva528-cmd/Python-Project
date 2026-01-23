import time
from plyer import notification
def water_reminder():
    while True:
        notification.notify(
            title="Hydration Reminder",
            message="Time to drink water! Stay hydrated for better health.",
            timeout=10
        )
        # time.sleep(3600)  # Remind every hour
        time.sleep(3600)

water_reminder()