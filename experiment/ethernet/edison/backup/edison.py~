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
host = "10.8.0.31" # set to IP address of target computer
port = 13000
lb=(sin(1010*pi/1000)+2.5)*1024/5
ub=(sin(990*pi/1000)+2.5)*1024/5
lb_i=floor(lb)
ub_i=floor(ub)
cmd=["ksh -c 'printf \"%(%s.%N)T'"]
class Edison:
	def __init__(self,host,port):
		self.host=host
		self.port=port
	def send_message(self,message):
		addr=(self.host,self.port)
		TCPSock = socket(AF_INET, SOCK_DGRAM)
		TCPSock.sendto(str(message),addr)
		#TCPSock.close()
	
	def analog_read(self):
		
		pot=mraa.Aio(2)
		potVal=float(pot.read())
		return potVal
if __name__=='__main__':
	client=Edison(host,port)
        while True:
	    #potVal=client.analog_read()
            content=subprocess.check_output(cmd,shell=True)
	    pot=mraa.Aio(2)
	    potVal=float(pot.read())
            if potVal>=1020:
                message=str(potVal)+':ss:'+str(content)
                #date_time=datetime.datetime.now()
                #message=str(potVal)+' '+str(date_time)
                client.send_message(message)
                print message
                time.sleep(0.2)	
        TCPSock.close()
