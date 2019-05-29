#USE THE ULTRASONIC SENSOR TO FIRE THE ALARM

#libraries
import RPi.GPIO as GPIO
import time
from time import sleep
import threading

#board pins
GPIO.setmode(GPIO.BCM)
#define the pins
trigPin = 18
echoPin = 24
#set trig to output and echo to input
GPIO.setup(trigPin, GPIO.OUT)
GPIO.output(trigPin, False)
GPIO.setup(echoPin, GPIO.IN)


#distance calculation
def Distance():
    GPIO.setup(trigPin, GPIO.OUT)
    GPIO.output(trigPin, False)
    GPIO.setup(echoPin, GPIO.IN)
    #print("in function")
    #trigger the sensor
    #print("Firing Up")
    sleep(.1)
    GPIO.output(trigPin, True)
    time.sleep(0.00001)
    GPIO.output(trigPin, False)
    while GPIO.input(echoPin)==0:
        print("echo low")
        startTime = time.time()
    while GPIO.input(echoPin) == 1:
        print("echo high")
        endTime = time.time()
    duration = endTime - startTime
    distance = (duration * 34300) / 2
    print("out of function")
    return distance

#distance call
print("Calculating Distance")
#calculation = threading.Thread(target=Distance)
#calculation.start()
while True:
    print("Distance is {0}".format(Distance()))
    GPIO.cleanup((trigPin, echoPin))
    time.sleep(0.5)
          

