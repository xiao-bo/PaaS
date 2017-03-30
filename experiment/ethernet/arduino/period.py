import datetime
import time
import sys
import draw
readline=open("arduino.txt","rb")
send_time=[]
receive_time=[]
for line in readline:
	send=line.split(":")[0]
	send_time.append(send)
	receive=line.split(":")[2]
	receive_time.append(send)

for x in range(0,len(send_time)-1):
	print float(send_time[x+1])-float(send_time[x])
print "======"
for x in range(0,len(receive_time)-1):
	print float(receive_time[x+1])-float(receive_time[x])

print len(receive_time)

