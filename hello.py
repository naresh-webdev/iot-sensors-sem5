import RPi.GPIO as GPIO
import time

# Pin configuration
servo_pin = 17  # GPIO pin connected to the servo signal wire

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Set up PWM
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz PWM frequency (standard for servos)
pwm.start(0)  # Start with 0% duty cycle (off)

def set_angle(angle):
    # Convert angle (0 to 180) to duty cycle
    duty_cycle = 2 + (angle / 18)
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Allow servo to reach position
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        # Test servo angles
        set_angle(0)   # 0 degrees
        time.sleep(2)
        set_angle(90)  # 90 degrees
        time.sleep(2)
        set_angle(180) # 180 degrees
        time.sleep(2)

except KeyboardInterrupt:
    print("Servo control stopped")
    pwm.stop()
    GPIO.cleanup()
