# Message Sender for edison 
import sys
import time
import os
import mraa
import datetime
import threading
from socket import *
from math import *
import subprocess
host = "192.168.11.3" # set to IP address of target computer
port = 12000
#cmd=["ksh -c 'printf \"%(%s.%N)T'"]
if __name__=='__main__':
	addr=(host,port)
	TCPSock = socket(AF_INET, SOCK_STREAM)
        TCPSock.connect(addr)
        while True:
	    #potVal=client.analog_read()
            #content=subprocess.check_output(cmd,shell=True)
	    pot=mraa.Aio(1)
	    potVal=int(pot.read())
            #print potVal;
            if potVal>=1010 or potVal<30:
                #message=str(potVal)+':ss:'+str(content)
                timestamp = time.time()
                message = str(potVal)+":"+str(timestamp)
                #date_time=datetime.datetime.now()
                #message=str(potVal)+' '+str(date_time)
	        TCPSock.send(message)
                print message
                time.sleep(0.2)	
        TCPSock.close()
