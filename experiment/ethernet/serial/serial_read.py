
##serial_read.py is for macbook read serial signal
import serial
import datetime
import time
import subprocess
cmd=["ksh -c 'printf \"%(%s.%N)T\'"]
ser = serial.Serial(
    port='/dev/ttyACM1',\
    baudrate=115200,)
fo=open("old.txt","wb")
while True:
    line=ser.readline()
    #ans=line+' '+str(datetime.datetime.now())+' '        
    content=subprocess.check_output(cmd,shell=True)
    ans=line+' 2016-07-05 04:@@:'+content
    print ans
    fo.write(ans+'\n')
    #time.sleep(0.05)
fo.close()
ser.close()
