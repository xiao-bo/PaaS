import copy

import math
import numpy as np
import random
from operator import attrgetter
from sensor import Sensor
from sensor import printSensorAllProperty
from sensor import printSensorPriority
from sensor import writeSensorData
from optimal import selectOptimalSet
from cp import selectCPSet

def produceSensor(totalNumber,assignedNumber):
    sensorGroup = []
    a = Sensor(0,1.0,1.0,1.0,1,1,1)
    for x in range(0,totalNumber):
        sensorGroup.append(copy.deepcopy(a))
   
    #printSensorPriority(sensorGroup)

    return produceUniformData(sensorGroup,sensorGroup[:assignedNumber],sensorGroup[assignedNumber:])
    
def produceUniformData(sensorGroup,assignedArray,unassignedArray):
    ## time level is us
    ## temperature sensor's frequency = 20hz,10hz,8hz,4hz,2hz,1hz
    temperatureDeadline = [50000,100000,125000,250000,500000,1000000]
    ## pressure sensor's frequency 100hz,20hz,10hz,8hz,4hz,2hz,1hz
    #pressureDeadline = [10000,50000,100000,125000,250000,500000,1000000]
    ## distance sensor's frequency 100hz,20hz,10hz,8hz,4hz,2hz,1hz
    #distanceDeadline = [10000,50000,100000,125000,250000,500000,1000000]
    
    ## remove 10000 for meeting slide
    pressureDeadline = [50000,100000,125000,250000,500000,1000000]
    ## distance sensor's frequency 100hz,20hz,10hz,8hz,4hz,2hz,1hz
    distanceDeadline = [50000,100000,125000,250000,500000,1000000]
    
    deadLine = [10000,50000,100000,200000,1000000]

    arrivalTime = [100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]
    kinds = [0,1,2]
    length = len(sensorGroup)
    weight = random.sample(xrange(1,length+1),length)
    
    ## initial property of sensorGroup
    index = 1
    for x in sensorGroup:

        x.transmissionTime = 5*(64 + 8 * math.ceil(np.random.uniform(0,3,1)))
        x.kind = random.choice(kinds)
        if x.kind == 0:
            x.deadLine = random.choice(temperatureDeadline)
        elif x.kind == 1:
            x.deadLine = random.choice(pressureDeadline)
        elif x.kind == 2:
            x.deadLine = random.choice(distanceDeadline)
        x.weight = weight[index-1]
        x.arrivalTime = random.choice(arrivalTime)
        x.index = index
        index = index + 1
        

    ## initial priority of unassignedArray
    if unassignedArray:
        for x in unassignedArray:
            x.priority = 0


    ## initial priority of assignedArray 
    if assignedArray:
        priority = random.sample(xrange(1,len(assignedArray)+1),len(assignedArray))  
        i = 0

        for x in assignedArray:
            x.priority = priority[i]
            i = i + 1

    #printSensorAllProperty(sensorGroup)
   
    return sensorGroup

def deadLineToFreq(x):
    freq = 0.0
    ## 5hz = 200ms = 200000us
    ## 10hz = 100ms = 100000us
    freq = 1.0/(float(x.deadLine)/1000000.0)
    #print "hz={}".format(freq)
    return freq

def temperatureUtility(x):
    utilityValue = 0.0
    
    freq = deadLineToFreq(x)
    if freq < 5:
        utilityValue = (4.0/9.0)*freq*freq
    elif freq >= 5:
        utilityValue = 10.0

    #utilityValue = 10.0
    #print "temperature sensor utility Value = {}".format(utilityValue)
    return utilityValue

def distanceUtility(x):
    utilityValue = 0.0
    
    freq = deadLineToFreq(x)
    if freq < 2:
        utilityValue = 4.0*freq*freq
    elif freq >= 2:
        utilityValue = 5.0

    #utilityValue = 10.0
    #print "distance sensor utility Value = {}".format(utilityValue)
    return utilityValue

def pressureUtility(x):
    utilityValue = 0.0
    
    freq = deadLineToFreq(x)
    if freq < 5:
        utilityValue = (2.0/1000)*freq*freq
    elif freq >= 5:
        utilityValue = 10.0

    #utilityValue = 10.0
    #print "pressure sensor utility Value = {}".format(utilityValue)
    return utilityValue

def getSumUtility(totalGroup,sensorGroup):
    sumUtility = 0.0
    p = len(sensorGroup)
    
    for x in sensorGroup:
        if x.kind == 0:
            sumUtility = sumUtility + 2*temperatureUtility(x)*x.weight*x.weight
        elif x.kind == 1:
            sumUtility = sumUtility + 2*pressureUtility(x)*x.weight*x.weight
        elif x.kind ==2:
            sumUtility = sumUtility + 2*distanceUtility(x)*x.weight*x.weight
    for x in totalGroup:
        if x.kind == 0:
            sumUtility = sumUtility + -1*temperatureUtility(x)*x.weight*x.weight
        elif x.kind == 1:
            sumUtility = sumUtility + -1*pressureUtility(x)*x.weight*x.weight
        elif x.kind ==2:
            sumUtility = sumUtility + -1*distanceUtility(x)*x.weight*x.weight
            
    # sum (Ui*Wi*Yi) Yi = {-1,1}
    # for code, sum(Ui*Wi*Yi) Yi={0,2} + totalSum(Uj*Wj*-1) = above
    ##  i = 0 to sensorGroup (select sensor)
    ##  j = 0 to totalGroup (all sensor)
    
    return sumUtility

def test():
    sumWeight = 0
    
    weight = [15,14,13,12,11,9,8,7,6,5,4,3]
    for x in weight:
        sumWeight = sumWeight + math.pow(100,12)* x
    print sumWeight

def main():
    
    ### arrival time, transmission time, deadLine, weight, priority, index

    totalNumber = 10
    assignedNumber = 0
    diffArray = []

    filename = "1.txt" 
    fo = open(filename,"w")
    fo.write("number sensor :"+str(totalNumber)+"\n")
    dire = ""
    foptimalSet = open(dire+"optimalSet.txt","w")
    fCPSet = open(dire+"CPSet.txt",'w')
    ftotalSet = open(dire +"totalSet.txt",'w')
    for x in range(0,70000):
        sensorGroup = produceSensor(totalNumber,assignedNumber)
        print x
        
        #printSensorAllProperty(sensorGroup)
        #print "get optimal"
        
        optimalSet = selectOptimalSet(sensorGroup[:assignedNumber],sensorGroup[assignedNumber:])
        #printSensorAllProperty(optimalSet)
        #print "get cp"
        CPSet = selectCPSet(sensorGroup[:assignedNumber],sensorGroup[assignedNumber:])
        #printSensorAllProperty(CPSet)
        
        ## sort CPset by weight with descending order
        CPSet = sorted(CPSet,key=attrgetter("weight"),reverse=True)
        #print "get cp"
        #printSensorAllProperty(CPSet)
   
        
        sumUtilityofTotalSet = getSumUtility(sensorGroup,sensorGroup)
        #print "=="
        sumUtilityofOptimalSet = getSumUtility(sensorGroup,optimalSet)

        #print "optimal utility :{}".format(sumUtilityofOptimalSet)
        sumUtilityofCPSet = getSumUtility(sensorGroup,CPSet)
        #print "CP weight :{}".format(sumUtilityofCPSet)
        difference = sumUtilityofOptimalSet-sumUtilityofCPSet
        #print "difference :{}".format(difference)
        #if difference!=0:
        print "all sensor"
        #printSensorAllProperty(sensorGroup)
        writeSensorData(sensorGroup,ftotalSet,x)
        #print "get optimal"
        #printSensorAllProperty(optimalSet)
        #print "optimal utility :{}".format(sumUtilityofOptimalSet)
        writeSensorData(optimalSet,foptimalSet,x)
        #print "get cp"
        #printSensorAllProperty(CPSet)
        #print "CP weight :{}".format(sumUtilityofCPSet)
        writeSensorData(CPSet,fCPSet,x)
        #print "difference :{}".format(difference)
        #break
        fo.write("total utility:"+str(sumUtilityofTotalSet)+":optimalSet utility : "+str(sumUtilityofOptimalSet)+":CP utility : "+
            str(sumUtilityofCPSet)+":difference:"+str(difference)+"\n")
        
    


if __name__ == "__main__":
    main()
    ### kind,arrival time, transmission time, deadLine, weight, priority, index

    a = Sensor(1,0,1.0,400000.0,1,1,1)
    #temperatureUtility(a)
    #distanceUtility(a)
    #pressureUtility(a)
