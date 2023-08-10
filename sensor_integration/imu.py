```python
import smbus
import time

# Constants
BUS = 1
ADDRESS = 0x68

# Register addresses
ACCEL_XOUT_H = 0x3B
ACCEL_XOUT_L = 0x3C
ACCEL_YOUT_H = 0x3D
ACCEL_YOUT_L = 0x3E
ACCEL_ZOUT_H = 0x3F
ACCEL_ZOUT_L = 0x40

bus = smbus.SMBus(BUS)

def read_imu(register):
    high = bus.read_byte_data(ADDRESS, register)
    low = bus.read_byte_data(ADDRESS, register+1)

    value = (high << 8) + low

    if (value >= 0x8000):
        return -((65535 - value) + 1)
    else:
        return value

def read_acceleration():
    x = read_imu(ACCEL_XOUT_H) / 16384.0
    y = read_imu(ACCEL_YOUT_H) / 16384.0
    z = read_imu(ACCEL_ZOUT_H) / 16384.0

    return (x, y, z)

def read_orientation():
    acceleration = read_acceleration()

    pitch = 180 * math.atan(acceleration[0]/math.sqrt(acceleration[1]*acceleration[1] + acceleration[2]*acceleration[2]))/math.pi
    roll = 180 * math.atan(acceleration[1]/math.sqrt(acceleration[0]*acceleration[0] + acceleration[2]*acceleration[2]))/math.pi
    yaw = 180 * math.atan(acceleration[2]/math.sqrt(acceleration[0]*acceleration[0] + acceleration[1]*acceleration[1]))/math.pi

    return (pitch, roll, yaw)

if __name__ == "__main__":
    while True:
        print("Orientation: Pitch=%f, Roll=%f, Yaw=%f" % read_orientation())
        time.sleep(1)
```