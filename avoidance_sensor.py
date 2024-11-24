from gpiozero import DigitalInputDevice
from time import sleep

# Set up the avoidance sensor on GPIO 17
avoidance_sensor = DigitalInputDevice(17)

# Function to check the sensor
def check_sensor():
    while True:
        if avoidance_sensor.is_active:
            print("Path is clear.")
        else:
            print("Obstacle detected!")
        sleep(1)  # Wait for 1 second before checking again

# Start checking the sensor
try:
    check_sensor()
except KeyboardInterrupt:
    print("Program interrupted, turning off.")
