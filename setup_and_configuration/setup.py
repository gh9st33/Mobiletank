```python
import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the motors, sensors, and other components
MOTOR_LEFT = 17
MOTOR_RIGHT = 27
ULTRASONIC_TRIGGER = 22
ULTRASONIC_ECHO = 23
SERVO = 24
GRIPPER = 25
NRF_CE = 8
NRF_CSN = 7
TELEMETRY_TX = 14
TELEMETRY_RX = 15

def setup():
    # Set the GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Setup the motor pins
    GPIO.setup(MOTOR_LEFT, GPIO.OUT)
    GPIO.setup(MOTOR_RIGHT, GPIO.OUT)

    # Setup the ultrasonic sensor pins
    GPIO.setup(ULTRASONIC_TRIGGER, GPIO.OUT)
    GPIO.setup(ULTRASONIC_ECHO, GPIO.IN)

    # Setup the servo and gripper pins
    GPIO.setup(SERVO, GPIO.OUT)
    GPIO.setup(GRIPPER, GPIO.OUT)

    # Setup the NRF radio pins
    GPIO.setup(NRF_CE, GPIO.OUT)
    GPIO.setup(NRF_CSN, GPIO.OUT)

    # Setup the telemetry radio pins
    GPIO.setup(TELEMETRY_TX, GPIO.OUT)
    GPIO.setup(TELEMETRY_RX, GPIO.IN)

    print("Setup complete")

def cleanup():
    # Clean up the GPIO pins before exiting
    GPIO.cleanup()
    print("Cleanup complete")

if __name__ == "__main__":
    try:
        setup()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        cleanup()
```