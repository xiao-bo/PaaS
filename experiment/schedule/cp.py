from sensor import Sensor
from sensor import printSensorAllProperty
import priorityAssignment as pa


def getSmallCP(sensorGroup):
    
    smallCP = 1.0
    tmp = 1.0
    
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


def main():


    ### arrival time, transmission time, deadLine, weight, priority, index
    a = Sensor(0.0,1.0,8.0,2,1,1)
    b = Sensor(0.0,1.0,4.0,4,2,2)
    c = Sensor(0.0,1.0,8.0,3,3,3)
    #a=Sensor(200000,400.0,1000000,19.0,1,2)
    #b=Sensor(300000,400.0,10000,17.0,2,1)
    #c=Sensor(100000,440.0,100000,17.0,4,4)
    e = Sensor(0.0,1.0,100.0,5,5,5)
    f = Sensor(0.0,1.0,100.0,6,6,6)
    
    #sensorGroup = [a,b,c,d]
    assignedArray = []
    
    unassignedArray = [a,b,c]
    sensorGroup=[a,b,c]
    #print getSmallCP(sensorGroup)

    selectCPSet(assignedArray,unassignedArray)

if __name__ == "__main__":
    main()
