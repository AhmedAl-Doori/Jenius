#ON THE PIN 6

from gpiozero import LED
from time import sleep

alarmPin = 6

myAlarm = LED(alarmPin)

x = 0
while True:
    myAlarm.on()
    sleep(1)
    myAlarm.off()
    sleep(1)

    
    
