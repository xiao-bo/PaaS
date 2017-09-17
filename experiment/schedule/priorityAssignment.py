import SchedulabilityAnalysis as sa


class Sensor:
    def __init__(self,arrivalTime,transmissionTime,deadLine,weight,priority = 0):
        self.arrivalTime = arrivalTime
        self.transmissionTime = transmissionTime
        self.deadLine = deadLine
        self.weight = weight

        self.priority = priority

def priorityAssignmentAlgo():

    ### arrival time, transmission time, deadLine, weight, priority
    a = Sensor(0.0,1.0,3.0,4,1)
    b = Sensor(0.0,2.0,4.0,7,2)
    c = Sensor(0.0,1.0,10.0,5,3)
    sensorGroup = [a,b,c]
    while True:
        if sa.isSchedule(sensorGroup,1):
            break

def main():
    
    ### arrival time, transmission time, deadLine, weight, priority
    a = Sensor(0.0,1.0,3.0,4,1)
    b = Sensor(0.0,2.0,4.0,7,2)
    c = Sensor(0.0,1.0,10.0,5,3)
    #a = Sensor(0.0,1.0,2.5,4,1)
    #b = Sensor(0.0,1.0,3.5,7,2)
    #c = Sensor(0.0,1.0,3.5,5,3)
    print "main"
    
    sensorGroup = [a,b,c]
    sa.isSchedule(sensorGroup,1)

if __name__ == "__main__":
    main()
