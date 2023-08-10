```python
import serial
import time

# Constants
TELEMETRY_RADIO_PORT = '/dev/ttyUSB0'  # Update this based on your setup
TELEMETRY_RADIO_BAUDRATE = 57600

# Variables
communication_message = ''

# Initialize the telemetry radio
def init_telemetry_radio():
    try:
        telemetry_radio = serial.Serial(TELEMETRY_RADIO_PORT, TELEMETRY_RADIO_BAUDRATE)
        print("Telemetry radio initialized.")
        return telemetry_radio
    except Exception as e:
        print("Error initializing telemetry radio: ", str(e))
        return None

# Function to send data
def send_data(telemetry_radio, data):
    try:
        telemetry_radio.write(data.encode())
        print("Data sent: ", data)
    except Exception as e:
        print("Error sending data: ", str(e))

# Function to receive data
def receive_data(telemetry_radio):
    global communication_message
    try:
        if telemetry_radio.in_waiting > 0:
            communication_message = telemetry_radio.readline().decode().strip()
            print("Data received: ", communication_message)
    except Exception as e:
        print("Error receiving data: ", str(e))

# Main function
def main():
    telemetry_radio = init_telemetry_radio()
    if telemetry_radio is not None:
        while True:
            # Send and receive data here
            send_data(telemetry_radio, "Test data")
            receive_data(telemetry_radio)
            time.sleep(1)

if __name__ == "__main__":
    main()
```