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

    print "hyperperiod = {}".format(hyperperiod)
    return hyperperiod

def isSchedule(sensorGroup,target):
    length = len(sensorGroup)
    '''
    utilijation = 0.0
    for x in range(0,length):
        utilijation = utilijation + sensorGroup[x].transmissionTime \
            /sensorGroup[x].deadLine

    if utilijation > 1:
        print "no schedule"
        return False
    '''

    print "target = {}".format(target)
    responseTime = getResponseTime(sensorGroup,target)
    if responseTime <= sensorGroup[target].deadLine+sensorGroup[target].arrivalTime:
        return True
    else:
        return False
    
    '''

    for target in range(0,length):
        responseTime = getResponseTime(sensorGroup,target)
        if responseTime <= sensorGroup[target].deadLine+sensorGroup[target].arrivalTime:
            continue
        else:
            return False
    return True
    '''
def getWaitingTime(waitingTime,blockingTime,higherPriority,transmissionTime,q):
    index = 1

    while True:
        tmp = waitingTime
        higherTime = 0 
        for x in range(0,len(higherPriority)):
            higherTime = higherTime + math.ceil(\
                (waitingTime + higherPriority[x].arrivalTime+0.01)/higherPriority[x].deadLine)\
                *higherPriority[x].transmissionTime
        higherTime = higherTime + q * transmissionTime
        waitingTime = blockingTime + higherTime
        
        print "wait^{} ({}) = {}".format(index,q,waitingTime)
        if waitingTime == tmp:
            break
        index = index +1 
    return waitingTime
    
def getQm():
    Qm = 0
    #tm = blockingTime
    #gettm(tm,blockingTime)
    return Qm

def gettm(tm,blockingTime,higherPriority,target):
    index = 1
    #tm = 0
    while True:
        tmp = tm
        higherTime = 0 
        for x in range(0,len(higherPriority)):
            higherTime = higherTime + math.ceil(\
                (tm + higherPriority[x].arrivalTime)/higherPriority[x].deadLine)\
                *higherPriority[x].transmissionTime
        higherTime = higherTime + math.ceil(\
                (tm + target.arrivalTime)/target.deadLine)*target.transmissionTime
                
        tm = blockingTime + higherTime
        
        print "tm^{} = {}".format(index,tm)
        if tm == tmp:
            break
        index = index +1 
    return tm

def getResponseTime(sensorGroup,index):
    
    length = len(sensorGroup)
    lowerPriority = []
    higherPriority = []
    maxlp = 0  
    blockingTime = 0
    waitingTime = []
    responseTime = []
    ## get lowerPriority list
    for x in range(0,length):
        if x ==index:
            continue
        if sensorGroup[x].priority > sensorGroup[index].priority:
            lowerPriority.append(sensorGroup[x].priority)
        elif sensorGroup[x].priority < sensorGroup[index].priority:
            higherPriority.append(sensorGroup[x])
    
    
    ## lowerPrioirty is not empty. in other word, 
    ## there have lower priority object in sensorGroup
    if lowerPriority: 
        ## get maximum priority in lower priority
        maxlp = min(lowerPriority)  
        ## search priority maxlp in sensorGroup
        for x in range(0,length): 
            if maxlp == sensorGroup[x].priority:
                blockingTime = sensorGroup[x].transmissionTime
                break

    
    print "blockingTime = {}".format(blockingTime)
    hyperperiod = getHyperperiod(sensorGroup) 
    #Qm = hyperperiod / sensorGroup[index].deadLine  ## get target multiple instance
    tm = sensorGroup[index].transmissionTime
    tm = gettm(tm,blockingTime,higherPriority,sensorGroup[index])
    Qm = math.ceil((tm+sensorGroup[index].arrivalTime)/sensorGroup[x].deadLine)
    print "Qm={}".format(Qm)
    print "tm={}".format(tm)
    #Qm = 2

    
    q = 0
    while q< Qm:
        if q == 0:
            waitingTime.append(blockingTime)
            print "blockingTime = {}".format(blockingTime)
            
        elif q > 0:
            waitingTime.append(waitingTime[q-1] + sensorGroup[index].transmissionTime)
            print "waitingTime({}) = {}".format(q,waitingTime)
        waitingTime[q] = getWaitingTime(waitingTime[q],blockingTime,higherPriority,\
                                        sensorGroup[index].transmissionTime,q)
        
        responseTime.append(sensorGroup[index].arrivalTime + \
                waitingTime[q] - q * sensorGroup[index].deadLine + \
                          sensorGroup[index].transmissionTime)
        print "responseTime({}) = {}".format(q,responseTime)
        
        q = q+1
    
    return max(responseTime)
    
    #print "true"


def main():
    ### arrival time, transmission time, deadLine, weight, priority
    a = Sensor(0.0,1.0,3.0,4,1)
    b = Sensor(0.0,2.0,4.0,7,2)
    c = Sensor(0.0,1.0,10.0,5,3)
    #a = Sensor(0.0,1.0,2.5,4,1)
    #b = Sensor(0.0,1.0,3.5,7,2)
    #c = Sensor(0.0,1.0,3.5,5,3)
    print "main"
    
    sensorGroup = [a,b,c]
    
    target = 0
    ans = isSchedule(sensorGroup,target)
    print "schedule result = {}".format(ans)
    

if __name__ == '__main__':
    main()
