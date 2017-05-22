# Message Receiver
import os
from socket import *
import time
import subprocess
import sys
from influxdb import InfluxDBClient
from datetime import datetime
## Initial server ip address and port
host = "192.168.11.3"
#host="140.112.28.139"
#port = int(sys.argv[2])
port = 12000
addr=(host,port)

## name of file
filename=sys.argv[1]+".txt"

json_body=[]
def insertDataIntoDB(value,epochTime):
    timestamp = datetime.fromtimestamp(float(epochTime)) 
    ## transform epochTime into 
    ## Year-Month-Day Hour-minute-second-millisceond
    print str(value)+"  "+str(timestamp)
    
    tmp_json={
    "measurement":"edison",
    "time":str(timestamp),
    "tags":{
        "host":"edison"
    },
    "fields":{
        "value":int(value)
        }
    }
    json_body.append(tmp_json)
    client.write_points(json_body)

if __name__=="__main__":
    
    ## initial socket property
    Sock = socket(AF_INET, SOCK_STREAM)

    ## reuse socket immediately 
    Sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    ## bind the socket to the port and ip address
    Sock.bind(addr)

    ## listen for incoming connections
    Sock.listen(5)
    print "Waiting to receive messages..."

    fo=open(filename,"wb")

    ##  build socket connection 
    connection,client_address= Sock.accept()
    
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example3')
    while True:
        receiveData=connection.recv(200)
        print "\n"+str(receiveData)
        ## below for python client
        sendTime=receiveData.split(":")[1]
        value=receiveData.split(":")[0]
        insertDataIntoDB(value,sendTime)
        
        ## below for c client
        #sendTime=receiveData.split(":")[1]
        #value=receiveData.split(":")[0]
        #rece_time=time.time()
        #ans="Value:"+str(value)+" send_Time"+str(sendTime)+": rece_time:%.9f"%rece_time
        #print float(rece_time)-float(send_time)
        #ans = "Value:"+str(value)+" send Time:"+str(sendTime)
        #client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example3')
        #insertDataIntoDB(value,sendTime)
        #print ans
        #fo.write(ans+'\n')
    
    csock.close()
    fo.close()
