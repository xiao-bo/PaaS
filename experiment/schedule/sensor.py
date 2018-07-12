
class Sensor:
    def __init__(self,kind,arrivalTime,transmissionTime,deadLine,weight,priority,index):
        
        self.arrivalTime = arrivalTime
        self.transmissionTime = transmissionTime
        self.deadLine = deadLine
        self.weight = weight

        self.priority = priority
        self.index = index
        self.kind = kind

def printSensorPriority(sensorGroup):
    for x in range(0,len(sensorGroup)):
        print "s[{}].p = {}, index ={}, weight = {}".format(x,sensorGroup[x].priority, sensorGroup[x].index,sensorGroup[x].weight)

def printSensorAllProperty(sensorGroup):

    for x in range(0,len(sensorGroup)):
        
        print "sensor[{}] kind = {} arrival time = {}, transmission = {}, deadLine ={} \n weight = {}, priority = {}, index ={}".format(x,\
            sensorGroup[x].kind,sensorGroup[x].arrivalTime, sensorGroup[x].transmissionTime, \
            sensorGroup[x].deadLine,sensorGroup[x].weight,sensorGroup[x].priority,\
             sensorGroup[x].index)


def printAll(sensorGroup,assignedArray,unassignedArray,selectGroup):
    
    print "sensorGroup:"
    for x in range(0,len(sensorGroup)):
        print "sensorGroup[{}].priority ={} , index = {}".format(x,sensorGroup[x].priority,sensorGroup[x].index)
    
    print "assignedArray"
    for x in range(0,len(assignedArray)):
        print "assignedArray[{}].priority = {}, index = {}".format(x,assignedArray[x].priority,assignedArray[x].index)

    print "unassignedArray"
    for x in range(0,len(unassignedArray)):
        print "unassignedArray[{}].priority = {}, index = {}".format(x,unassignedArray[x].priority,unassignedArray[x].index)

    print "selectGroup"
    for x in range(0,len(selectGroup)):
        print "selectGroup[{}].priority = {}, index = {}".format(x,selectGroup[x].priority,selectGroup[x].index)

def writeSensorData(sensorGroup,fo,count):
    #fo = open(filename,'w')
    for x in range(0,len(sensorGroup)):
        ans = ":sensor["+str(x)+"] kind :"+str(sensorGroup[x].kind)+":arrival time:"\
            +str(sensorGroup[x].arrivalTime)+":transmission:"+str(sensorGroup[x].transmissionTime)\
            +":deadLine:"+str(sensorGroup[x].deadLine)+":weight:"+str(sensorGroup[x].weight)\
            +":priority:"+str(sensorGroup[x].priority)+":index:"+str(sensorGroup[x].index)
        fo.write("count:"+str(count)+ans+"\n")

def readSensorData():
    print ""

def main():
    
    ### kind,arrival time, transmission time, deadLine, weight, priority, index,
    ### kind = 0 represent temperature sensor, kind = 1 represents pressure sensor
    ### kind = 2 represent distance sensor.
    a = Sensor(1,0,3.0,5.0,1,1,1)
    b = Sensor(0,0,1.0,4.0,2,2,2)
    c = Sensor(1,0,1.0,6.0,3,3,3)
    d = Sensor(2,0.0,1.0,5.0,4,4,4)
    e = Sensor(1,0.0,1.0,100.0,5,5,5)
    f = Sensor(2,0.0,1.0,100.0,6,6,6)
    sensorGroup = [a,b,c,d]
    assignedArray = [e,f]
    unassignedArray = [a,b,c,d]
    
if __name__ == "__main__":
    main()
