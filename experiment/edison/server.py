# Message Receiver
import os
from socket import *
import time
import datetime
host = ""
port = 13000
buf = 1024
#addr = (host, port)
#TCPSock = socket(AF_INET, SOCK_DGRAM)
#TCPSock.bind(addr)
print "Waiting to receive messages..."
#while True:
	#(data, addr) = TCPSock.recvfrom(buf)
	#print "Received message: " + data #+ "time "+str(datetime.datetime.now())
	#if data == "exit":
	#	TCPSock.close()
	#	os._exit(0)
class server:
	def __init__(self,port,host):
		self.port=port
		self.host=host
	def TCP_receive(self):
		addr=(self.host,self.port)
		TCPSock = socket(AF_INET, SOCK_DGRAM)
		TCPSock.bind(addr)
		print "Waiting to receive messages..."
		fo=open("data.txt","wb")
		while True:
			(data, addr) = TCPSock.recvfrom(buf)
			ans=data #": mac time "+str(datetime.datetime.now())
			print ans
			fo.write(ans+'\n')
		fo.close()
if __name__=="__main__":
	macbook=server(port,host)
	macbook.TCP_receive()
