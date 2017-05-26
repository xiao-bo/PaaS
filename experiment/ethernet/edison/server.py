# Message Receiver
import os
import socket 
import time
import sys
from influxdb import InfluxDBClient
from datetime import datetime
def insertDataIntoDB(value,epochTime):
    timestamp = datetime.fromtimestamp(float(epochTime)-28800.0) 
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
    
    ## Initial server ip address and port
    host = "192.168.11.4"
    port = 12000
    addr=(host,port)

    ## name of file
    filename=sys.argv[1]+".txt"
    json_body=[]
    
    ## initial socket property
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ## reuse socket immediately 
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    ## bind the socket to the port and ip address
    sock.bind(addr)

    ## listen for incoming connections
    sock.listen(5)
    print "Waiting to receive messages..."

    fo=open(filename,"wb")

    ##  build socket connection 
    connection,client_address= sock.accept()
    
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example3')
    while True:
        receiveData = connection.recv(200)
        print "\n"+str(receiveData)
        ## below for python client
        sendTime = receiveData.split(":")[1]
        value = receiveData.split(":")[0]
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
    
    connection.close()
    fo.close()
