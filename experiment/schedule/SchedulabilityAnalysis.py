import math

class Sensor:
    def __init__(self,arrivalTime,transmissionTime,deadLine,weight,priority = 0):
        self.arrivalTime = arrivalTime
        self.transmissionTime = transmissionTime
        self.deadLine = deadLine
        self.weight = weight

        self.priority = priority


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

    if utilijation > 1:
        print "no schedule"
        return False
    

    #print "target = {}".format(target)
    responseTime = getResponseTime(sensorGroup,target)
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
    if lowerPriority: 
        ## get maximum priority in lower priority
        maxlp = min(lowerPriority)  
        ## search priority maxlp in sensorGroup
        for i in range(0,length): 
            if maxlp == sensorGroup[i].priority:
                blockingTime = sensorGroup[i].transmissionTime
                break

    
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
    a = Sensor(0.0,3.0,20.0,4,0)
    b = Sensor(0.0,2.0,5.0,7,1)
    c = Sensor(0.0,2.0,9.0,5,2)
    print "main"
    
    sensorGroup = [a,b,c]
    
    target = 1
    ans = isSchedule(sensorGroup,target)
    print "schedule result = {}".format(ans)
    

if __name__ == '__main__':
    main()
