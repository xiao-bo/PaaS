import priorityAssignment as pa
import random

class Sensor:
    def __init__(self,arrivalTime,transmissionTime,deadLine,weight,priority,index):
        
        self.arrivalTime = arrivalTime
        self.transmissionTime = transmissionTime
        self.deadLine = deadLine
        self.weight = weight

        self.priority = priority
        self.index = index

def smallestSensorIndex(sensorGroup):
    
    smallest = 1
    tmp = 1
    
    for x in sensorGroup:
        tmp = x.transmissionTime / (x.deadLine * x.weight)
        if tmp < smallest:
            smallest = tmp
            index = sensorGroup.index(x)
    return index


def printSensor(sensorGroup):
    for x in range(0,len(sensorGroup)):
        print "sensor[{}].priority = {}, index = {}".format(x,sensorGroup[x].priority,sensorGroup[x].index)
    
def printAll(sensorGroup,assignedArray,unassignedArray,selectGroup):
    
    print "sensorGroup:"
    for x in range(0,len(sensorGroup)):
        print "sensorGroup[{}].priority ={} , index = {}".format(x,sensorGroup[x].priority,sensorGroup[x].index)
    
    print "assignedArray"
    for x in range(0,len(assignedArray)):
        print "assignedArray[{}].priority = {}, index = {}".format(x,assignedArray[x].priority,assignedArray[x].index)

    print "unassignedArray"
    for x in range(0,len(unassignedArray)):
        print "unassignedArray[{}].priority = {}, index = {}".format(x,unassignedArray[x].priority,unassignedArray[x].index)

    print "selectGroup"
    for x in range(0,len(selectGroup)):
        print "selectGroup[{}].priority = {}, index = {}".format(x,selectGroup[x].priority,selectGroup[x].index)

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
        index = smallestSensorIndex(unassignedArray)
        selectGroup.append(unassignedArray[index])
        unassignedArray.pop(index)

        ## sensorGroup represent set B unions assignedArray
        sensorGroup = newGroup(assignedArray,selectGroup) 
        
        printAll(sensorGroup,assignedArray,unassignedArray,selectGroup)

        
        ## when sensorGroup can't be schedule 
        while not pa.priorityAssignmentAlgo(sensorGroup,assignedArray,selectGroup):        
        
            print "remove new element from selectGroup and move random one \
            from unassignedArray"
            selectGroup.pop() ## pop new tail
            if not unassignedArray:
                ## unassignedArray is empty, then reassign priority to sensorGroup 
                ## and break loop. 
                sensorGroup = newGroup(assignedArray,selectGroup)
                pa.priorityAssignmentAlgo(sensorGroup,assignedArray,selectGroup)
                print "break"
                break
            randIndex = random.randrange(0,len(unassignedArray))
            selectGroup.append(unassignedArray[randIndex])
            unassignedArray.pop(randIndex)
            sensorGroup = newGroup(assignedArray,selectGroup)
            
            printAll(sensorGroup,assignedArray,unassignedArray,selectGroup)
            
            
        tmp = getSumOfWeight(sensorGroup)
        maximum = max(maximum,tmp)
        print "maximum:{}".format(maximum)
        convergenceMaximum = convergenceMaximum +1
        printSensor(sensorGroup)

def main():
    
    ### arrival time, transmission time, deadLine, weight, priority, index
    a = Sensor(0,3.0,5.0,3,1,1)
    b = Sensor(0,1.0,4.0,4,2,2)
    c = Sensor(0,1.0,6.0,2,3,3)
    d = Sensor(0.0,1.0,2.0,10,4,4)
    e = Sensor(0.0,1.0,100.0,10,5,5)
    
    
    
    sensorGroup = [a,b,c,d]
    assignedArray = []
    unassignedArray = [a,c,d]
    
    select(assignedArray,unassignedArray)



if __name__ == "__main__":
    main()
