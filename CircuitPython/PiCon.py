"""
file for interfacing to pi pico
- create simple gui for interfacing to pi pico
"""

import serial
import time
import serial.tools.list_ports

# 1. List available and select devices
# --------------------------------------------2----------
# Get a list of available serial ports
available_ports = serial.tools.list_ports.comports()
devs = {}
for i, port in enumerate(available_ports):
    devs[i] = port

for key, value in devs.items():
    print(f"{key}: {value}")
p = input("Enter port number from : ")
device = devs[int(p)]
print(f"Selected port: {device}")

# 2. Open the selected port
# ------------------------------------------------------
ser = serial.Serial(device.device, 115200, xonxoff=True)
ser.timeout = 1 #specify timeout when using readline()
ser.close()
ser.open()
if ser.is_open==True:
	print(f"Listening on: {device}")

while True:
    d = ser.readline()
    if d:
        d = d.decode()
        d = d.replace("\r\n", "")
        print(d)
    time.sleep(.1)
