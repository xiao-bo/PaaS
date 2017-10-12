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
    count = 0
    
    while currentPriority >= 0 :
       
        #print "currentPriority:{}".format(currentPriority)

        ## check currentPriority is assigned 
        if currentPriority in assignedPriority:
            currentPriority = currentPriority -1
            continue
        else:
                   
            for target in sensorGroup:
                #print "sensorGroup"
                #printSensorPriority(sensorGroup)           
                #print "target.priority={} weight={}".format(target.priority,target.weight)
                #print "current priority={}".format(currentPriority)
                count = count +1
                if target.priority == 0:
                    target.priority = currentPriority
                else:
                    #print ""
                    continue
                
                index = sensorGroup.index(target)

                ## check schedule.
                saCount = saCount +1
                if sa.isSchedule(sensorGroup,index):
                    #print "target index:{} can schedule at priority {}  and jump".format(index,currentPriority)
                    
                    break
                else:
                    #print "target index:{} can't schedule at priority {}".format(index,currentPriority)
                    ## to avoid duplicate priority in sensor
                    target.priority = 0
                
            
            currentPriority = currentPriority - 1
    
    #printSensorPriority(sensorGroup)
    ans, finialCount = finialTest(sensorGroup)
    saCount = saCount+finialCount
    return ans,saCount

def main():
    
    ### arrival time, transmission time, deadLine, weight, priority, index
    a = Sensor(851.0,120.0,2862.0,12.0,1,1)
    b = Sensor(977.0,112.0,457.0,4,2,6)
    c = Sensor(156.0,104.0,931.0,2,3,3)
    d = Sensor(210.0,120.0,509.0,10,4,4)
    e = Sensor(701.0,128.0,516.0,10,5,5)
    print "main"
    
    sensorGroup = [a,b,c,d,e]
    assignedArray = []
    unassignedArray = [a,b,c,d,e]

    print time.time() 
    for x in assignedArray:
        if x.priority ==0:
            print ("please remove priority 0 in assigned Array")
            break
    else:        
        ans,saCount = priorityAssignmentAlgo(sensorGroup,assignedArray,unassignedArray)
        if ans:
            print "==== sensorGroup can be schedulable"
        else:
            print "====can't be schedulable"
    print time.time()
    printSensorPriority(sensorGroup)
if __name__ == "__main__":
    main()
