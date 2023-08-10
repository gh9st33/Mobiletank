```python
import RPi.GPIO as GPIO
import spidev
import time

# NRF24L01 registers
CONFIG      = 0x00
EN_AA       = 0x01
EN_RXADDR   = 0x02
SETUP_AW    = 0x03
SETUP_RETR  = 0x04
RF_CH       = 0x05
RF_SETUP    = 0x06
STATUS      = 0x07
OBSERVE_TX  = 0x08
CD          = 0x09
RX_ADDR_P0  = 0x0A
TX_ADDR     = 0x10
RX_PW_P0    = 0x11
FIFO_STATUS = 0x17
PAYLOAD     = 0x61
FLUSH_TX    = 0xE1
FLUSH_RX    = 0xE2
REUSE_TX_PL = 0xE3
NOP         = 0xFF

# GPIO pins
CE_PIN = 17
CSN_PIN = 27

# SPI device
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 500000

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(CE_PIN, GPIO.OUT)
GPIO.setup(CSN_PIN, GPIO.OUT)

def nrf_command(cmd):
    GPIO.output(CSN_PIN, GPIO.LOW)
    status = spi.xfer2([cmd])[0]
    GPIO.output(CSN_PIN, GPIO.HIGH)
    return status

def nrf_read_register(reg):
    GPIO.output(CSN_PIN, GPIO.LOW)
    status = spi.xfer2([reg, NOP])[0]
    GPIO.output(CSN_PIN, GPIO.HIGH)
    return status

def nrf_write_register(reg, value):
    GPIO.output(CSN_PIN, GPIO.LOW)
    status = spi.xfer2([reg | 0x20, value])[0]
    GPIO.output(CSN_PIN, GPIO.HIGH)
    return status

def nrf_send_payload(payload):
    GPIO.output(CSN_PIN, GPIO.LOW)
    status = spi.xfer2([PAYLOAD] + payload)
    GPIO.output(CSN_PIN, GPIO.HIGH)
    return status

def nrf_flush_tx():
    return nrf_command(FLUSH_TX)

def nrf_flush_rx():
    return nrf_command(FLUSH_RX)

def nrf_send_message(message):
    nrf_flush_tx()
    nrf_send_payload([ord(c) for c in message])
    GPIO.output(CE_PIN, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(CE_PIN, GPIO.LOW)

def nrf_receive_message():
    nrf_flush_rx()
    GPIO.output(CE_PIN, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(CE_PIN, GPIO.LOW)
    status = nrf_read_register(STATUS)
    if status & 0x40:
        GPIO.output(CSN_PIN, GPIO.LOW)
        spi.xfer2([0x61])
        message = spi.readbytes(nrf_read_register(RX_PW_P0))
        GPIO.output(CSN_PIN, GPIO.HIGH)
        return ''.join([chr(c) for c in message])
    else:
        return None
```