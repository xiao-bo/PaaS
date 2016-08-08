# Message Receiver
import os
from socket import *
import time
import datetime
import subprocess
import sys

## Initial server ip address and port
host = "192.168.11.8"
#host="140.112.28.139"
port = int(sys.argv[2])
addr=(host,port)

## name of file
filename=sys.argv[1]+".txt"


if __name__=="__main__":
    
    ## initial socket property
    Sock = socket(AF_INET, SOCK_STREAM)

    ## reuse socket immediately 
    Sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    ## bind the socket to the port and ip address
    Sock.bind(addr)

    ## listen for incoming connections
    Sock.listen(5)
    print "Waiting to receive messages..."

    fo=open(filename,"wb")

    ##  build socket connection 
    connection,client_address= Sock.accept()
    
    while True:
        send_time=connection.recv(60)
        rece_time=time.time()
        ans=str(send_time)+": mac time:rece_time:%.9f"%rece_time
        #print float(rece_time)-float(send_time)
        print ans
        fo.write(ans+'\n')
    
    csock.close()
    fo.close()
