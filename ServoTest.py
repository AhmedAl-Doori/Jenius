from gpiozero import Servo
from gpiozero import LED
from time import sleep

servoPin = 17
#ledPin = 17

myservo = Servo(servoPin)
#myled = LED(ledPin)

while True:
    myservo.min()
    #myled.on()
    sleep(0.5)
    myservo.max()
   # myled.off()
    sleep(0.5)
    
