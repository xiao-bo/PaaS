class Sensor:
    def __init__(self,kind,arrivalTime,transmissionTime,deadLine,weight,priority,index,origin,classes):
        
        self.arrivalTime = arrivalTime
        self.transmissionTime = transmissionTime
        self.deadLine = deadLine
        self.weight = weight

        self.priority = priority
        self.index = index
        self.kind = kind
        self.origin = origin
        self.classes = classes

def printSensorPriority(sensorGroup):
    for x in range(0,len(sensorGroup)):
        print "s[{}].p = {}, index ={}, weight = {}".format(x,sensorGroup[x].priority, sensorGroup[x].index,sensorGroup[x].weight)

def printSensorAllProperty(sensorGroup):

    for x in range(0,len(sensorGroup)):
        
        print "sensor[{}] kind = {} arrival time = {}, transmission = {}, deadLine ={} \n weight = {}, priority = {}, index ={}".format(x,\
            sensorGroup[x].kind,sensorGroup[x].arrivalTime, sensorGroup[x].transmissionTime, \
            sensorGroup[x].deadLine,sensorGroup[x].weight,sensorGroup[x].priority,\
             sensorGroup[x].index)
def deadLineToFreq(x):
    freq = 0.0
    ## 5hz = 200ms = 200000us
    ## 10hz = 100ms = 100000us
    freq = 1.0/(float(x.deadLine)/1000000.0)
    #print "hz={}".format(freq)
    return freq

def temperatureUtility(x):
    utilityValue = 0.0
    
    freq = deadLineToFreq(x)
    if freq < 5:
        utilityValue = (4.0/9.0)*freq*freq
    elif freq >= 5:
        utilityValue = 10.0

    #utilityValue = 10.0
    #print "temperature sensor utility Value = {}".format(utilityValue)
    return utilityValue

def distanceUtility(x):
    utilityValue = 0.0
    
    freq = deadLineToFreq(x)
    if freq < 2:
        utilityValue = 4.0*freq*freq
    elif freq >= 2:
        utilityValue = 5.0

    #utilityValue = 10.0
    #print "distance sensor utility Value = {}".format(utilityValue)
    return utilityValue

def pressureUtility(x):
    utilityValue = 0.0
    
    freq = deadLineToFreq(x)
    if freq < 5:
        utilityValue = (2.0/1000)*freq*freq
    elif freq >= 5:
        utilityValue = 1.0

    #utilityValue = 10.0
    #print "pressure sensor utility Value = {}".format(utilityValue)
    return utilityValue
def getSumUtility(totalGroup,sensorGroup):
    sumUtility = 0.0
    p = len(sensorGroup)
    
    for x in sensorGroup:
        if x.kind == 0:
            sumUtility = sumUtility + 2*temperatureUtility(x)*x.weight*x.weight
        elif x.kind == 1:
            sumUtility = sumUtility + 2*pressureUtility(x)*x.weight*x.weight
        elif x.kind ==2:
            sumUtility = sumUtility + 2*distanceUtility(x)*x.weight*x.weight
    for x in totalGroup:
        if x.kind == 0:
            sumUtility = sumUtility + -1*temperatureUtility(x)*x.weight*x.weight
        elif x.kind == 1:
            sumUtility = sumUtility + -1*pressureUtility(x)*x.weight*x.weight
        elif x.kind ==2:
            sumUtility = sumUtility + -1*distanceUtility(x)*x.weight*x.weight
            
    # sum (Ui*Wi*Yi) Yi = {-1,1}
    # for code, sum(Ui*Wi*Yi) Yi={0,2} + totalSum(Uj*Wj*-1) = above
    ##  i = 0 to sensorGroup (select sensor)
    ##  j = 0 to totalGroup (all sensor)
    
    return sumUtility

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
        if sensorGroup[x].kind == 0:
            utility = temperatureUtility(sensorGroup[x])
        elif sensorGroup[x].kind == 1:
            utility = pressureUtility(sensorGroup[x])
        elif sensorGroup[x].kind == 2:
            utility = distanceUtility(sensorGroup[x])
        ans = ":sensor["+str(x)+"] kind :"+str(sensorGroup[x].kind)+":arrival time:"\
            +str(sensorGroup[x].arrivalTime)+":transmission:"+str(sensorGroup[x].transmissionTime)\
            +":deadLine:"+str(sensorGroup[x].deadLine)+":weight:"+str(sensorGroup[x].weight)\
            +":priority:"+str(sensorGroup[x].priority)+":index:"+str(sensorGroup[x].index)+":utility:"+str(utility)+\
            ":origin:"+str(sensorGroup[x].origin)+":class:"+str(sensorGroup[x].classes)
        fo.write(":count:"+str(count)+ans+"\n")

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
