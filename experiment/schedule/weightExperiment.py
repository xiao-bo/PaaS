import copy
import math
import numpy as np
import random
from operator import attrgetter
from sensor import Sensor
from sensor import printSensorAllProperty
from sensor import printSensorPriority
from optimal import selectOptimalSet
from cp import selectCPSet

def produceSensor(totalNumber,assignedNumber):
    sensorGroup = []
    a = Sensor(1.0,1.0,1.0,1,1,1)
    for x in range(0,totalNumber):
        sensorGroup.append(copy.deepcopy(a))
   
    #printSensorPriority(sensorGroup)

    return produceUniformData(sensorGroup,sensorGroup[:assignedNumber],sensorGroup[assignedNumber:])
    
def produceUniformData(sensorGroup,assignedArray,unassignedArray):
    deadLine = [10000,50000,100000,200000,1000000]
    arrivalTime = [100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]
    length = len(sensorGroup)
    weight = random.sample(xrange(1,length+1),length)
    
    ## initial property of sensorGroup
    index = 1
    for x in sensorGroup:

        x.transmissionTime = 5*(64 + 8 * math.ceil(np.random.uniform(0,3,1)))
        x.deadLine = random.choice(deadLine)
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

def utility(sensorGroup):
    sumWeight = 0.0
    p = len(sensorGroup)
    
    for x in sensorGroup:
        sumWeight = sumWeight + math.pow(100,x.weight)* x.weight
        p = p-1
    sumWeight = sumWeight/math.pow(100,sensorGroup[0].weight)
    return sumWeight

def test():
    sumWeight = 0
    
    weight = [15,14,13,12,11,9,8,7,6,5,4,3]
    for x in weight:
        sumWeight = sumWeight + math.pow(100,12)* x
    print sumWeight

def main():
    
    ### arrival time, transmission time, deadLine, weight, priority, index

    totalNumber = 35
    assignedNumber = 0
    diffArray = []

    filename = "1.txt" 
    fo = open(filename,"w")
    
    fo.write("number sensor :"+str(totalNumber)+"\n")
    
    for x in range(0,10):
        sensorGroup = produceSensor(totalNumber,assignedNumber)
       
        
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
   
        
        #print "=="
        sumWeightofOptimalSet = utility(optimalSet)
        #print "optimal weight :" + str(sumWeightofOptimalSet)
        sumWeightofCPSet = utility(CPSet)
        #print "CP weight :" + str(sumWeightofCPSet)
        #print "diff:" + str(sumWeightofOptimalSet-sumWeightofCPSet)
        '''
        if (sumWeightofOptimalSet-sumWeightofCPSet)<0:
            print "get optimal"
            printSensorAllProperty(optimalSet)
            print "optimal weight :" + str(sumWeightofOptimalSet)
            print "get cp"
            printSensorAllProperty(CPSet)
            print "CP weight :" + str(sumWeightofCPSet)
            print "diff:" + str(sumWeightofOptimalSet-sumWeightofCPSet)
        '''
        fo.write("optimalSet weight : "+str(sumWeightofOptimalSet)+":CP weight : "+
            str(sumWeightofCPSet)+":diff:"+str(sumWeightofOptimalSet-sumWeightofCPSet)+"\n")
        
    



if __name__ == "__main__":
    main()
