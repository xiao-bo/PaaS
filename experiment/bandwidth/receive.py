# Message Receiver
import os
from socket import *
host = ""
port = 13000
buf = 1024

class server:
	def __init__(self,port,host):
		self.port=port
		self.host=host
	def TCP_receive(self):
		addr=(self.host,self.port)
		TCPSock = socket(AF_INET, SOCK_DGRAM)
		TCPSock.bind(addr)
		print "Waiting to receive messages..."
		while True:
			(data, addr) = TCPSock.recvfrom(buf)
			print data
	
		
		

if __name__=="__main__":
	macbook=server(port,host)
	macbook.TCP_receive()
