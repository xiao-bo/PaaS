import datetime
import time
import sys
import os
os.system("sh preprocess.sh")
array=[]
readline=open("new.txt","rb")
send_time=[]
receive_time=[]
for line in readline:
	send=line.split(":")[2]
	send_time.append(send)

for x in range(0,len(send_time)-1):
	print float(send_time[x+1])-float(send_time[x])

print '========'
#for x in range(0,len(receive_time)-1):
	#print float(receive_time[x+1])-float(receive_time[x])



