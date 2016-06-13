
##serial_read.py is for macbook read serial signal
import serial
import datetime
import time
ser = serial.Serial(
    port='/dev/tty.usbmodem1421',\
    baudrate=9600,)
fo=open("data.txt","wb")
while True:
	line=ser.readline()
	#print line
	#tmp=''.join(line.split('\n'))
	#print tmp
	#print tmp+(str(datetime.datetime.now())
	ans=line+' '+str(datetime.datetime.now())+' '
	print ans
	fo.write(ans+'\n')
	#time.sleep(0.05)
fo.close()
ser.close()
