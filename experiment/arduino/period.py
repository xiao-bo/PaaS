import datetime
import time
import sys
readline=open("data.txt","rb")
send_time=[]
for line in readline:
	send=line.split(":")[2]
	send_time.append(send)

for x in range(0,len(send_time)-1):
	print float(send_time[x+1])-float(send_time[x])

