import math
from sensor import Sensor

def gcd(a,b):
    while b:
        a,b =b,a%b
    return a 
def lcm(a,b):
    return a*b / gcd(a,b)

def getHyperperiod(sensorGroup):
    length = len(sensorGroup)
    sumTransmissionTime = 0

    hyperperiod = lcm(sensorGroup[0].deadLine,sensorGroup[1].deadLine)
    for x in range(2,length):
        hyperperiod = lcm(hyperperiod,sensorGroup[x].deadLine)

    #print "hyperperiod = {}".format(hyperperiod)
    return hyperperiod

def isSchedule(sensorGroup,target):
    length = len(sensorGroup)
    
    utilijation = 0.0
    for x in range(0,length):
        utilijation = utilijation + sensorGroup[x].transmissionTime \
            /sensorGroup[x].deadLine
 
    ### what is it???
    #if utilijation > 0.35:
        #print "utilijation >1, no schedule"
    #    return False
    

    #print "target = {}".format(target)
    responseTime = getResponseTime(sensorGroup,target)
    #print "responseTime = {}".format(responseTime)
    if responseTime <= sensorGroup[target].deadLine+sensorGroup[target].arrivalTime:
        return True
    else:
        return False
    
   
def getWaitingTime(waitingTime,blockingTime,higherPriority,transmissionTime,q):
    waitIndex = 1

    while True:
        tmp = waitingTime
        higherTime = 0 
        for x in range(0,len(higherPriority)):
            higherTime = higherTime + math.ceil(\
                (waitingTime + higherPriority[x].arrivalTime+0.01)/higherPriority[x].deadLine)\
                *higherPriority[x].transmissionTime
        higherTime = higherTime + q * transmissionTime
        waitingTime = blockingTime + higherTime
        
        #print "wait^{} ({}) = {}".format(waitIndex,q,waitingTime)
        if waitingTime == tmp:
            break
        waitIndex = waitIndex +1 
    return waitingTime


def gettm(tm,blockingTime,higherPriority,target):
    tmIndex = 1
    
    while True:
        tmp = tm
        higherTime = 0 
        for x in range(0,len(higherPriority)):
            higherTime = higherTime + math.ceil(\
                (tm + higherPriority[x].arrivalTime)/higherPriority[x].deadLine)\
                *higherPriority[x].transmissionTime
        higherTime = higherTime + math.ceil(\
                (tm + target.arrivalTime)/target.deadLine)*target.transmissionTime
        #print "higherTime = {}".format(higherTime)
        tm = blockingTime + higherTime
        
        #print "tm^{} = {}".format(tmIndex,tm)
        
        if tm == tmp:
            break
        tmIndex = tmIndex +1

    return tm

def getResponseTime(sensorGroup,targetIndex):
    
    length = len(sensorGroup)
    lowerPriority = []
    higherPriority = []
    maxlp = 0  
    blockingTime = 0
    waitingTime = []
    responseTime = []
    ## get lowerPriority list
    for i in range(0,length):
        if i == targetIndex:
            continue
        if sensorGroup[i].priority > sensorGroup[targetIndex].priority:
            lowerPriority.append(sensorGroup[i].priority)
        elif sensorGroup[i].priority < sensorGroup[targetIndex].priority:
            higherPriority.append(sensorGroup[i])
    
    
    ## lowerPrioirty is not empty. in other word, 
    ## there have lower priority object in sensorGroup
    '''
    maxblock = 0
    if lowerPriority: 
        ## get maximum priority in lower priority
        #maxlp = min(lowerPriority)  
        ## search priority maxlp in sensorGroup
        for i in range(0,length): 
            if maxblock < sensorGroup[i].transmissionTime and sensorGroup[i].priority > 0:
                maxblock = sensorGroup[i].transmissionTime
                print i
        blockingTime = maxblock 
    
    print "blockingTime = {}".format(blockingTime)
    '''
    ### get blockTime
    maxblock = 0
    for x in sensorGroup:
        if sensorGroup[targetIndex].priority < x.priority  and maxblock < x.transmissionTime :
            maxblock = x.transmissionTime
    blockingTime = maxblock
    #print "blockingTime = {}".format(blockingTime)
   
    ## initial tm^0
    tm = sensorGroup[targetIndex].transmissionTime

    ## get finial tm
    tm = gettm(tm,blockingTime,higherPriority,sensorGroup[targetIndex])
    ## get Qm
    Qm = math.ceil((tm+sensorGroup[targetIndex].arrivalTime)/sensorGroup[targetIndex].deadLine)
    
    #print "Qm={}".format(Qm)
    #print "tm={}".format(tm)
    

    
    q = 0

    ## get maximum response time
    while q< Qm:
        ## get blockTime
        if q == 0:
            waitingTime.append(blockingTime)
            #print "blockingTime = {}".format(blockingTime)
        

        elif q > 0:
            waitingTime.append(waitingTime[q-1] + sensorGroup[targetIndex].transmissionTime)
            #print "waitingTime({}) = {}".format(q,waitingTime)

        ## get Waiting time
        waitingTime[q] = getWaitingTime(waitingTime[q],blockingTime,higherPriority,\
                                        sensorGroup[targetIndex].transmissionTime,q)
        
        ## get response Time
        responseTime.append(sensorGroup[targetIndex].arrivalTime + \
                waitingTime[q] - q * sensorGroup[targetIndex].deadLine + \
                          sensorGroup[targetIndex].transmissionTime)
        #print "responseTime({}) = {}".format(q,responseTime)
        
        q = q+1
    
    return max(responseTime)
    


def main():
    ### arrival time, transmission time, deadLine, weight, priority
    #a = Sensor(0.0,1.0,4.0,4,1)
    #b = Sensor(0.0,3.0,6.0,7,2)
    #c = Sensor(0.0,1.0,4.0,5,3)
    #a = Sensor(0.0,3.0,9.0,4,2)
    #b = Sensor(0.0,1.0,4.0,7,1)
    #c = Sensor(0.0,1.0,6.0,5,0)
    
    
    
    a = Sensor(851.0,120.0,2862.0,12.0,0,1)
    b = Sensor(977.0,112.0,457.0,4,2,6)
    c = Sensor(156.0,104.0,931.0,2,3,3)
    d = Sensor(210.0,120.0,509.0,10,4,4)
    e = Sensor(701.0,128.0,516.0,10,5,5)
    '''
    a = Sensor(0.2,1.08,3.0,0,4)
    b = Sensor(0.2,1.08,4.0,1,8)
    c = Sensor(0.2,0.52,4.5,2,3)
    d = Sensor(0  ,1.08,200,3,5)
    
    a = Sensor(0.0,5.0,40.0,0,6)
    b = Sensor(0.0,2.0,50.0,1,5)
    c = Sensor(0.0,1.0,9.0,2,1)
    d = Sensor(0.0,1.0,8.0,3,2)
    e = Sensor(0.0,2.0,7.0,4,3)
    f = Sensor(0.0,1.0,15.0,4,4)
    '''
    print "main"
    
    sensorGroup = [a,c,e]#,d,e,f]
    
    for x in range(0,len(sensorGroup)):
        ans = isSchedule(sensorGroup,x)
        print "{}:{}".format(x,ans)
    #target = 2
    #ans = isSchedule(sensorGroup,target)
    #print "schedule result = {}".format(ans)
    

if __name__ == '__main__':
    main()
