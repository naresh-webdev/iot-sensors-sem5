from gpiozero import DigitalInputDevice
from time import sleep

# Set up the tracking sensor on GPIO17
tracking_sensor = DigitalInputDevice(17)

# Function to test the sensor
def test_tracking_sensor():
    print("Testing Tracking Sensor...")
    while True:
        if tracking_sensor.is_active:
            print("No Line detected (or dark surface)")
        else:
            print("line detected (or light surface)")
        sleep(1)  # Check every 1 second

# Run the test function
test_tracking_sensor()
