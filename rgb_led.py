from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=17, green=27, blue=22)

def cycle_colors():
    while True:
        led.color = (1, 0, 0)  # Red
        sleep(1)
        led.color = (0, 1, 0)  # Green
        sleep(1)
        led.color = (0, 0, 1)  # Blue
        sleep(1)
        led.color = (1, 1, 0)  # Yellow (Red + Green)
        sleep(1)
        led.color = (0, 1, 1)  # Cyan (Green + Blue)
        sleep(1)
        led.color = (1, 0, 1)  # Magenta (Red + Blue)
        sleep(1)
        led.color = (1, 1, 1)  # White (Red + Green + Blue)
        sleep(1)

try:
    cycle_colors()
except KeyboardInterrupt:
    led.off()  