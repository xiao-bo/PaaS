import sys
import numpy
import draw

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
def compute_delay(list_1,list_2):
    delay=[]
    #shift = 0.0000065
    shift = 0 
    i = 0
    for first,second in zip(list_1,list_2):
	delay.append(abs(first-second-shift*i)*1000)
	i=i+1
    return delay


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

    print "mean: "+str(numpy.mean(delay_list))
    print "standard deviation: "+str(numpy.std(delay_list))
    
    return [numpy.mean(delay_list),numpy.std(delay_list)]


def dataProcess(list_former,list_backer):

    ### insert integer 0.0 to recover miss part 
    #timestamp_former=align(list_former)
    #timestamp_backer=align(list_backer)
    ### compute delay between list
    #delay=compute_delay(timestamp_former,timestamp_backer)
    delay=compute_delay(list_former,list_backer)

    return delay
	

if __name__=='__main__':
    error_data=dataProcess()
    draw.curve(error_data,"s")
