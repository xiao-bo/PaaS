### use python3 to execute this program !!!!!
import time
import can


if __name__ == "__main__":
    ## value is 0 or 1023
    target = 'a'  ## c or d 
    ## initial can network
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native') 

    ## data part 1 or part 2 
    part = 1
    receivePart1 = 0
    ## initial packet 
    msg = can.Message(arbitration_id=0x7de,data=[0, 25, 0, 1, 3, 1, 4, 1])
    T1 = 0
    
    
    while True:
        ## receiver data format is 
        ## 1504018295.064378        0001    000    8    0d 00 01 06 04 00 00 02
        receiveData = str(bus.recv())   ## receiver data
        print(receiveData)
        ## split data = 
        ##['1504018295.064378', '0001', '000', '8', '0d', '00', '01', '06', '04', '00', '00', '02']
        receiveList = receiveData.split()

        ## analyze sensor value is 1023 or 0
        if '0d' in receiveList:
            value = 1023
            target = 'd'
            print ("0d (value = 1023) in List")
        elif '0c' in receiveList:
            value = 0
            target = 'c'
            print("0c (value = 0) in list")
    
        ## just reserved payload()
        payload = receiveList[4::1]

        ## reversed payload
        payload = payload[::-1]
        ## concatenate element in list into a string
        payload=''.join(payload)
        ## remove prefix (0) of elements
        payload = payload[1::2]
        print(payload)
    
        ## skip short message , for example , d003434d
        if payload[0]==payload[7] and payload[0] ==target:
            print("skip this time")
            continue


        index = payload.find(target)
        if index == 7: 
            ## target is in payload, in order words, 
            ## payload is PART1 of data
            ## for example , 1234567c, just move 1234567 into part1
            print("target is on 7")
        
            receivePart1=payload[:7:1]
            receivePart2 = ""
            T1 = receiveList[0]
        else:
            ## target is second position in payload
            ## for example , payload = 12d34567
            ## just get 34567 into part2
            receivePart2 = payload[index+1::1]


        ## because arduino send reversed payload to master like payload1: c02345678
        ## payload2 : 91234c10
        ## real payload is 1087654320
        ## so we have to put part2 on first and part 2 on second 
        c21 = receivePart2+receivePart1
        print("c21:{}".format(c21))


'''
#bus.send(msg)   ## send data
'''
