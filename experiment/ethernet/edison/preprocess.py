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
readline=open("1.txt","rb")
fo=open("data.txt","wb")
send_time=[]
for line in readline:
	send=line.split(".")[1]
	ans=send.split(":")[0]
	print ans
        fo.write(ans+"\n")


