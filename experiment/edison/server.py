# Message Receiver
import os
from socket import *
import time
import datetime
import subprocess
import sys
host = "192.168.11.8"
#host="140.112.28.139"
port = int(sys.argv[2])
buf = 1024
filename=sys.argv[1]+".txt"
cmd=["cat /var/run/ptpd2.status.log|grep 'Offset'"]

if __name__=="__main__":
    
    
    print "sss"
    addr=(host,port)
    Sock = socket(AF_INET, SOCK_STREAM)
    Sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    Sock.bind(addr)
    Sock.listen(5)
    print "Waiting to receive messages..."
    fo=open(filename,"wb")
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
