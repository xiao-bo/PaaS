# Message Sender for edison 
import sys
import time
import os
import mraa
import datetime
import threading
from socket import *
from math import *
host = "10.8.0.8" # set to IP address of target computer
port = 13000
lb=(sin(1010*pi/1000)+2.5)*1024/5
ub=(sin(990*pi/1000)+2.5)*1024/5
lb_i=floor(lb)
ub_i=floor(ub)

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
		
		pot=mraa.Aio(0)
		potVal=float(pot.read())
		return potVal
if __name__=='__main__':
	client=Edison(host,port)
        while True:
            date_time=datetime.datetime.now()
	    potVal=client.analog_read()
            if  ub_i>=potVal and potVal >=lb_i: 
                message=str(potVal)+' '+str(date_time)
                client.send_message(message)
                print message
                time.sleep(0.005)	
        TCPSock.close()
'''
addr=(host,port)
TCPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    pot=mraa.Aio(0)
    date_time=str(datetime.datetime.now())
    potVal=pot.read()
    if  ub_i>=potVal and potVal >=lb_i:
        message=str(potVal)+' '+date_time
        TCPSock.sendto(message,addr)
        time.sleep(0.005)
TCPSock.close()

'''
