from gpiozero import Button
from signal import pause

# Connect the sensor's Signal pin to GPIO 17
vibration_sensor = Button(17)

def vibration_detected():
    print("Vibration detected!")

# Attach the detection callback
vibration_sensor.when_pressed = vibration_detected

print("Vibration sensor is ready. Waiting for vibration...")
pause()  # Keeps the program running
