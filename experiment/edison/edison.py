# Message Sender for edison 
import sys
import time
import os
import mraa
import datetime
import threading
from socket import *
from math import *
#host = "192.168.0.100" # set to IP address of target computer
host = "10.8.0.35" # set to IP address of target computer
#host="10.1.2.13"
port = 13000

'''	
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
        addr=(host,port)
        while True:
	    potVal=client.analog_read()
            message=str(potVal)+' '+str(datetime.datetime.now())
            #client.send_message(message)
	    TCPSock = socket(AF_INET, SOCK_DGRAM)
	    TCPSock.sendto(message,addr)
            print message
            #time.sleep(0.018)	
        TCPSock.close()
	fo.close()
'''
lb=(sin(1020*pi/1000)+2.5)*1024/5
ub=(sin(980*pi/1000)+2.5)*1024/5
lb_i=floor(lb)
ub_i=floor(ub)
addr=(host,port)
TCPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    #thread.start_new_thread(Thread_read,)
    #thread.start_new_thread(send_message,)
    
    pot=mraa.Aio(0)
    date_time=str(datetime.datetime.now())
    potVal=float(pot.read())
    #print potVal
    if  ub_i>=potVal and potVal >=lb_i:
        message=str(potVal)+' '+date_time
        #print message
        TCPSock.sendto(message,addr)
        time.sleep(0.010)	
    
TCPSock.close()
