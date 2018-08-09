from sensor import Sensor
from sensor import printSensorAllProperty
import priorityAssignment as pa


def getMaxWeightOfSensorIndex(sensorGroup):
    
    maxWeight = 0
    tmp = 1
    
    for x in sensorGroup:
        tmp = x.weight
        if tmp > maxWeight:
            maxWeight = tmp
            index = sensorGroup.index(x)

    
    return index

def newGroup(assignedArray,selectGroup):
    new = []
    for x in assignedArray:
        new.append(x)

    for x in selectGroup:
        new.append(x)
    return new

def selectMaximalSet(assignedArray,unassignedArray):
    sensorGroup = []

    ## for i =1 to |S|:
    for i in range(len(unassignedArray)):
        
        ## get maximum weight of unassignedArray
        maxWeightIndex = getMaxWeightOfSensorIndex(unassignedArray)
        #print "max:"+str(maxWeightIndex)
        
        ## copy sensor with maximum weight from unassignedArray into selectGroup
        sensorGroup.append(unassignedArray[maxWeightIndex])
        
        ## remove sensor with maximum weight from unassignedArray
        unassignedArray.pop(maxWeightIndex)

        
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
    return sensorGroup

