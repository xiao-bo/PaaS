import datetime
import time
import sys
from decimal import Decimal
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
readline=open("11.txt","rb")
fo=open("data.txt","wb")
send_time=[]
for line in readline:
    send=line.split(":")[1]
    print send
    ans=str(round(Decimal(send),4))
    ans=ans.split(".")[1]
    ans=int(ans)*1000000
    print ans
    fo.write(str(ans)+"\n")


