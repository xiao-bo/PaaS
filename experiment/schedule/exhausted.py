import priorityAssignment as pa
import SchedulabilityAnalysis as sa
import copy
from greedy import newGroup, getSumOfWeight
import time


class Sensor:
    def __init__(self,arrivalTime,transmissionTime,deadLine,weight,priority,index):
        
        self.arrivalTime = arrivalTime
        self.transmissionTime = transmissionTime
        self.deadLine = deadLine
        self.weight = weight

        self.priority = priority
        self.index = index

def exhaustedProgram(maximum,target,assignedArray,unassignedArray,maxGroup,count):
    
    for i in range(len(unassignedArray)):
        newTarget = copy.copy(target)
        
        newTarget.append(unassignedArray[i])
        new = newGroup(assignedArray,newTarget)
        if pa.priorityAssignmentAlgo(new,assignedArray,newTarget):
     
            #pa.printSensorPriority(new)
            #print "==="
 
            tmp,maxGroup,count = exhaustedProgram(maximum, newTarget,assignedArray,unassignedArray[i+1:],maxGroup,count)
            if tmp > getSumOfWeight(newTarget):
                maximum = tmp

            else:
                maximum = getSumOfWeight(newTarget)
                maxGroup = newTarget
    if not unassignedArray:
        count = count +1
    return maximum,maxGroup,count
        

def oneRound(assignedArray,unassignedArray):
    maximum = 0
    
    now = time.time()
    #print now
    maximum,maxGroup,count = exhaustedProgram(maximum,[],assignedArray,unassignedArray,[],0)
    now = time.time()
    #print now
    print "count={}".format(count)

    total = newGroup(assignedArray,maxGroup)
    maximum = getSumOfWeight(total)
    #print maximum
    #print "finial run==========~~~"
    pa.priorityAssignmentAlgo(total,assignedArray,maxGroup)
    #pa.printSensorPriority(total)
    return maximum
def main():
    
    ### arrival time, transmission time, deadLine, weight, priority, index
    a = Sensor(0.0,3.0,5.0,1,1,1)
    b = Sensor(0.0,1.0,4.0,2,2,2)
    c = Sensor(0.0,1.0,6.0,3,3,3)
    d = Sensor(0.0,1.0,5.0,4,4,4)
    e = Sensor(0.0,1.0,100.0,5,5,5)
    f = Sensor(0.0,1.0,100.0,6,6,6)
   
    assignedArray = [e,f]
    unassignedArray = [a,b,c,d]
      
    oneRound(assignedArray,unassignedArray)

if __name__ == "__main__":
    main()
