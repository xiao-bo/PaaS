# Message Sender for edison 
import sys
import time
import os
from socket import *
host = "192.168.0.100" # set to IP address of target computer
#host = "10.1.2.11" # set to IP address of target computer
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
	"""
	def analog_read(self):
		
		pot=mraa.Aio(0)
		potVal=float(pot.read())
		#time.sleep(0.01)
		return potVal
	"""
if __name__=='__main__':
	client=Edison(host,port)
	for x in range(1,100):
		#potVal=client.analog_read()
		#client.send_message(potVal)
		client.send_message(x)

