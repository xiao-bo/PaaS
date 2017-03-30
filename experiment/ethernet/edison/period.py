import datetime
import time
import sys

def compute_delay(list_1,list_2):
	delay=[]
	for first,second in zip(list_1,list_2):
		if first==0 or second==0 :
			continue
		elif abs(float(first)-float(second))<50:
		### minute different will lead value larger 50
			delay.append(float(first)-float(second))
			
	return delay

array=[]
readline=open("data.txt","rb")
send_time=[]
receive_time=[]
for line in readline:
	send=line.split(":")[0]
	#rece=line.split(":")[3]
	#print 'send:'+str(send)
	#print 'rece:'+str(rece)
	send_time.append(send)
	#receive_time.append(rece)
for x in range(0,len(send_time)-1):
    if float(send_time[x+1])-float(send_time[x]) <1:
        print float(send_time[x+1])-float(send_time[x]) 

'''
print '========'
for x in range(0,len(receive_time)-1):
	print float(receive_time[x+1])-float(receive_time[x])
'''

#print compute_delay(receive_time,send_time)

