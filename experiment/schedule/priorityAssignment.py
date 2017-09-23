import SchedulabilityAnalysis as sa


class Sensor:
    def __init__(self,arrivalTime,transmissionTime,deadLine,weight,priority = 0):
        self.arrivalTime = arrivalTime
        self.transmissionTime = transmissionTime
        self.deadLine = deadLine
        self.weight = weight

        self.priority = priority

def printSensor(sensorGroup):
    for x in range(0,len(sensorGroup)):
        print "sensor[{}].priority = {}".format(x,sensorGroup[x].priority)
    
def search(sensorGroup,priority):
    for x in sensorGroup:
        if x.priority == priority:
            index = sensorGroup.index(x)
            return index
def finialTest(sensorGroup):
    for x in range(0,len(sensorGroup)):
        if sa.isSchedule(sensorGroup,x):
            continue
        else:
            return False
        
    return True

def initialSensor(sensorGroup,assignedArray,unassignedArray):
    for x in range(0,len(sensorGroup)):
        if sensorGroup[x] in assignedArray:
            print "sensor[{}] in assignedArray".format(x)
            continue
        sensorGroup[x].priority = 0



def priorityAssignmentAlgo(sensorGroup,assignedArray,unassignedArray):



    #########
    
    initialSensor(sensorGroup,assignedArray,unassignedArray)
    
    ## note unassigned sensor index

    
    assignedPriority = [x.priority for x in assignedArray]
    currentPriority = len(sensorGroup)-1

    print "==="
    for x in range(0,10):
        if x in assignedPriority:
            print x
    print currentPriority

    
    
    ## lowest priority first be assigned
    count = 0
    
    while currentPriority >= 0 :
       
        print "currentPriority:{}".format(currentPriority)

        ## check currentPriority is assigned 
        if currentPriority in assignedPriority:
            index = search(sensorGroup,currentPriority)
            ## check sensor is schedule?
            count = count +1
            if sa.isSchedule(sensorGroup,index):
                print "sensor[{}] can schedule at priority {}".format(index,currentPriority)
                currentPriority = currentPriority -1
                continue
            else:
                print "sensor[{}] can't be schedule at priority {}".format(index,currentPriority)
                return False
        else:
                   
            for target in sensorGroup:
                print "sensorGroup"
                printSensor(sensorGroup)           
                print "target.priority={} weight={}".format(target.priority,target.weight)
                print "current priority={}".format(currentPriority)
                count = count +1
                if target.priority == 0:
                    target.priority = currentPriority
                else:
                    print ""
                    continue
                
                index = sensorGroup.index(target)

                ## check schedule.
                if sa.isSchedule(sensorGroup,index):
                    print "target index:{} can schedule at priority {}  and jump".format(index,currentPriority)
                    
                    break
                else:
                    print "target index:{} can't schedule at priority {}".format(index,currentPriority)
                    ## to avoid duplicate priority in sensor
                    target.priority = 0
                
            
            else:
                print "count = {}".format(count)
                return finialTest(sensorGroup)
                
            currentPriority = currentPriority - 1
    
    print "count = {}".format(count)
    printSensor(sensorGroup)
    return True

def main():
    
    ### arrival time, transmission time, deadLine, weight, priority
    '''
    a = Sensor(0.0,3.0,6.0,7,0)
    b = Sensor(0.0,1.0,4.0,4,1)
    c = Sensor(0.0,1.0,4.0,5,2)
    '''
    a = Sensor(0.0,1.0,5.0,0,2)
    b = Sensor(0.0,2.0,6.0,1,1)
    c = Sensor(0.0,1.0,50.0,2,2)
    d = Sensor(0.0,1.0,100.0,3,5)
    e = Sensor(0.0,1.0,100.0,4,4)
    print "main"
    
    sensorGroup = [a,b,c,d,e]
    assignedArray = [c,d]
    unassignedArray = [a,b,e]
    if priorityAssignmentAlgo(sensorGroup,assignedArray,unassignedArray):
        print "==== sensorGroup can be schedulable"
    else:
        print "====can't be schedulable"

if __name__ == "__main__":
    main()
