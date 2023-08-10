```python
import serial
import pynmea2

# Constants
SERIAL_PORT = "/dev/serial0"
BAUD_RATE = 9600

# Variables
gps_coordinates = None

def setup_gps_module():
    """
    Setup the GPS module by initializing the serial port.
    """
    global gps_serial
    gps_serial = serial.Serial(SERIAL_PORT, baudrate=BAUD_RATE, timeout=1)

def read_gps():
    """
    Read data from the GPS module and parse the NMEA sentences.
    """
    global gps_coordinates
    while True:
        sentence = gps_serial.readline().decode('utf-8')
        if sentence[0:6] == "$GPGGA":
            data = pynmea2.parse(sentence)
            gps_coordinates = (data.latitude, data.longitude)
            return gps_coordinates

def get_gps_coordinates():
    """
    Return the latest GPS coordinates.
    """
    return gps_coordinates

# Setup the GPS module when the script is run
if __name__ == "__main__":
    setup_gps_module()
    while True:
        print(read_gps())
```