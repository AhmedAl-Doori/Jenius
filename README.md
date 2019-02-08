# Jenius :chart_with_upwards_trend: :closed_umbrella:
The project aims to manufacture an assistive walking device that reduces the number of accidents elders face by integrating modern sensing and processing technologies. 

## Background
Cognitive and sensory abilities tend to deteriorate as one ages. According to WHO, adults older than 65
years suffer the greatest number of fatal falls. Factors like environmental hazards, awareness, and assistive device
disregard are all related and can be minimized with smart solutions. Normal wooden canes are cool, but their only function is to reduce the weight on the person's legs. My idea is to have a cane that does all the factors above at the same time. The cane is projected to detect obtacles and reduce the rate of injury.
***
## Early Planning
![overview](https://github.com/AhmedAl-Doori/Jenius/blob/master/Documentation/Overview.jpg)
***
## Finalized Planning
The whole framework doesn't include an actual cain. All the pieces are intended wo be designed with holders that clamp to sticks. Doing so makes the device more widley used but will require some setup for the wiring. 
### Processisng System
A Raspberry PI 3 will be used to drive all the operations. Therefore, it should be located at the middle of the stick and enclosed by a shell of some sort to keep it protected. It's also useful to have the board easily reachable so the code can be edited anytime.
### Notification System
The speaker is located near the handle so the user can hear the alarm clearly, which fires when the sensor detects an irregularity in the terrain. The ultrasonic sensor is the closest instrument to the ground located at the end of the stick. 
### Gimbal System
The ultrasonic sensor maintains its oritentation because of the data a gyroscope recieves; the gyroscope directs the servo to spin the sensor in the right way. The gyrscope needs to stay accurate at all times so the best option is to store it in the PI's shell near the middle of the stick. While the servo is connected to the ultrasonic sensor near the bottom.  
### Docking and Charging System
A carrier will have LED lights around that glow when approached to help see the stick in the dark night. It also functions as a charger for the cane's battery.
### Further Optimizations
* A pressure sensor can be used at the base so the algorithm only functions when there's ground contact. That saves battery energy.
* Different tones can be used as alarms to represent holes or bumps.
* Hollow sick to maintain light weight and hide the wires
* Adjustable length and headlight
***
## Resources
* Raspberry PI 3
* 
## Code
***

## Design
