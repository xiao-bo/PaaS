from sensor import Sensor
from sensor import printSensorAllProperty
import priorityAssignment as pa
import copy
from SchedulabilityAnalysis import isSchedule
def getFileLineCount(filename):
    numLines = sum(1 for line in open(filename))
    return numLines

def readSensorData(filename):
    fileRead = open(filename,'r')
    sensorGroup = []
    a =Sensor(1,1.0,1.0,1.0,1,1,1)
    numOfLines=getFileLineCount(filename)
    for x in range(0,numOfLines):
        sensorGroup.append(copy.deepcopy(a))
    x = 0
    for line in fileRead:
        ans = line.split(":")
        sensorGroup[x].kind = int(ans[1])
        sensorGroup[x].arrivalTime = int(ans[3])
        sensorGroup[x].transmissionTime = float(ans[5])
        sensorGroup[x].deadLine = int(ans[7])
        sensorGroup[x].weight = int(ans[9])
        sensorGroup[x].priority = int(ans[11])
        sensorGroup[x].index = int(ans[13])
        x = x+1
    #printSensorAllProperty(sensorGroup)        
    return sensorGroup

def thisSensorGroupisSchedule(sensorGroup):
    for x in range(len(sensorGroup)):
        print "x = {} = {}".format(x,isSchedule(sensorGroup,x))
        


if __name__ == '__main__':
    sensorGroup = readSensorData("sensorGroup.txt")
    optimalSet = readSensorData("optimalSet.txt")
    CPSet = readSensorData("CPSet.txt")
    ans,count=pa.priorityAssignmentAlgo(sensorGroup,[],sensorGroup)
    print "is sensorGroup schedulable? {}".format(ans)

    #thisSensorGroupisSchedule(sensorGroup)
    '''
    ans,count=pa.priorityAssignmentAlgo(optimalSet,[],sensorGroup)
    print "is optimalSet schedulable? {}".format(ans)
    ans,count=pa.priorityAssignmentAlgo(CPSet,[],sensorGroup)
    print "is CPSet schedulable? {}".format(ans)

    '''
