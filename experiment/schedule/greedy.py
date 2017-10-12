import priorityAssignment as pa
import random
from sensor import Sensor
from sensor import printAll
from sensor import printSensorAllProperty
def smallestSensorIndex(sensorGroup):
    
    smallest = 1
    tmp = 1
    
    for x in sensorGroup:
        tmp = x.transmissionTime / (x.deadLine * x.weight)
        if tmp < smallest:
            smallest = tmp
            index = sensorGroup.index(x)
    return index


def newGroup(assignedArray,selectGroup):
    new = []
    for x in assignedArray:
        new.append(x)

    for x in selectGroup:
        new.append(x)
    return new

def getSumOfWeight(sensorGroup):
    maximum = 0
    for x in sensorGroup:
        maximum = maximum + x.weight

    return maximum

def select(assignedArray,unassignedArray):

    ## unassignedArray represents set A
    ## selectGroup represents set B
    selectGroup = []
    maximum = 0
    convergenceMaximum = 0
    while unassignedArray:

        ## move smallest element from set A into set B
        smallestIndex = smallestSensorIndex(unassignedArray)
        selectGroup.append(unassignedArray[smallestIndex])
        unassignedArray.pop(smallestIndex)

        ## sensorGroup represent set B unions assignedArray
        sensorGroup = newGroup(assignedArray,selectGroup) 
        
        #printAll(sensorGroup,assignedArray,unassignedArray,selectGroup)

        
        ## when sensorGroup can't be schedule
        
        ans,saCount = pa.priorityAssignmentAlgo(sensorGroup,assignedArray,selectGroup)
        while not ans: 
        
            #print "remove new element from selectGroup and move random one \
            #from unassignedArray"
            selectGroup.pop() ## pop new tail
            if not unassignedArray:
                ## unassignedArray is empty, then reassign priority to sensorGroup 
                ## and break loop. 
                sensorGroup = newGroup(assignedArray,selectGroup)
                pa.priorityAssignmentAlgo(sensorGroup,assignedArray,selectGroup)
                #print "break"
                break
            randIndex = random.randrange(0,len(unassignedArray))
            selectGroup.append(unassignedArray[randIndex])
            unassignedArray.pop(randIndex)
            sensorGroup = newGroup(assignedArray,selectGroup)
            
            #printAll(sensorGroup,assignedArray,unassignedArray,selectGroup)
            
            
        tmp = getSumOfWeight(sensorGroup)
        maximum = max(maximum,tmp)
        #print "maximum:{}".format(maximum)
        convergenceMaximum = convergenceMaximum +1

    #print "greedy select: "
    #printSensorAllProperty(sensorGroup)
    return maximum


def main():
    
    ### arrival time, transmission time, deadLine, weight, priority, index
    a = Sensor(0,3.0,5.0,1,1,1)
    b = Sensor(0,1.0,4.0,2,2,2)
    c = Sensor(0,1.0,6.0,3,3,3)
    d = Sensor(0.0,1.0,5.0,4,4,4)
    e = Sensor(0.0,1.0,100.0,5,5,5)
    f = Sensor(0.0,1.0,100.0,6,6,6)
    
    
    
    sensorGroup = [a,b,c,d]
    assignedArray = [e,f]
    unassignedArray = [a,b,c,d]
    
    select(assignedArray,unassignedArray)



if __name__ == "__main__":
    main()
