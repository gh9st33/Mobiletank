```python
import time
from sensor_integration.ultrasonic_sensor import read_ultrasonic
from sensor_integration.imu import read_imu
from motor_control.motor_driver import drive_forward, drive_backward, turn_left, turn_right

# Constants
OBSTACLE_DISTANCE_THRESHOLD = 10  # in cm
TURN_TIME = 1  # in seconds

def navigate():
    while True:
        # Read sensor data
        obstacle_distance = read_ultrasonic()
        imu_orientation = read_imu()

        # If an obstacle is detected
        if obstacle_distance < OBSTACLE_DISTANCE_THRESHOLD:
            # Stop moving forward
            drive_backward()
            time.sleep(TURN_TIME)
            # Turn to avoid the obstacle
            turn_left()
            time.sleep(TURN_TIME)
            drive_forward()
        else:
            # If no obstacle is detected, continue moving forward
            drive_forward()

if __name__ == "__main__":
    navigate()
```
This code will make the robot move forward until it detects an obstacle within 10 cm. When an obstacle is detected, the robot will stop, move backward for 1 second, turn left for 1 second, and then continue moving forward. The robot's orientation is read from the imu but not used in this simple navigation algorithm. In a more advanced version, the imu data could be used to help the robot navigate more complex environments.