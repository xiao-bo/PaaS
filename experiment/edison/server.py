# Message Receiver
import os
from socket import *
import time
import datetime
import subprocess
host = ""
port = 13000
buf = 1024
cmd=["cat /var/run/ptpd2.status.log|grep 'Offset'"]
cmd2=["ksh -c 'printf \"%(%s.%N)T\'"]
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
			content=subprocess.check_output(cmd,shell=True)## get sync offset  
			content2=subprocess.check_output(cmd2,shell=True)## get sync offset  
		        (data, addr) = TCPSock.recvfrom(buf)
                        
                        ###offset = rece-send
			content=content.split(':')[1]
			offset=content.split(',')[0]
			offset=offset.split("s")[0]
			send_time=data.split(':')[2]## let send time +offset
			#send_time=float(send_time)+float(offset)
                        #ans=str(send_time)+": mac time "+str(datetime.datetime.now())
                        ans=str(send_time)+": mac time:s:"+str(content2)

			ti=str(datetime.datetime)
			#tmp=ti.split(':')[2]

			print "offset"+str(offset)
			print float(content2)-float(send_time)
			print ans
                        print time.time()
			fo.write(ans+'\n')
		fo.close()
	
		
		

if __name__=="__main__":
	macbook=server(port,host)
	macbook.TCP_receive()
