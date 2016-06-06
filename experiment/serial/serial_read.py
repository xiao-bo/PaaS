
##serial_read.py is for macbook read serial signal
import serial
import datetime
import time
ser = serial.Serial(
    port='/dev/tty.usbmodem14231',\
    baudrate=9600,)
fo=open("data.txt","wb")
while True:
	line=ser.readline()
	tmp=line.strip('\n')
	#print tmp+' '+str(datetime.datetime.now())
	ans=line+' '+str(datetime.datetime.now())
	print ans
	fo.write(ans+'\n')
	#time.sleep(0.05)
fo.close()
ser.close()
