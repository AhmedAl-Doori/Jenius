from gpiozero import DistanceSensor
from gpiozero import LED
from time import sleep
mySensor = DistanceSensor(echo=24, trigger=18, max_distance=2)
myAlarm = LED(6)

mySensor.when_in_range = myAlarm.on
mySensor.when_out_of_range = myAlarm.off
