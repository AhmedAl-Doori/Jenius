
from gpiozero import DistanceSensor
from gpiozero import PWMLED
from time import sleep
mySensor = DistanceSensor(echo=24, trigger=18, max_distance=2)
myAlarm = PWMLED(6)

def turnTemp():
    myAlarm.value = 1
    sleep(1)
    myAlarm.value = 0
    mySensor.distance
    
while True:
    if not (mySensor.distance<1.2 and mySensor.distance>0.0):
        print(mySensor.distance)
        turnTemp()
        
        #pass
    else:
        print(mySensor.distance)
        myAlarm.value = 0
        #pass
sleep(0.5)
