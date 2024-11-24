from gpiozero import LED
from time import sleep

# Set up GPIO pin for the laser (e.g., GPIO 17)
laser = LED(17)

while True:
    print("Turning on the laser...")
    laser.on()

    # Keep the laser on for 5 seconds
    sleep(5)


    print("Turning off the laser...")
    laser.off()
    
    sleep(2)
