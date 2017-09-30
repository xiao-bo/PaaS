import copy
import numpy as np
import math
import random
import priorityAssignment as pa

from exhausted import oneRound
from greedy import select

class Sensor:
    def __init__(self,arrivalTime,transmissionTime,deadLine,weight,priority,index):
        
        self.arrivalTime = arrivalTime
        self.transmissionTime = transmissionTime
        self.deadLine = deadLine
        self.weight = weight

        self.priority = priority
        self.index = index

def produceSensor(totalNumber,assignedNumber):
    sensorGroup = []
    a = Sensor(1.0,1.0,1.0,1,1,1)
    for x in range(0,totalNumber):
        sensorGroup.append(copy.deepcopy(a))
   
    #pa.printSensorPriority(sensorGroup)
    #a.priority = 2
    #pa.printSensorPriority(sensorGroup)

    return produceUniformData(sensorGroup,sensorGroup[:assignedNumber],sensorGroup[assignedNumber:])
    
def produceUniformData(sensorGroup,assignedArray,unassignedArray):

    ## initial property of sensorGroup
    index = 1
    for x in sensorGroup:

        x.transmissionTime = 64 + 8 * math.ceil(np.random.uniform(0,8,1))
        x.deadLine = x.transmissionTime + 128 + math.ceil(np.random.uniform(0,100,1))
        x.weight = math.ceil(np.random.uniform(0,20,1))
        x.arrivalTime = math.ceil(np.random.uniform(0,1000,1))
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

    #pa.printSensorAllProperty(sensorGroup)
   
    return sensorGroup


def main():
    
    ### arrival time, transmission time, deadLine, weight, priority, index


    totalNumber = 10
    assignedNumber = 0
    diffArray = []

    filename = "1.txt" 
    fo = open(filename,"w")
    selectArray = []
    exhaustedArray = []
    for x in range(0,100):
        sensorGroup = produceSensor(totalNumber,assignedNumber)
        #pa.printSensorPriority(sensorGroup)

        print "???????????????????"
        maximumSelect = select(sensorGroup[:assignedNumber],sensorGroup[assignedNumber:])
        selectArray.append(maximumSelect)
        print "???????????????????"
        
        maximumExhausted = oneRound(sensorGroup[:assignedNumber],sensorGroup[assignedNumber:])
        exhaustedArray.append(maximumExhausted)

        diff = maximumExhausted - maximumSelect
        diffArray.append(diff)
        print "x = {}".format(x)
        del sensorGroup

    print selectArray
    print "=="
    print exhaustedArray
    print "=="
    print diffArray

    fo.write("select = "+str(selectArray)+"\n")
    fo.write("exhausted = "+str(exhaustedArray)+"\n")
    fo.write("diff = "+str(diffArray))
if __name__ == "__main__":
    main()
