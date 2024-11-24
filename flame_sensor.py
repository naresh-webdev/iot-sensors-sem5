from gpiozero import DigitalInputDevice
from time import sleep

# Set up the flame sensor on GPIO 17
flame_sensor = DigitalInputDevice(17)

# Function to check the flame sensor
def check_flame():
    while True:
        if flame_sensor.is_active:
            print("No Flame detected! Stay Cool ;)")
        else:
            print("Flame detected!")
        sleep(1) 

# Start checking the flame sensor
try:
    check_flame()
except KeyboardInterrupt:
    print("Program interrupted, turning off.")
