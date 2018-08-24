import SchedulabilityAnalysis as sa
import time
from sensor import Sensor
from sensor import printSensorPriority
from sensor import printSensorAllProperty

def search(sensorGroup,priority):
    for x in sensorGroup:
        if x.priority == priority:
            index = sensorGroup.index(x)
            return index

def finialTest(sensorGroup):
    saCount = 0 
    count = 0
    for x in sensorGroup:
        if x.priority == 0:
            count = count +1
    if count >1:
        return False,saCount
    for x in range(0,len(sensorGroup)):
        if sa.isSchedule(sensorGroup,x):
            saCount = saCount +1
            continue
        else:
            return False,saCount
        
    return True,saCount

def initialSensor(sensorGroup,assignedArray,unassignedArray):
    for x in range(0,len(sensorGroup)):
        if sensorGroup[x] in assignedArray:
            #print "sensor[{}] in assignedArray".format(x)
            continue
        sensorGroup[x].priority = 0
def nestedLoop(sensorGroup,currentPriority,assignedPriority):
    
    if currentPriority in assignedPriority:
        return "continue"
    else:
               
        for target in sensorGroup:
            tmp = True
            #print "sensorGroup"
            #printSensorPriority(sensorGroup)           
            #print "target.priority={} weight={} index={}".format(target.priority,target.weight,target.index)
            #print "current priority={}".format(currentPriority)
            if target.priority == 0:
                target.priority = currentPriority
            else:
                #print "target have priority"
                continue
            
            index = sensorGroup.index(target)

            ## check schedule.
            if sa.isSchedule(sensorGroup,index):
                #print "target index:{} can schedule at priority {}  and jump".format(target.index,currentPriority)
                ## jump to outer loop
                return "continue"

            else:
                #print "target index:{} can't schedule at priority {}".format(target.index,currentPriority)
                ## to avoid duplicate priority in sensor
                target.priority = 0
        #print "can't schedulable"
        return "no"
    
def priorityAssignmentAlgo(sensorGroup,assignedArray,unassignedArray):

    #########
    
    initialSensor(sensorGroup,assignedArray,unassignedArray)
    
    ## note unassigned sensor index
    
    assignedPriority = [x.priority for x in assignedArray]
    if assignedPriority:
        currentPriority = max(assignedPriority)+len(unassignedArray)
    else:
        currentPriority = len(unassignedArray)
    finialPriority = []
    saCount = 0
    #print currentPriority
    
    ## lowest priority first be assigned
    #count = 0
    
    while currentPriority >=1: 
        ans = nestedLoop(sensorGroup,currentPriority,assignedPriority)    
        #printSensorAllProperty(sensorGroup)
        currentPriority = currentPriority-1
        if ans == 'no':
            #print "break"
            break
        #print "currentPriority:{}".format(currentPriority)

    #print ans
    #printSensorPriority(sensorGroup)
    ans, finialCount = finialTest(sensorGroup)
    saCount = saCount+finialCount
    return ans,saCount
