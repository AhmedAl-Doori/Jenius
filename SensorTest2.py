'''Example of getting a direct reading from RPi.GPIO.'''

import RPi.GPIO as GPIO
from hcsr04sensor import sensor
from time import sleep

# This script uses a static function outside of the Measurement class
# in hcsr04sensor named basic_distance
# No median readings pulled from a sample for error correction
# No setmode in the library
# No pin cleanups.  You handle all of these things in your own code
# Just a simple return of a cm distance as reported directly from Rpi.GPIO

# use any available gpio pins
trig = 18
echo = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # use GPIO.BCM for board pin values

while True:
    distance = sensor.basic_distance(trig, echo)
    print("The distance is {} cm's".format(distance))
    GPIO.cleanup((trig, echo))
    sleep(0.01)
