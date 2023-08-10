```python
import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the motor driver
MOTOR1A = 17
MOTOR1B = 27
MOTOR2A = 23
MOTOR2B = 24

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR1A, GPIO.OUT)
GPIO.setup(MOTOR1B, GPIO.OUT)
GPIO.setup(MOTOR2A, GPIO.OUT)
GPIO.setup(MOTOR2B, GPIO.OUT)

# Define the motor speed
motor_speed = 100

# Create PWM objects
motor1 = GPIO.PWM(MOTOR1A, motor_speed)
motor2 = GPIO.PWM(MOTOR2A, motor_speed)

def drive_forward():
    motor1.start(0)
    motor2.start(0)
    motor1.ChangeDutyCycle(motor_speed)
    motor2.ChangeDutyCycle(motor_speed)
    GPIO.output(MOTOR1A, GPIO.HIGH)
    GPIO.output(MOTOR1B, GPIO.LOW)
    GPIO.output(MOTOR2A, GPIO.HIGH)
    GPIO.output(MOTOR2B, GPIO.LOW)

def drive_backward():
    motor1.start(0)
    motor2.start(0)
    motor1.ChangeDutyCycle(motor_speed)
    motor2.ChangeDutyCycle(motor_speed)
    GPIO.output(MOTOR1A, GPIO.LOW)
    GPIO.output(MOTOR1B, GPIO.HIGH)
    GPIO.output(MOTOR2A, GPIO.LOW)
    GPIO.output(MOTOR2B, GPIO.HIGH)

def turn_left():
    motor1.start(0)
    motor2.start(0)
    motor1.ChangeDutyCycle(motor_speed)
    motor2.ChangeDutyCycle(motor_speed)
    GPIO.output(MOTOR1A, GPIO.LOW)
    GPIO.output(MOTOR1B, GPIO.HIGH)
    GPIO.output(MOTOR2A, GPIO.HIGH)
    GPIO.output(MOTOR2B, GPIO.LOW)

def turn_right():
    motor1.start(0)
    motor2.start(0)
    motor1.ChangeDutyCycle(motor_speed)
    motor2.ChangeDutyCycle(motor_speed)
    GPIO.output(MOTOR1A, GPIO.HIGH)
    GPIO.output(MOTOR1B, GPIO.LOW)
    GPIO.output(MOTOR2A, GPIO.LOW)
    GPIO.output(MOTOR2B, GPIO.HIGH)

def stop():
    motor1.stop()
    motor2.stop()
    GPIO.output(MOTOR1A, GPIO.LOW)
    GPIO.output(MOTOR1B, GPIO.LOW)
    GPIO.output(MOTOR2A, GPIO.LOW)
    GPIO.output(MOTOR2B, GPIO.LOW)

if __name__ == "__main__":
    try:
        while True:
            drive_forward()
            time.sleep(2)
            stop()
            time.sleep(1)
            drive_backward()
            time.sleep(2)
            stop()
            time.sleep(1)
            turn_left()
            time.sleep(2)
            stop()
            time.sleep(1)
            turn_right()
            time.sleep(2)
            stop()
            time.sleep(1)
    except KeyboardInterrupt:
        stop()
        GPIO.cleanup()
```