import datetime
import time
import sys
import os
import subprocess
array=[]
count=0

fo=open("data.txt","wb")
#fo=open
while True: 
	cmd=["cat /var/run/ptpd2.status.log|grep 'Offset'"]
	content=subprocess.check_output(cmd,shell=True)
	content=content.split(':')[1]
	offset=content.split(',')[0]
	array.append(offset)
	count=count+1
	fo.write(str(count)+": "+str(offset)+'\n')
	print str(count)+": "+str(offset)
	time.sleep(0.5)

#readline=open("data.txt","wb")
#for line in readline:
#	print line
	#send=line.split(":")[2]
	#send_time.append(send)
'''
for x in range(0,len(send_time)-1):
	print float(send_time[x+1])-float(send_time[x])

print '========'
'''