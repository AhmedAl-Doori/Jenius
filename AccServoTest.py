#find the difference between the required orientation and the actual orientation
#use the difference to tell the servo how much to rotate. The sign determines the direction

import time
import Adafruit_LSM303
from gpiozero import Servo
from gpiozero import LED

servoPin = 17
myAdjustment = 0.45
minPulse = (1.5 - myAdjustment)/1000
maxPulse = (2.5 + myAdjustment)/1000

myServo = Servo(servoPin, min_pulse_width=minPulse, max_pulse_width=maxPulse)
myLSM= Adafruit_LSM303.LSM303()

def map(amount):
    mappedAmount = 1000*(amount - 0) * (maxPulse - minPulse) / (1000 + 1000) + minPulse
    return mappedAmount

targetTilt = -1000
myServo.max()
time.sleep(5)
myServo.min()
time.sleep(5)
myServo.mid()
time.sleep(5)
while True:
    accel, mag = myLSM.read()
    x, y, z = accel
    #print("X = {0}, Y = {1}, Z = {2}".format(x,y,z)),
    error = x - targetTilt
    mappedError = map(error)
    if (z!=0):
        value = mappedError*z/abs(z)
    myServo.value = value
    print(" Error = {0}, Mapped = {1}, Value = {2}".format(error, mappedError,value))

    time.sleep(0.1)
