from gpiozero import LED
from time import sleep

myLED = LED(6)

while True:
    myLED.on()
    sleep(1)
    myLED.off()
    sleep(1)
