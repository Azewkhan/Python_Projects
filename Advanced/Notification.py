from plyer import notification
import time

#here plyer library helps to access hardware setting - notification
while True:
    notification.notify(
        title = "Hey Champ!",
        message = "Take a quick 5",
        timeout =10
    # time out tells us for how long our notification is going to stay
    )
    time.sleep(1800) # after these many second this while loop will run and we will be notified