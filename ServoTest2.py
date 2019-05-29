#Modified Range of Rotation

from gpiozero import Servo
from gpiozero import LED
from time import sleep

servoPin = 17
myAdjustment = 0.5
minPulse = (1 - myAdjustment)/1000
maxPulse = (2.0 + myAdjustment)/1000

myservo = Servo(servoPin, min_pulse_width=minPulse, max_pulse_width=maxPulse)
#myled = LED(ledpin)

while True:
    myservo.min()
    print("currently min")
 #   myled.on()
    sleep(1)
    myservo.max()
    print("currently max")
  #  myled.off()
    sleep(1)
    
