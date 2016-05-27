
##serial_read.py is for macbook read serial signal
import serial
import datetime
ser = serial.Serial(
    port='/dev/tty.usbmodem1421',\
    baudrate=9600,\
        timeout=2)

while True:
	line=ser.readline()
	print line+str(datetime.datetime.now())
ser.close()
