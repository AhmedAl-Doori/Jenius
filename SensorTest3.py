from gpiozero import DistanceSensor

mySensor = DistanceSensor(echo=24, trigger=18, max_distance=5)

while True:
    print(mySensor.distance)
