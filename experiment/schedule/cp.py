from sensor import Sensor
from sensor import printSensorAllProperty
import priorityAssignment as pa


def getSmallCP(sensorGroup):
    
    smallCP = 1.0
    tmp = 1.0
    index = 0
    for x in sensorGroup:
        tmp = x.transmissionTime/x.deadLine

        if tmp < smallCP:
            smallCP = tmp
            index = sensorGroup.index(x)
    return index

def newGroup(assignedArray,selectGroup):
    new = []
    for x in assignedArray:
        new.append(x)

    for x in selectGroup:
        new.append(x)
    return new

def selectCPSet(assignedArray,unassignedArray):
    sensorGroup = []

    ## for i =1 to |S|:
    for i in range(len(unassignedArray)):
        
        ## get minimum CP of unassignedArray
        minCPIndex = getSmallCP(unassignedArray)
        #print "min:"+str(minCPIndex)
        
        ## copy sensor with minimum CP from unassignedArray into selectGroup
        sensorGroup.append(unassignedArray[minCPIndex])
        
        ## remove sensor with minimum CP from unassignedArray
        unassignedArray.pop(minCPIndex)

        
        ## sensorGroup consists of assignedArray and selectGroup,
        ## priority of element in assignedArray is fixed
        ## priority of element in selectGroup can be reassigned.
        #print "sensorGroup"
        #printSensorAllProperty(sensorGroup)
        ans,saCount = pa.priorityAssignmentAlgo(sensorGroup,assignedArray,sensorGroup)
        #print str(ans)+"len:"+str(len(sensorGroup))
        
        ## when sensorGroup can't be schedule
        if not ans: 
            #remove new element from sensorGroup and move random one \
            #from unassignedArray
            sensorGroup.pop()
            #print "pop"
            ## reassign priority 
            ans,saCount = pa.priorityAssignmentAlgo(sensorGroup,assignedArray,sensorGroup)


    #print printSensorAllProperty(sensorGroup)
    #ans,saCount = pa.priorityAssignmentAlgo(sensorGroup,assignedArray,sensorGroup)
    return sensorGroup

