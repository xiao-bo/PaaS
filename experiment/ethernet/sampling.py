import datetime
import time
import sys
import draw
import numpy
import data_processing as dp

def CounterInterval(CounterList):
    ListInterval=[]
    for x in range(0,len(CounterList)-1):
        ListInterval.append((float(CounterList[x+1])-float(CounterList[x]))/1000000)
    for x in ListInterval:
        print x
    return ListInterval

def getRealClockIntervalForMillisecond(RealClockList):
    ListInterval=[]
    RealClockListMicrosecond=[]## microsecond level , 0.923423s=923423 us
    ## for >1hz
    ## get part of time ms because data contain problem, for example
    ## in 10HZ, 9.923 become 10.23  , in fact, 10.23 mean 10.023,
    ## because of ms overflow.
    for x in range(0,len(RealClockList)-1):
        RealClockListMicrosecond.append(RealClockList[x].split(".")[1])
        print RealClockList[x].split(".")[1]

    for x in range(0,len(RealClockListMicrosecond)-1):
        Interval=float(RealClockListMicrosecond[x+1])-float(RealClockListMicrosecond[x])
        ##prevent 1.100-0.99000 , because split time into s , ms,
        ## so above become 0.100-0.99000, and I will skip this situation
        if Interval>0.0:
            ListInterval.append(Interval/10000)## get millsecond
            
    return ListInterval

def getRealClockInterval(RealClockList):
    ListInterval=[]
    for x in range(0,len(RealClockList)-1):
        Interval=float(RealClockList[x+1])-float(RealClockList[x])
        #if tmp<1.95:
        ListInterval.append(Interval)
    
    return ListInterval

def getSamplingBias(ListInterval,freq):
    Bias=[]
    for x in ListInterval:
        Interval=float(x)-(1.0/freq)
        Bias.append(abs(Interval)*1000)
    return Bias


if __name__=='__main__':

    board=sys.argv[1]
    freq=sys.argv[2]
    sendTime=[]
    sendInterval=[]
    sendSamplingBias=[]
    
    if board=="arduino": ## for 1 hz
        readline=open("save/scalable/different_freq/arduino_1Hz.txt","rb")
        for line in readline:
	    send=line.split(":")[0]## for arduino
	    sendTime.append(send)
        sendInterval=CounterInterval(sendTime) ##for arduino
        Title="arduino sender's sampling error in "+freq+"hz"
    elif board=="edison":
        if freq=="1":## for 1 Hz
            readline=open("edison/edison_1023.txt","rb")
            for line in readline:
	        send=line.split(":")[0]## for arduino
	        sendTime.append(send)
            sendInterval=getRealClockInterval(sendTime)## for edison
            Title="edison's sampling period for 1023"
        else:## for all data
            readline=open("edison/edison_all_timer.txt","rb")
            for line in readline:
	        send=line.split(" ")[1]## for edison all data
	        sendTime.append(send)
            sendInterval=getRealClockIntervalForMillisecond(sendTime)## for edison
            statistics=[dp.compute_statistics(sendInterval)]
            Title="edison's sampling period for all data"
            draw.curve(sendInterval,Title,statistics)
        

    sendSamplingBias=getSamplingBias(sendInterval,float(freq))
    statistics=[dp.compute_statistics(sendSamplingBias)]
    draw.curve(sendSamplingBias,Title,statistics)
    
