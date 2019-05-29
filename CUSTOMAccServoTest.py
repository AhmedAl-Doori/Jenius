#find the difference between the required orientation and the actual orientation
#use the difference to tell the servo how much to rotate. The sign determines the direction

import time
import Adafruit_LSM303
from gpiozero import Servo
from gpiozero import LED

servoPin = 17
myAdjustment = 0.45
minPulse = (1.0 - myAdjustment)/1000
maxPulse = (2.0 + myAdjustment)/1000

myServo = Servo(servoPin, min_pulse_width=minPulse, max_pulse_width=maxPulse)
myLSM= Adafruit_LSM303.LSM303()

def map(amount):
    mappedAmount = 1000*(amount - 0) * (maxPulse - minPulse) / (1000 + 1000) + minPulse
    return mappedAmount

#This is where I need the value of the servo to be 0. Right at the mid
targetTilt = 1000

#calibrat the servo and test the bounds
myServo.max()
time.sleep(5)
myServo.min()
time.sleep(5)
myServo.mid()
time.sleep(5)

#Error always a positive number for consistency
while True:
    accel, mag = myLSM.read()
    x, y, z = accel
    #print("X = {0}, Y = {1}, Z = {2}".format(x,y,z)),
    error = abs(abs(x) - targetTilt)
    mappedError = map(error)
    if (z!=0):
        value = (-1)*mappedError*z/abs(z)
    myServo.value = value
    print(" Error = {0}, Mapped = {1}, Value = {2}".format(error, mappedError,value))

    time.sleep(0.1)
