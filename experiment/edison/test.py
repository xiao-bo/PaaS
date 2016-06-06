import datetime
import time
import sys
array=[]
'''
fo=open("exit.txt","wb")
for x in range(1,100):
	t=datetime.datetime.now()
	a=str(t).split(':')[2]
	array.append(a)
	print a
	fo.write(a+'\n')
	time.sleep(0.001)
	
fo.close()
for x in range(0,len(array)-1):
	ans=float(array[x+1])-float(array[x])
	print ans
'''
readline=open("data.txt","rb")
send_time=[]
receive_time=[]
for line in readline:
	send=line.split(":")[3]
	rece=line.split(":")[6]
	#print 'send:'+str(send)
	#print 'rece:'+str(rece)
	send_time.append(send)
	receive_time.append(rece)

for x in range(0,len(send_time)-1):
	print float(send_time[x+1])-float(send_time[x])

print '========'
for x in range(0,len(receive_time)-1):
	print float(receive_time[x+1])-float(receive_time[x])



