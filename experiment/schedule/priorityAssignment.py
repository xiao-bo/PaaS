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
    
def swapPriority(a,b):
    tmp = a.priority 
    a.priority = b.priority
    b.priority = tmp

def initialSensor(sensorGroup):
    for x in range(0,len(sensorGroup)):
        sensorGroup[x].priority = x

def priorityAssignmentAlgo(sensorGroup):



    target = len(sensorGroup) - 1
    
    initialSensor(sensorGroup)
    ## note unassigned sensor index
    unassignArray = [x for x in range(target,-1,-1)]
    priorityLevel = [x.priority for x in sensorGroup]
    currentPriority = max(priorityLevel)
    print currentPriority
    '''
    while currentPriority >=0:
        print "currentPriority:{}".format(currentPriority)
        for x in range(0,5):
            print "x:{}".format(x)
            if x%2==0:
                print "break"
                break
            
        print "can't schedule"
            
        currentPriority = currentPriority -1
    '''
    ## lowest priority first be assigned
    while currentPriority >= 0 :
        print "currentPriority:{}".format(currentPriority)
        for target in unassignArray:
        
            #print "unassignArray:{} and target {}".format(unassignArray,target)

            ## assign priority to target
            sensorGroup[target].priority = currentPriority

            ## check schedule.
            if sa.isSchedule(sensorGroup,target):
                print "target:{} can schedule at priority {}  and jump".format(target,currentPriority)
                
                ## remove assign message from unassigned sensor
                unassignArray.remove(target)
                break
            else:
                print "target:{} can't schedule at priority {}".format(target,currentPriority)
            
            ## to avoid duplicate priority in sensor
            swapPriority(sensorGroup[target],sensorGroup[target-1])
        
        else:
            #print "sensor group can't be schedulable"
            return False
        currentPriority = currentPriority - 1
    

    printSensor(sensorGroup)
    return True

def main():
    
    ### arrival time, transmission time, deadLine, weight, priority
    '''
    a = Sensor(0.0,3.0,6.0,7,0)
    b = Sensor(0.0,1.0,4.0,4,1)
    c = Sensor(0.0,1.0,4.0,5,2)
    '''
    a = Sensor(0.0,5.0,20.0,4,3)
    b = Sensor(0.0,2.0,5.0,7,2)
    c = Sensor(0.0,2.0,9.0,5,4)

    print "main"
    
    sensorGroup = [a,b,c]
    
    if priorityAssignmentAlgo(sensorGroup):
        print "==== sensorGroup can be schedulable"
    else:
        print "====can't be schedulable"

if __name__ == "__main__":
    main()
