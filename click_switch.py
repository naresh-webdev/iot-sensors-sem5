from gpiozero import Button
import time

button = Button(17)

def button_pressed():
    print("Button Pressed")

def button_released():
    print("Button Released")

def check_button_state():
    print("Button state:", button.is_pressed)

# Attach the functions to the button events
button.when_pressed = button_pressed
button.when_released = button_released

# Keep the program running and check the button state
try:
    while True:
        check_button_state()
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
