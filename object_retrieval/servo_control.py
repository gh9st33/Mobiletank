```python
import RPi.GPIO as GPIO
import time

# Define the servo GPIO pin
SERVO_PIN = 17

# Setup the GPIO for servo
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Set the servo to use PWM on the servo pin
servo = GPIO.PWM(SERVO_PIN, 50) # 50 Hz frequency

# Function to set the servo angle
def set_servo_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN, True)
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(SERVO_PIN, False)
    servo.ChangeDutyCycle(0)

# Function to move the servo to the default position
def reset_servo():
    set_servo_angle(0)

# Function to move the servo to the pick up position
def pick_up_position():
    set_servo_angle(90)

# Function to move the servo to the drop off position
def drop_off_position():
    set_servo_angle(180)

# Start the servo
servo.start(0)

# Test the servo control
if __name__ == "__main__":
    try:
        while True:
            reset_servo()
            time.sleep(2)
            pick_up_position()
            time.sleep(2)
            drop_off_position()
            time.sleep(2)
    except KeyboardInterrupt:
        servo.stop()
        GPIO.cleanup()
```