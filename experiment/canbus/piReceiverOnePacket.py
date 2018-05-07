
### use python3 to execute this program !!!!!
import time
import can
from decimal import Decimal
from datetime import datetime
from influxdb import InfluxDBClient
import sys
def reply(msg,bus,alignRestart):
    T2 =0
    if alignRestart == 0:
        bus.send(msg)   ## send data
        T2 = time.time()
        print("reply")
    return T2

def sync(T2,T3,C21,C22,C23,R):
    T2 = Decimal(T2)
    T3 = Decimal(T3)
    C21 = Decimal(C21)
    C22 = Decimal(C22)
    C23 = Decimal(C23)

    R = Decimal(R) * Decimal(0.000001)
    if C23-C22 ==0:
        C23 = C22+4
    delay = ((T3 - T2) - (C23 - C22) * R) / 2
    #delay = Decimal(0.0004)
    T1 = T3 - delay - (C23 - C21) * R
    
    print ("C21:"+str(C21))
    print ("C22:"+str(C22))
    print ("C23:"+str(C23))
    print ("T2:"+str(T2))
    print ("T3:"+str(T3))
    print ("R:"+str(R))
    print ("R*(C23-C21): "+str((C23-C21)*R))
    print ("R*(C23-C22): "+str((C23-C22)*R))
    print ("T3-T2:"+str(T3-T2))
    print ("delay = ((T3-T2)-(C23-C22)*R)/2 = "+str(delay))
    print ("R= "+str(R))
    print ("actual T1 = T3 - delay - (C23-C21) * R =  "+str(T1))
    print ("sync") 
    return T1


def calculateAfterTime(oldc21,currentc21,oldT1,R):
    currentc21 = Decimal(currentc21)
    oldc21 = Decimal(oldc21)
    R = Decimal(R) * Decimal(0.000001)

    currentT1 = oldT1 + (currentc21 - oldc21) * R 
    #print "calculateAfterTime oldc21:"+str(oldc21)+" current21 "+str(c21)+" oldT1:"+str(oldT1)+"new:"+str(currentT1)
    return currentT1

def getPayloadFromPacket(receiveList):

    ## analyze sensor value is 1023 or 0 or align packet
    if '64' in receiveList:
        value = 0
        target = 'c'
    elif '65' in receiveList:
        value = 1023
        target = 'd'
    
    ## represent align packet
    elif '66' in receiveList:
        value = -1
        target = 'e'

    ## just reserved payload()
    payload = receiveList[4::1]
    ## reversed payload
    payload = payload[::-1]
    startIndex = payload.index('ff')
    ans = ""
    for x in range(startIndex+1,7):
        tmp = str(int(payload[x],16))
        if len(tmp)<2:
            #print('0'+tmp)
            tmp = '0'+tmp
        ans = ans+tmp
    return ans,target,value

def insertDataIntoDB(value,epochTime):
    timestamp = datetime.fromtimestamp(epochTime) 
    ## transform epochTime into 
    ## Year-Month-Day Hour-minute-second-millisceond
    #print str(value)+"  "+str(timestamp)
    #print("insert")
    client = InfluxDBClient('10.88.10.91', 8086, 'root', 'root', 'example4')
    jsonBody =[
        {
            "measurement":"arduino",
            "tags":{
                "host":"arduino"
            },
            "time":str(timestamp),

            "fields":{
                "value":int(value),
                
            }
        }
    ]
    #print(timestamp) 
    i=client.write_points(jsonBody)



if __name__ == "__main__":
    ## value is 0 or 1023
    target = 'a'  ## c or d 
    ## initial can network
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native') 

    ## data part 1 or part 2 
    part = 1
    
    ## initial packet 
    msg = can.Message(arbitration_id=0x00,data=[0, 25, 0, 1, 3, 1, 4, 1])
    R=1.00016319556 ## too high
    receiveT1 = ""
    T3 = ""
    T2 = ""
    ## protocol control variable
    alignRestart = 0  ## receive c22 once

    actualT1 = 0 ## record old T1 for calculate after time
    oldc21 = 0 ## record old c21 for calculate after time
    
    ##name of file
    filename = sys.argv[1] + ".txt"
    if len(sys.argv[1]) == 0:
        print("please input arg for file name")
    
    
    fo = open(filename,"w")
     
    while True:
        ## receiver data format is 
        ## 1504018295.064378        0001    000    8    0d 00 01 06 04 00 00 02
        receiveData = str(bus.recv())   ## receiver data
            
        ## split data = 
        ##['1504018295.064378', '0001', '000', '8', '0d', '00', '01', '06', '04', '00', '00', '02']
        
        receiveList = receiveData.split()
        print(receiveList)
        ## filter ID
        if receiveList[1] != "0003" and receiveList[1] != "0004":
            print("filter")
            continue
        
        payload,target,value = getPayloadFromPacket(receiveList)
        #print(c21)

        ## c or d represent payload packet
        if (target =='c' or target == 'd'): 
            receiveT1 = receiveList[0]
            c21 = payload
            print("receiveT1:{}".format(receiveT1))

            ## alignRestart = 0 represent first align
            if alignRestart == 0:
                T2 = reply(msg,bus,alignRestart)
                #print("T2:{}".format(T2))
                fo.write("c21:"+str(c21)+":value:"+str(value)+":time:"+str(actualT1)+":receiveT1:"+str(receiveT1)+"\n")
                #insertDataIntoDB(value,actualT1)
                
            ## alignRestart = 1 represent finish align, just calculate each message time
            elif alignRestart == 1:
                T1 = calculateAfterTime(oldc21,c21,actualT1,R)

                print("c21:{}:value:{}:T1:{}:receiveT1:{}".format(c21,value,T1,receiveT1))
                #print("value:{}:T1:{}".format(value,T1))
                fo.write("c21:"+str(c21)+":value:"+str(value)+":time:"+str(T1)+":receiveT1:"+str(receiveT1)+"\n")
                #insertDataIntoDB(value,T1)
        ##target e represent align packet
        elif target == 'e' and alignRestart ==0 : 
            
            ## receive T3
            T3 = receiveList[0]
            print("T3:{}".format(T3))
            ## receive c22
            c22 = payload
            #c22,tmp,tmp2 = getPayloadFromPacket(receiveList)
            actualT1 = sync(T2,T3,c21,c22,c22,R)
            oldc21 = c21
            print ("c21:{} value:{} actualT1:{}:receiveT1:{}".format(c21,value,actualT1,receiveT1))
            alignRestart =1
        
        #print("align:{}".format(alignRestart))
