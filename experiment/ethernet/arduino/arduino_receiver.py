import socket
import sys
import time
import subprocess 
from decimal import Decimal
from influxdb import InfluxDBClient
from datetime import datetime
import random
# Initial server address and port
#host="140.112.28.139"
#host="192.168.11.3"
host="192.168.0.103"
#port=int(sys.argv[2])
port=10005
addr=(host,port)
json_body=[]
bufferT1=[]
baseLine=[2.0,1.0]
flag2=[0]
a=0
## sync flag
flag=0
def reply():
    connection.sendto("c",client_address)#request
    T2=time.time()
    return T2

def sync(T2,T3,C21,C22,C23,R):
    T2=Decimal(T2)
    T3=Decimal(T3)
    C21=Decimal(C21)
    C22=Decimal(C22)
    C23=Decimal(C23)

    R=Decimal(R)*Decimal(0.000001)
    if C23-C22==0:
        C23=C23+4
    delay=((T3-T2)-(C23-C22)*R)/2
    
    T1=T3-delay-(C23-C21)*R
    
    """ debug message
    print "C21:"+str(C21)
    print "T2:"+str(T2)
    print "T3:"+str(T3)
    print "R:"+str(R)
    print "C23-C21: "+str((C23-C21)*R)
    print "delay= "+str(delay)
    print "T3-T2:"+str(T3-T2)
    print "R= "+str(R)
    print "actual T1= "+str(T1)
    print "sync" 
    """

    return T1
def insertDataIntoDB(value,epochTime):
    timestamp = datetime.fromtimestamp(epochTime) 
    ## transform epochTime into 
    ## Year-Month-Day Hour-minute-second-millisceond
    print str(value)+"  "+str(timestamp)
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example3')
    error=computeError(epochTime)
    tmp_json={
    "measurement":"cos",
    "tags":{
        "host":"arduino"
    },
    "time":str(timestamp),

    "fields":{
        "value":int(value),
        "error":error
        }
    }
    json_body.append(tmp_json)
    client.write_points(json_body)

def computeError(T1):
    
    
    if flag2[0]==0:
        a=float(T1)-float(baseLine[0])
        baseLine[0]=T1
        flag2[0]=1
    else:
        a=float(T1)-float(baseLine[1])
        baseLine[1]=T1
        flag2[0]=0
    
    a = str(a-int(a))[1:]
    a='0'+a
    error=float(a)
    if error>0.4 and error <0.6:
        error=error-0.5
    elif error>0.9:
        error=1-error
    error=error*1000

    #print "a:"+str(a)+" error:"+str(error)
    return abs(error)
def handleBigData(data,T3,delay):

    
    a=data.split(",")
    
    for x in a:
        print x
    print T3-delay
    for x in range(0,len(a)):
        bufferT1.insert(0,T3-delay-x)
        insertDataIntoDB(1023,T3-delay-x)
        
    print bufferT1
    

if __name__=="__main__":
    
    ## Inital socket property
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ## AF_INET can send data to public IP
    ## sock_stream as TCP
    ## reuse socket immediately
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    ## Bind the socket to the port and ip address
    sock.bind(addr)

    ## Listen for incoming connections
    sock.listen(5)
    
    ##name of file
    filename=sys.argv[1]+".txt"
    
    
    if len(sys.argv[1])==0:
        print "please input arg for file name \n"
    #print filename
    
    
    # Wait for a connection
    print('waiting for a connection...')
    
    ## build socket connection
    connection, client_address = sock.accept()
    print('connection from %s:%d' % client_address)       
    
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example3')
    fo=open(filename,"wb")
    try:
        print "conntection\n"
        while True:
            
            ## Receive the data one byte at a time
            connection.settimeout(1.0)
            try:
                data = connection.recv(18000)
                ## data format
                ## head:C21:xxxx:value:xxxx,
                ## C22:xxxx:C23:xxxx
                ## long data: head:C21:xxxx:value:xxxx,C21:xxxx,value:xxxx


                #fo.write("received:"+data+" len"+str(len(data)))
                print "received data:"+data+" len"+str(len(data))
                ## receive R at beginning of protocol
                whatCounter=data.split(":")[1]
                head=data.split(":")[0]
                print whatCounter
                if ',' in data: ##long data 
                    print "long data"
                else: ## 2th or 3th packet    
                    if whatCounter == 'C21' :
                        T1=time.time() 
                        T2=reply()
                        value=data.split(":")[4]
                        c21=data.split(":")[2]
                    elif whatCounter == 'C22':
                        T3=time.time()
                        R=1.0
                        c22=data.split(":")[2]
                        c23=data.split(":")[4]
                        actual_T1=sync(T2,T3,c21,c22,c23,R)
                        print "clock:"+str(value)+" T1:"+str(actual_T1)
                    
                '''
                if len(data)==0:
                    print "disconnect"
                elif len(data)>0 and len(data)<10 :
                    R=data
                elif len(data)>=20 and len(data)<38:
                    ## receive c21

                    T1=time.time() 
                    T2=reply()
                    value=data.split(":")[0]
                    c21=data.split(":")[2]
                    """ debug message
                    #print "C21:"+str(c21)
                    #print "T1: %.9f"%T1
                    """
                    ## receive c22,c23
                elif len(data)>=38 and len(data)<100:
                    T3=time.time()
                    """ debug message
                    print "split[1]: "+str(data.split(":")[2])
                    print "split[3]: "+str(data.split(":")[4])
                    """
                    R=1.0
                    ##process receive message
                    c22=data.split(":")[2]
                    c23=data.split(":")[4]
                    actual_T1=sync(T2,T3,c21,c22,c23,R)
                    
                    #print "clock:"+str(value)+" T1:"+str(actual_T1)+":rece_T1:%.9f"%T1
                    delay=Decimal(T1)-actual_T1
                    #print delay

                    insertDataIntoDB(value,actual_T1)
                    fo.write(str(actual_T1)+":rece_T1:"+str(Decimal(T1))+'\n')
                elif len(data)>=100:
                    T3=time.time()
                    delay=0.0005229114837646484375
                    handleBigData(data,T3,delay)
                    print "len of data >120 "+str(T3)

                else:
                    connection.close()
                    print('no more data, closing connection.')
                '''
            except socket.timeout:
                connection.close()
                print "no more data, timeout"
                print "waiting for a connection..."
                
                ## build socket connection
                connection, client_address = sock.accept()
                print('connection from %s:%d' % client_address)       
                continue
    finally:
        # Clean up the connection
        connection.close()
        fo.close()

