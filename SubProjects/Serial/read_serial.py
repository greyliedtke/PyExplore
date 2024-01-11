import serial
import time

#initialize serial port
ser = serial.Serial('COM3', 115200, xonxoff=True)
ser.timeout = 1 #specify timeout when using readline()
ser.close()
ser.open()
if ser.is_open==True:
	print("\nAll right, serial port now open. Configuration:\n")
	print(ser, "\n") #print serial parameters
	
while True:
	d = ser.read()
	# ser.reset_input_buffer()
	if d:
		data = eval(d)
		print(data)
	time.sleep(.5)