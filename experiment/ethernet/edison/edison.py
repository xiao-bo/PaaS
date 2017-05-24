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
        change = 0 
	addr = (host,port)
	TCPSock = socket(AF_INET, SOCK_STREAM)
        TCPSock.connect(addr)
        while True:
	    #potVal=client.analog_read()
            #content=subprocess.check_output(cmd,shell=True)
	    pot=mraa.Aio(3)
	    potVal=pot.read()
            #print potVal
            if potVal != change :
                timestamp = time.time()
                message = str(potVal)+":"+str(timestamp)
	        TCPSock.send(message)
                #print message
                change=potVal
                #time.sleep(0.4)	
        TCPSock.close()
