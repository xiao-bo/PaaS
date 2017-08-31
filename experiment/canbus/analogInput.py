
##### use python2.7 to urn
import time
from datetime import datetime
import grovepi
from influxdb import InfluxDBClient
import sys
def insertDataIntoDB(value,epochTime):
    timestamp = datetime.fromtimestamp(epochTime) 
    ## transform epochTime into 
    ## Year-Month-Day Hour-minute-second-millisceond
    #print str(value)+"  "+str(timestamp)

    client = InfluxDBClient('192.168.11.4', 8086, 'root', 'root', 'example3')
    jsonBody =[
        {
            "measurement":"pi",
            "tags":{
                "host":"pi"
            },
            "time":str(timestamp),

            "fields":{
                "value":int(value),
                
            }
        }
    ]
    client.write_points(jsonBody)

if __name__ == "__main__":
    #Sensor connected to A0 Port 
    pin = 16    # Pin 14 is A0 Port.
    change = 0 ## for sensing Value 
    grovepi.pinMode(pin,"INPUT")

    ##name of file
    filename = sys.argv[1] + "pi.txt"
    if len(sys.argv[1]) == 0:
        print("please input arg for file name")
    
    
    fo = open(filename,"w")

    while True:
        try:
            sensorValue = grovepi.analogRead(pin)
            if sensorValue !=change and (sensorValue==0 or sensorValue==1023):
                t = time.time()
                insertDataIntoDB(sensorValue,t)
                change = sensorValue
                print ("sensorValue:{}  time:{}".format(sensorValue,t))
                fo.write("pi sensorValue:"+str(sensorValue)+":time:"+str(t)+"\n")
            time.sleep(0.1)
        except IOError:
            print ("Error")
