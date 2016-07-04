# Message Sender for control bandwidth  
import sys
import time
import os
from socket import *
host = "10.8.0.35" # set to IP address of target computer
port = 13000

class Sender:
	def __init__(self,host,port):
		self.host=host
		self.port=port
	def send_message(self,message):
		addr=(self.host,self.port)
		TCPSock = socket(AF_INET, SOCK_DGRAM)
		TCPSock.sendto(str(message),addr)
		TCPSock.close()
	
if __name__=='__main__':
	message="message~~~~~"
	client=Edison(host,port)
	client.send_message(message)
