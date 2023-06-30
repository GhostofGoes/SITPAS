#!/usr/bin/env python3

# PySerial library.
# https://pyserial.readthedocs.io/en/latest/index.html
#
# To install:
#   pip install pyserial
#
# List available serial ports:
#   python -m serial.tools.list_ports

import serial

# Names of ports vary by Operating System.
#
# Windows: COM1, COM2, etc.
# Linux: /dev/ttyUSB0 (USB), /dev/ttyS0 (RS232)

with open("/dev/tx", "w") as f:
    f.write("hello satellite")

with open("/dev/rx", "r") as f:
    print(f.read())

# Create an instance of the Serial object
# This also "opens" the port for use.
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=9600,
    # bytesize=8,  # 8N1
    # parity='N',
    # stopbits=1,
    timeout=5.0,
    # rtscts=False,  # clear-to-send
)

print(ser.name)  # check which port was really used
print(ser.baudrate)

# write a string
ser.write(b'hello')
'j'
b'\x6a'

# read 50 bytes
while True:
    bytes_read = ser.read(size=50)
    print(bytes_read)

# close port
ser.close()

with serial.Serial(port="COM3") as ser:
    print(ser.name)
    ser.write(b"hello")
    print(ser.read(size=50))
    return True

print("end")