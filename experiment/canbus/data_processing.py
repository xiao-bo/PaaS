import sys
import numpy
import draw
import math
def ReadArduinoFile(filename,index):
    ##read data and append list
    file_read=open(filename,'r')
    S0timestamp = []
    S1timestamp = []
    S2timestamp = []
    for line in file_read:
        ans=line.split(":")
        if ans[1]=="0010":
            S0timestamp.append(float(ans[index]))
        elif ans[1]=="0011":
            S1timestamp.append(float(ans[index]))
        elif ans[1]=="0018":
            S2timestamp.append(float(ans[index]))
    
    return S0timestamp,S1timestamp,S2timestamp
	
def ReadEdisonFile(filename,index):
    ##read data and append list
    file_read = open(filename,'r')
    Etimestamp = []
    for line in file_read:
        ans=line.split(":")
        Etimestamp.append(float(ans[index]))
    return Etimestamp
def computeError(list_1,list_2,length):
    delay=[]
    #shift = 0.0000065
    shift = 0 
    i = 0
    for first,second in zip(list_1,list_2):
	delay.append(abs(first-second)*1000)
	i=i+1
        #print abs(first-second)
        if i > length:
            break
    return delay

def computeConfidience(list1,mean,std,):
    normal = []
    for x in list1:
        if x-mean<std :
            normal.append(x)
    
    confidience = float(len(normal))/float(len(list1))
    
    print ("confidience :{}").format(confidience)

def align(time_list):
    ## count number of zero because x can't ++ in 
    ##loop and lead number of loop shorter 
    count=0
    for x in range(0,len(time_list)-1): 
    	diff=time_list[x+1]-time_list[x]
    	#print diff
        if diff<0:
            diff=diff+60
	if diff>0.6:
	    for y in range(0,int(round(diff/0.5))-1):
		count=count+1
	for x in range(0,len(time_list)-1+count):
	    if time_list[x]==0:
	    	continue
	    diff=time_list[x+1]-time_list[x]
	    if diff<0:
		diff=diff+60
	    if diff>0.6:
		for y in range(0,int(round(diff/0.5))-1):## insert multiple zero
		    time_list.insert(x+1,0.0)

    return time_list

def time_sync(edison,offset):
    sync=[]
    ##offset = slave - master=mac - edison
    ##
    for x,y in zip(edison,offset):
	sync.append(x+float(y))
    return sync

def compute_statistics(delay_list):
    ##evalute average , standard deviation, mean square error
    delay_list=numpy.array(delay_list)
    length = len(delay_list)
    mean = numpy.mean(delay_list)
    std = numpy.std(delay_list)
    ste = std/math.sqrt(length)
    samplingError = ste/mean*100
    print "mean: "+str(mean)
    print "standard deviation: "+str(std)
    print "standard error:"+str(ste)
    print "sampling error:"+str(samplingError)+"%"
    
    return [numpy.mean(delay_list),numpy.std(delay_list),ste]
	

if __name__=='__main__':
    error_data=dataProcess()
    draw.curve(error_data,"s")
