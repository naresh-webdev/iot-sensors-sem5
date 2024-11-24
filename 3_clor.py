from gpiozero import PWMLED
from time import sleep

# Define RGB pins
red = PWMLED(17)
green = PWMLED(27)
blue = PWMLED(22)

def neon_effect():
    while True:
        # Fade in red
        for r in range(0, 101):  # 0 to 100% duty cycle
            red.value = r / 100.0
            sleep(0.02)  # Small delay for smooth transition
        # Fade in green while keeping red
        for g in range(0, 101):
            green.value = g / 100.0
            sleep(0.02)
        # Fade out red
        for r in range(100, -1, -1):
            red.value = r / 100.0
            sleep(0.02)
        # Fade in blue while keeping green
        for b in range(0, 101):
            blue.value = b / 100.0
            sleep(0.02)
        # Fade out green
        for g in range(100, -1, -1):
            green.value = g / 100.0
            sleep(0.02)
        # Fade out blue
        for b in range(100, -1, -1):
            blue.value = b / 100.0
            sleep(0.02)

try:
    print("Starting neon effect. Press Ctrl+C to exit.")
    neon_effect()
except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Turn off the LED when exiting
    red.off()
    green.off()
    blue.off()
