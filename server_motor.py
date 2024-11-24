from gpiozero import Servo
from time import sleep

# Configure servo
servo = Servo(27)  # GPIO pin connected to the servo signal wire

try:
    while True:
        print("Moving to minimum position")
        servo.min()  # Move to minimum position
        sleep(2)
        
        print("Moving to mid position")
        servo.mid()  # Move to mid position
        sleep(2)
        
        print("Moving to maximum position")
        servo.max()  # Move to maximum position
        sleep(2)

except KeyboardInterrupt:
    print("Stopping servo control")
