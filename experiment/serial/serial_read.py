
##serial_read.py is for macbook read serial signal
import serial
import datetime
ser = serial.Serial(
    port='/dev/tty.usbmodem1411',\
    baudrate=9600,)
fo=open("serial_data.txt","wb")
while True:
	line=ser.readline()
	ans=line+str(datetime.datetime.now())
	print ans
	fo.write(ans+'\n')
fo.close()
ser.close()
