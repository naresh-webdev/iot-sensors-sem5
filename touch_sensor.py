from gpiozero import DigitalInputDevice
from time import sleep

# Set up the touch sensor on GPIO 17
touch_sensor = DigitalInputDevice(17)

# Function to check the touch sensor
def check_touch():
    while True:
        if touch_sensor.is_active:
            print("Touch detected!")
        else:
            print("No touch.")
        sleep(1)  # Wait for 1 second before checking again

# Start checking the touch sensor
try:
    check_touch()
except KeyboardInterrupt:
    print("Program interrupted, turning off.")
