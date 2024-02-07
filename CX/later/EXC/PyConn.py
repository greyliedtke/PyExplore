"""
file for interfacing to pi pico
- create simple gui for interfacing to pi pico
"""

import serial
import time
import serial.tools.list_ports
import PySimpleGUI as sg


# 1. List available and select devices
# ------------------------------------------------------
# Get a list of available serial ports
available_ports = serial.tools.list_ports.comports()
# Print the list of available serial ports
devices = [port.device for port in available_ports]
for port in available_ports:
     print(port)

# select port config
layout_device = [
    [sg.Text('Select your device:')],
    [sg.Combo(devices, default_value='COM3', key='-port-')],
    [sg.Button('Submit')]
]
window = sg.Window('Select Device', layout_device)

# Event loop
port = None
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Submit':
        print(f"Selected port: {values['-port-']}")
        port = values['-port-']
        break

# Close the window
window.close()

# 2. Open the selected port
# ------------------------------------------------------
ser = serial.Serial(port, 115200, xonxoff=True)
ser.timeout = 1 #specify timeout when using readline()
ser.close()
ser.open()
if ser.is_open==True:
	print("Listening on port: ", port)

# select port config
layout_device = [
    [sg.Multiline(default_text='', size=(40, 10), key='-TEXT_AREA-', disabled=True, autoscroll=True)],
]
window = sg.Window('Pico', layout_device)

tt = ""

while True:
    event, values = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break
    else:
        d = ser.readline()
        if d:
            d = d.decode()
            tt += d
            window['-TEXT_AREA-'].update(value=tt)

window.close()

# [sg.InputText(key='-term_input-', size=(80, 1)), sg.Button('Send')],
# elif event == 'Send':
#     command = values['-term_input-']
#     ser.write(command.encode())
#     # ser.reset_output_buffer()
#     # ser.reset_input_buffer()
#     print(f">>> {command}")  # Echo the command in the terminal