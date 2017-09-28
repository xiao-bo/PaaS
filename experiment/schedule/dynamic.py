import priorityAssignment as pa
from greedy import newGroup


class Sensor:
    def __init__(self,arrivalTime,transmissionTime,deadLine,weight,priority,index):
        
        self.arrivalTime = arrivalTime
        self.transmissionTime = transmissionTime
        self.deadLine = deadLine
        self.weight = weight

        self.priority = priority
        self.index = index
        
def dynamicProgram(assignedArray,unassignedArray):
    #new
    #for x in range(0,)
    return True
def main():
    
    ### arrival time, transmission time, deadLine, weight, priority, index
    a = Sensor(0,3.0,5.0,3,1,1)
    b = Sensor(0,1.0,4.0,4,2,2)
    c = Sensor(0,1.0,6.0,2,3,3)
    d = Sensor(0.0,1.0,2.0,10,4,4)
    e = Sensor(0.0,1.0,100.0,10,5,5)
    
    
    
    sensorGroup = [a,b,c,d]
    assignedArray = [b]
    unassignedArray = [a,c,d]
    
    z = newGroup(assignedArray,unassignedArray)
    pa.printSensor(z)

    #dynamicProgram(assignedArray,unassignedArray)



if __name__ == "__main__":
    main()
