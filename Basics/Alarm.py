from datetime import datetime
import time

Alarm_time = input("Enter the alarm time (HH:MM:SS): ")

try:
    Alarm_hour = int(Alarm_time[0:2])
    Alarm_minute = int(Alarm_time[3:5])
    Alarm_second = int(Alarm_time[6:8])

    if Alarm_hour > 23 or Alarm_minute > 59 or Alarm_second > 59:
        raise ValueError

    if len(Alarm_time) != 8:
        raise ValueError

except ValueError:
    print("Please type time in correct format HH:MM:SS")

while True:
    Current_time = datetime.now()

    if (Alarm_hour == Current_time.hour and
        Alarm_minute == Current_time.minute):
        #Alarm_second == Current_time.second ):

        print("Wake Up!")
        break

    time.sleep(1)