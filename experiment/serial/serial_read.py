
##serial_read.py is for macbook read serial signal
import serial
import datetime
import time
ser = serial.Serial(
    port='/dev/tty.usbmodem1421',\
    baudrate=115200,)
fo=open("old.txt","wb")
while True:
	line=ser.readline()
	ans=line+' '+str(datetime.datetime.now())+' '
	print ans
	fo.write(ans+'\n')
	#time.sleep(0.05)
fo.close()
ser.close()
