# Message Sender for edison 
import sys
import time
import os
import mraa
import datetime
from socket import *
#host = "192.168.0.100" # set to IP address of target computer
host = "10.8.0.35" # set to IP address of target computer
port = 13000

class Edison:
	def __init__(self,host,port):
		self.host=host
		self.port=port
	def send_message(self,message):
		addr=(self.host,self.port)
		TCPSock = socket(AF_INET, SOCK_DGRAM)
		TCPSock.sendto(str(message),addr)
		TCPSock.close()
	
	def analog_read(self):
		
		pot=mraa.Aio(0)
		potVal=float(pot.read())
		return potVal
	
if __name__=='__main__':
	client=Edison(host,port)
	#for x in range(1,10000):
        fo=open("data.txt","wb")
        while True:
	    potVal=client.analog_read()
            message=str(potVal)+' '+str(datetime.datetime.now())
	    #client.send_message(str(potVal)+' '+str(datetime.datetime.now())
            client.send_message(message)
            fo.write(message+'\n')
            print message
            time.sleep(0.018)


            #client.send_message(x)

