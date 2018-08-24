import copy

import math
import numpy as np
import random
import time
import sys

from operator import attrgetter
from sensor import Sensor
from sensor import printSensorAllProperty
from sensor import printSensorPriority
from sensor import writeSensorData
from sensor import temperatureUtility
from sensor import pressureUtility
from sensor import distanceUtility
from sensor import getSumUtility
from sensor import deadLineToFreq
from maximal import selectMaximalSet
from cp import selectCPSet

def produceSensor(totalNumber,assignedNumber):
    sensorGroup = []
    a = Sensor(0,1.0,1.0,1.0,1,1,1,0,0)
    for x in range(0,totalNumber):
        sensorGroup.append(copy.deepcopy(a))
   
    #printSensorPriority(sensorGroup)

    return produceUniformData(sensorGroup,sensorGroup[:assignedNumber],sensorGroup[assignedNumber:])
    
def produceUniformData(sensorGroup,assignedArray,unassignedArray):
    ## time level is us
    ## temperature sensor's frequency = 20hz,10hz,8hz,4hz,2hz,1hz
    temperatureDeadline = [50000,100000,125000,250000,500000,1000000]
    ## pressure sensor's frequency 100hz,20hz,10hz,8hz,4hz,2hz,1hz
    pressureDeadline = [10000,50000,100000,125000,250000,500000,1000000]
    ## distance sensor's frequency 100hz,20hz,10hz,8hz,4hz,2hz,1hz
    distanceDeadline = [10000,50000,100000,125000,250000,500000,1000000]
    
    ## remove 10000 for meeting slide
    #pressureDeadline = [10000,50000,100000,125000,250000,500000,1000000]
    ## distance sensor's frequency 100hz,20hz,10hz,8hz,4hz,2hz,1hz
    #distanceDeadline = [10000,50000,100000,125000,250000,500000,1000000]
    
    #deadLine = [10000,50000,100000,200000,1000000]

    arrivalTime = [100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]
    kinds = [0,1,2]
    length = len(sensorGroup)
    weight = random.sample(xrange(1,length+1),length)
    
    ## initial property of sensorGroup
    index = 1
    for x in sensorGroup:

        x.transmissionTime = 5*(64 + 8 * math.ceil(np.random.uniform(0,3,1)))
        x.kind = random.choice(kinds)
        if x.kind == 0:
            x.deadLine = random.choice(temperatureDeadline)
        elif x.kind == 1:
            x.deadLine = random.choice(pressureDeadline)
        elif x.kind == 2:
            x.deadLine = random.choice(distanceDeadline)
        x.weight = weight[index-1]
        x.arrivalTime = random.choice(arrivalTime)
        x.index = index
        index = index + 1
        

    ## initial priority of unassignedArray
    if unassignedArray:
        for x in unassignedArray:
            x.priority = 0
            x.origin = 0
            x.classes = 0

    ## initial priority of assignedArray 
    if assignedArray:
        priority = random.sample(xrange(1,len(assignedArray)+1),len(assignedArray))  
        i = 0
        

        for x in assignedArray:
            x.priority = priority[i]
            x.origin = 1
            x.classes = 0
            i = i + 1

    #printSensorAllProperty(sensorGroup)
   
    return sensorGroup
def getUtility(x):
    utility = 0
    if x.kind == 0:
        utility = temperatureUtility(x)
    elif x.kind == 1:
        utility = pressureUtility(x)
    elif x.kind ==2:
        utility = distanceUtility(x)
    return utility 
def classification(totalGroup,sensorGroup):
    category = [[],[],[],[],[],[],[],[],[],[]]
    utilityWeight = []
    for x in totalGroup :
        #print "weight:{} utility:{}".format(x.weight,getUtility(x))
        utilityWeight.append(x.weight*getUtility(x))
    #print utilityWeight
    a = np.array(utilityWeight)
    #a = np.array([1,2,3,4,5,6,7,8,9,10])
    p = np.percentile(a,10)
    for x in totalGroup:
        #print "utility:{}".format(x.weight*getUtility(x))
        if x.weight*getUtility(x) < np.percentile(a,10):
            #print "10%:{}".format(np.percentile(a,10))
            category[0].append(x)    
        elif x.weight*getUtility(x) >= np.percentile(a,10) and x.weight*getUtility(x) < np.percentile(a,20):
            #print "20%:{}".format(np.percentile(a,20))
            category[1].append(x)    
        elif x.weight*getUtility(x) >= np.percentile(a,20) and x.weight*getUtility(x) < np.percentile(a,30):
            #print "30%:{}".format(np.percentile(a,30))
            category[2].append(x)    
        elif x.weight*getUtility(x) >= np.percentile(a,30) and x.weight*getUtility(x) < np.percentile(a,40):
            #print "40%:{}".format(np.percentile(a,40))
            category[3].append(x)    
        elif x.weight*getUtility(x) >= np.percentile(a,40) and x.weight*getUtility(x) < np.percentile(a,50):
            #print "50%:{}".format(np.percentile(a,50))
            category[4].append(x)    
        elif x.weight*getUtility(x) >= np.percentile(a,50) and x.weight*getUtility(x) < np.percentile(a,60):
            #print "60%:{}".format(np.percentile(a,60))
            category[5].append(x)    
        elif x.weight*getUtility(x) >= np.percentile(a,60) and x.weight*getUtility(x) < np.percentile(a,70):
            #print "70%:{}".format(np.percentile(a,70))
            category[6].append(x)    
        elif x.weight*getUtility(x) >= np.percentile(a,70) and x.weight*getUtility(x) < np.percentile(a,80):
            category[7].append(x)    
            #print "80%:{}".format(np.percentile(a,80))
        elif x.weight*getUtility(x) >= np.percentile(a,80) and x.weight*getUtility(x) < np.percentile(a,90):
            #print "90%:{}".format(np.percentile(a,90))
            category[8].append(x)    
        elif x.weight*getUtility(x) >= np.percentile(a,90):
            category[9].append(x)
    z = 10
    '''
    for x in category:
        for y in x:
            print "{}%:{}".format(z,y.weight*getUtility(y))
        z = z+10
        #print "===="
    '''
    return category
def computeCategoryProportion(category,sensorGroup):
    ## print all length of cols
    ## get every class length
    allClassLength = map(len,category)
    #print allClassLength
    
    #print sensorGroup
    SensorCount = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    for x in sensorGroup:
        for i in range(0,10):
            if x in category[i]:
                ## if x belongs class i
                SensorCount[i] = SensorCount[i]+1.0
                x.classes = (i+1)
                break  
    #print SensorCount
    proportion = []
    for x in range(0,len(SensorCount)):
        if SensorCount[x]!=0:
            proportionTmp = SensorCount[x]/float(allClassLength[x]) 
        else:
            proportionTmp = 0.0
        #print "class{}:{}".format(x,proportionTmp)
        proportion.append(proportionTmp)
    return proportion

def test():
    sumWeight = 0
    
    weight = [15,14,13,12,11,9,8,7,6,5,4,3]
    for x in weight:
        sumWeight = sumWeight + math.pow(100,12)* x
    print sumWeight

def main():
    

    ### arrival time, transmission time, deadLine, weight, priority, index

    totalNumber = 10
    assignedNumber = 0
    diffArray = []

    dire = ""
    filename = dire+"1.txt" 
    fo = open(filename,"w")
    fo.write("number sensor :"+str(totalNumber)+"\n")
    fmaximalSet = open(dire+"maximalSet.txt","w")
    fCPSet = open(dire+"CPSet.txt",'w')
    ftotalSet = open(dire +"totalSet.txt",'w')
    for x in range(0,100):
        totalGroup = produceSensor(totalNumber,assignedNumber)
        start_time = time.time()
        print x
        
        printSensorAllProperty(totalGroup)
        #print "get maximal"

        category = classification(totalGroup,totalGroup)     
    
        maximalSet = selectMaximalSet(totalGroup[:assignedNumber],totalGroup[assignedNumber:])
        #printSensorAllProperty(maximalSet)
        #print "get cp"
        

        #print "maximal utility :{}".format(sumUtilityofmaximalSet)
        CPSet = selectCPSet(totalGroup[:assignedNumber],totalGroup[assignedNumber:])
        #printSensorAllProperty(CPSet)
        ## sort CPset by weight with descending order
        CPSet = sorted(CPSet,key=attrgetter("weight"),reverse=True)
        #print "get cp"
        #printSensorAllProperty(CPSet)
        sumUtilityofTotalSet = getSumUtility(totalGroup,totalGroup)
        sumUtilityofMaximalSet = getSumUtility(totalGroup,maximalSet)
        sumUtilityofCPSet = getSumUtility(totalGroup,CPSet)
        difference = sumUtilityofMaximalSet-sumUtilityofCPSet
   
        ProportionOfMaximal = computeCategoryProportion(category,maximalSet)
        ProportionOfCP = computeCategoryProportion(category,CPSet) 
        print "maximal {}".format(ProportionOfMaximal)
        print "CP {}".format(ProportionOfCP)
        fo.write("maximalSet proportion : ")
        for i in range(0,len(ProportionOfMaximal)):
            fo.write(str(ProportionOfMaximal[i])+":")
        
        fo.write("CP proportion : ")
        for i in range(0,len(ProportionOfCP)):
            fo.write(str(ProportionOfCP[i])+":")
        fo.write("total utility:"+str(sumUtilityofTotalSet)+":maximalSet utility : "+str(sumUtilityofMaximalSet)+":CP utility : "+
            str(sumUtilityofCPSet)+":difference:"+str(difference)+"\n")
        writeSensorData(totalGroup,ftotalSet,x)
        writeSensorData(maximalSet,fmaximalSet,x)
        writeSensorData(CPSet,fCPSet,x)
        elapsed_time = time.time() - start_time
        print "x = {} elaspsetTime= {}".format(x,elapsed_time)
        

        print "total utility :{}".format(sumUtilityofTotalSet)
        print "maximal utility :{}".format(sumUtilityofMaximalSet)
        print "CP utility :{}".format(sumUtilityofCPSet)
       


if __name__ == "__main__":
    main()
    ### kind,arrival time, transmission time, deadLine, weight, priority, index

    a = Sensor(1,0,1.0,400000.0,1,1,1,1,0)
    #temperatureUtility(a)
    #distanceUtility(a)
    #pressureUtility(a)
