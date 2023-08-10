```python
import RPi.GPIO as GPIO
import time

# Define the GPIO pin that the gripper servo is connected to
GRIPPER_SERVO_PIN = 17

# Define the open and close positions of the gripper
GRIPPER_OPEN = 10
GRIPPER_CLOSE = 5

# Setup the GPIO pin for the gripper servo
GPIO.setmode(GPIO.BCM)
GPIO.setup(GRIPPER_SERVO_PIN, GPIO.OUT)

# Create a PWM instance for the gripper servo
gripper_servo = GPIO.PWM(GRIPPER_SERVO_PIN, 50)  # 50Hz frequency

def open_gripper():
    """
    Open the gripper.
    """
    gripper_servo.start(GRIPPER_OPEN)
    time.sleep(1)  # Allow time for the servo to move
    gripper_servo.stop()

def close_gripper():
    """
    Close the gripper.
    """
    gripper_servo.start(GRIPPER_CLOSE)
    time.sleep(1)  # Allow time for the servo to move
    gripper_servo.stop()

def cleanup():
    """
    Cleanup the GPIO settings.
    """
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        open_gripper()
        time.sleep(2)
        close_gripper()
    except KeyboardInterrupt:
        cleanup()
    finally:
        cleanup()
```