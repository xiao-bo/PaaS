### use python3 to execute this program !!!!!
import time
import can


if __name__ == "__main__":
    ## initial can network
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native') 

    msg = can.Message(arbitration_id=0x7de,data=[0, 25, 0, 1, 3, 1, 4, 1])
    
    while True:
        ## receiver data format is 
        ## 1504018295.064378        0001    000    8    0d 00 01 06 04 00 00 02
        receiveData = str(bus.recv())   ## receiver data
        print(receiveData)
        '''
        #bus.send(msg)   ## send data
        '''
