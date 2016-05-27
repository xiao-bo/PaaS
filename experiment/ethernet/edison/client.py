# Message Sender for edison 
import os
from socket import *
host = "10.1.2.11" # set to IP address of target computer
port = 13000
addr = (host, port)
TCPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = raw_input("Enter message to send or type 'exit': ")
    for x in range (1,100):

        TCPSock.sendto(str(x), addr)
    if data == 'exit':
        
        TCPSock.close()
        os._exit(0)
