# Message Receiver
import os
from socket import *
import time
import datetime
import subprocess
import sys
host = ""
port = 13000
buf = 1024
filename=sys.argv[1]+"%.txt"
cmd=["cat /var/run/ptpd2.status.log|grep 'Offset'"]
cmd2=["ksh -c 'printf \"%(%s.%N)T\'"]

class server:
	def __init__(self,port,host):
		self.port=port
		self.host=host
        
	def receive(self):
		print filename
        addr=(host,port)
        Sock = socket(AF_INET, SOCK_STREAM)
        #Sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        Sock.bind(addr)
        Sock.listen(5)
        print "Waiting to receive messages..."
        fo=open(filename,"wb")
        while True:
            (csock,adr)= Sock.accept()
            send_time=csock.recv(10240)
            rece_time=subprocess.check_output(cmd2,shell=True) 
            #send_time=data.split(':')[2]## let send time +offset
            ans=str(send_time)+": mac time:rece_time:"+str(rece_time)

            print float(rece_time)-float(send_time)
            print ans
            fo.write(ans+'\n')
        csock.close()
        fo.close()
	
		

if __name__=="__main__":
    
    
    print "sss"
    #macbook=server(port,host,filename)
    #macbook.receive(filename)