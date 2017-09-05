# Message Sender for edison 
import sys
import time
import mraa
import socket
from datetime import datetime
from influxdb import InfluxDBClient

def insertDataIntoDB(value,epochTime):
    timestamp = datetime.fromtimestamp(epochTime-28800) 
    ## transform epochTime into 
    ## Year-Month-Day Hour-minute-second-millisceond

    client = InfluxDBClient('192.168.11.4', 8086, 'root', 'root', 'example4')
    jsonBody =[
        {
            "measurement":"edison",
            "tags":{
                "host":"edison"
            },
            "time":str(timestamp),

            "fields":{
                "value":int(value),
                
            }
        }
    ]
    #print(timestamp) 
    client.write_points(jsonBody)

if __name__=='__main__':
        change = 1023
        
        pinNumber = 1

        filename = sys.argv[1]+"edison.txt"
        fo = open(filename,'w')
        
        while True:
	    pot = mraa.Aio(pinNumber)
	    potVal = pot.read()
            if potVal != change and (potVal==0 or potVal==1023):
                timestamp = time.time()
                message = str(potVal)+":"+str(timestamp)
                print message
                fo.write(message+"\n")
                insertDataIntoDB(potVal,timestamp)
                change = potVal
        
        fo.close()
