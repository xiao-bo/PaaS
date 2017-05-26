# Message Sender for edison 
import sys
import time
import mraa
import socket
host = "192.168.11.4" # set to IP address of target computer
port = 12000
if __name__=='__main__':
        change = 0
        pinNumber = 5
	addr = (host,port)
	TCPSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TCPSock.connect(addr)
        while True:
	    pot = mraa.Aio(pinNumber)
	    potVal = pot.read()
            #print potVal
            if potVal != change :
                timestamp = time.time()
                message = str(potVal)+":"+str(timestamp)
	        TCPSock.send(message)
                #print message
                change = potVal
        TCPSock.close()
