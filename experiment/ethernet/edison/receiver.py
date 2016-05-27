# Message Receiver
import os
#import datatime 
from socket import *

host = ""
port = 13000
buf = 1024
addr = (host, port)
TCPSock = socket(AF_INET, SOCK_DGRAM)
TCPSock.bind(addr)
print "Waiting to receive messages..."
while True:
	(data, addr) = TCPSock.recvfrom(buf)
	print "Received message: " + data #+ "time "+str(datetime.datetime.now())
	if data == "exit":
		TCPSock.close()
		os._exit(0)

