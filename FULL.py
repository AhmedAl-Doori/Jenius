#import the tools
import time
from time import sleep
import Adafruit_LSM303
from gpiozero import PWMLED
from gpiozero import DistanceSensor
from gpiozero import Servo
#define pins
servoPin = 17
alarmPin = 6
trigPin = 18
echoPin = 24
#prepare servo 
myAdjustment = 0.45
minPulse = (1.0 - myAdjustment)/1000
maxPulse = (2.0 + myAdjustment)/1000
targetTilt = 1000
#make objects
myServo = Servo(servoPin, min_pulse_width=minPulse, max_pulse_width=maxPulse)
myAlarm = PWMLED(alarmPin)
mySensor = DistanceSensor(echo=echoPin, trigger=trigPin, max_distance=2)
myAcc = Adafruit_LSM303.LSM303()
xList = []
valList = []
disList = []

#function to convert the error to the servo
def map(amount):
    mappedAmount = 1000*(amount - 0) * (maxPulse - minPulse) / (1000 + 1000) + minPulse
    return mappedAmount

#function to turn on the alarm
def turnTemp():
    myAlarm.value = 1
    sleep(0.5)
    myAlarm.value = 0

#function to calculate distance and fire alarm
def fire():
    disList.append(mySensor.distance)
    if len(disList)==10:
        avg = sum(disList)/10
        if avg<0.1:
            #print(mySensor.distance)
            turnTemp()
        else:
            #print(mySensor.distance)
            myAlarm.value = 0
        disList.clear()
    else:
        pass
#function to calculate error in tilt and stabilize
def orient(targetTilt):
    accel, mag = myAcc.read()
    x, y, z = accel
    xList.append(x)
    #print("X = {0}, Y = {1}, Z = {2}".format(x,y,z)),

    if len(xList) == 10: 
        avg = sum(xList)/10
        error = abs(abs(avg) - targetTilt)
        mappedError = map(error)
        
        if (z!=0):
            value = (-1)*mappedError*z/abs(z)
            valList.append(value)
        else:
            value = 0
            valList.append(value)

        print(valList)

        if len(valList) == 10:
            if abs(valList[0]-valList[9])>0.1:
                myServo.value = valList[9]
                print(valList[9])
            else:
                myServo.value = None
            valList.clear()
        else:
            pass
        #print(xList, "and", avg)
        xList.clear()
    else:
        pass
    #print(" Error = {0}, Mapped = {1}, Value = {2}".format(error, mappedError,value))

#calibrat the servo and test the bounds
myServo.max()
time.sleep(5)
myServo.min()
time.sleep(5)
myServo.mid()
time.sleep(5)

#operation part
while True:
    orient(targetTilt)
    fire()
    
