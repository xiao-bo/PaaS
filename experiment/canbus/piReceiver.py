### use python3 to execute this program !!!!!
import time
import can
from decimal import Decimal
def reply(msg,bus,alignRestart):
    T2 =0
    if alignRestart == 0:
        bus.send(msg)   ## send data
        T2 = time.time()
    return T2

def sync(T2,T3,C21,C22,C23,R):
    T2 = Decimal(T2)
    T3 = Decimal(T2)
    C21 = Decimal(C21)
    C22 = Decimal(C22)
    C23 = Decimal(C23)

    R = Decimal(R) * Decimal(0.000001)
    if C23-C22 ==0:
        C23 = C22+4
    delay = ((T3 - T2) - (C23 - C22) * R) / 2
    
    T1 = T3 - delay - (C23 - C21) * R
    
    print ("C21:"+str(C21))
    print ("T2:"+str(T2))
    print ("T3:"+str(T3))
    print ("R:"+str(R))
    print ("C23-C21: "+str((C23-C21)*R))
    print ("delay= "+str(delay))
    print ("T3-T2:"+str(T3-T2))
    print ("R= "+str(R))
    print ("actual T1= "+str(T1))
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

    ## analyze sensor value is 1023 or 0
    if '0d' in receiveList:
        value = 1023
        target = 'd'
        #print ("0d (value = 1023) in List")
    elif '0c' in receiveList:
        value = 0
        target = 'c'
        #print("0c (value = 0) in list")
    elif '0e' in receiveList:
        value = 0
        target = 'e'
        #print("0e (value = 0) in list")

    ## just reserved payload()
    payload = receiveList[4::1]

    ## reversed payload
    payload = payload[::-1]
    ## concatenate element in list into a string
    payload=''.join(payload)
    ## remove prefix (0) of elements
    payload = payload[1::2]
    print(payload)
    return payload,target


if __name__ == "__main__":
    ## value is 0 or 1023
    target = 'a'  ## c or d 
    ## initial can network
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native') 

    ## data part 1 or part 2 
    part = 1
    receivePart1 = '0'
    ## initial packet 
    msg = can.Message(arbitration_id=0x01,data=[0, 25, 0, 1, 3, 1, 4, 1])
    R = 1.0
    T3 = ""
    T2 = ""
    ## protocol control variable
    alignRestart = 0  ## receive c22 once

    actualT1 = 0 ## record old T1 for calculate after time
    oldc21 = 0 ## record old c21 for calculate after time

    
    while True:
        ## receiver data format is 
        ## 1504018295.064378        0001    000    8    0d 00 01 06 04 00 00 02
        receiveData = str(bus.recv())   ## receiver data
        ## split data = 
        ##['1504018295.064378', '0001', '000', '8', '0d', '00', '01', '06', '04', '00', '00', '02']
        receiveList = receiveData.split()
        print(receiveData) 
        payload,target = getPayloadFromPacket(receiveList)
        
        ## skip short message , for example , d003434d
        if payload[0]==payload[7] and payload[0] ==target:
            print("skip this time")
            alignRestart = 0
            continue

        index = payload.find(target)
        if index == 7 and (target =='c' or target == 'd'): 
            ## target is in payload, in order words, 
            ## payload is PART1 of data
            ## for example , 1234567c, just move 1234567 into part1
            receivePart1 = payload[:7:1]
            receivePart2 = ""
            T1 = receiveList[0]

        elif target == 'e' and alignRestart ==0 : 
            ## receive c22
            receivePart1 = payload[:7:1]
            receivePart2 = ""
            T3 = receiveList[0]
            print("T3:{}".format(T3))
            alignRestart =1
        else:
            ## target is second position in payload
            ## for example , payload = 12d34567
            ## just get 34567 into part2
            receivePart2 = payload[index+1::1]


        ## because arduino send reversed payload to master like payload1: c02345678
        ## payload2 : 91234c10
        ## real payload is 1087654320
        ## so we have to put part2 on first and part1 on second 
        if receivePart2 != "":
            if target !='e':
                c21 = receivePart2+receivePart1
                print("c21:{}".format(c21))
                T2 = reply(msg,bus,alignRestart) 
                print("T2:{}".format(T2))
                if alignRestart ==1:
                    T1 = calculateAfterTime(oldc21,c21,actualT1,R)
                    print("T1:{}".format(T1))
            elif target =='e':
                ## receive reply message
                c22 = receivePart2+receivePart1
                print("c22:{}".format(c22))
                actualT1 = sync(T2,T3,c21,c22,c22,R)
                oldc21 = c21
                print ("actualT1:{}".format(actualT1))
        print("align:{}".format(alignRestart))

'''
#bus.send(msg)   ## send data
'''
