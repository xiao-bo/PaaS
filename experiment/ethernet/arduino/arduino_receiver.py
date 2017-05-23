import socket
import sys
import time
import subprocess 
from decimal import Decimal
from influxdb import InfluxDBClient
from datetime import datetime

def reply():
    if alignRestart == 0:
        connection.sendto(str(counter),client_address)#request
    T2 = time.time()
    return T2

def sync(T2,T3,C21,C22,C23,R):
    T2 = Decimal(T2)
    T3 = Decimal(T3)
    C21 = Decimal(C21)
    C22 = Decimal(C22)
    C23 = Decimal(C23)

    R = Decimal(R) * Decimal(0.000001)

    if C23 - C22 == 0:
        C23 = C23 + 4
    delay = ((T3 - T2) - (C23 - C22) * R) / 2
    
    T1 = T3 - delay - (C23 - C21) * R
    
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
def insertDataIntoDB(value,epochTime,samplingPeriod):
    timestamp = datetime.fromtimestamp(epochTime) 
    ## transform epochTime into 
    ## Year-Month-Day Hour-minute-second-millisceond
    print str(value)+"  "+str(timestamp)
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example3')
    jsonBody =[
        {
            "measurement":"arduino",
            "tags":{
                "host":"arduino"
            },
            "time":str(timestamp),

            "fields":{
                "value":int(value),
                "samplingPeriod":samplingPeriod
            }
        }
    ]
    #print jsonBody
    client.write_points(jsonBody)

def computeSamplingPeriod(T1,odd,baseLine):
    
    #print "0:"+str(baseLine[0])+":1:"+str(baseLine[1])+":T1:"+str(T1)+"  odd:"+str(odd)

    
    if odd %2 == 0:
        tmp = float(T1) - float(baseLine[0])
    else:
        tmp = float(T1) - float(baseLine[1])
    
    #if tmp > 0.9: ## avoid T1=445.256, base=444.259 -> error = 0.97
    #    tmp = 1.0 - tmp
    
    #tmp = str(tmp - int(tmp))[1:]
    #tmp = '0' + tmp
    #print tmp
    samplingPeriod = float(tmp)
    
    
    #error = error * 1000
    #if abs(error) > 300:
    #    error = 0.0
    #print " sampling period"+str(samplingPeriod)
    return abs(samplingPeriod)
def handleBigData(data,currentc21,currentT1,R):
    
    a = []
    print "handle big data\n\n"
    if "head" in data:
        dataRemovehead = data[5:]
        a = dataRemovehead.split(",")
    else:
        a = data.split(",")
    odd = 0
    counter = 0
    baseLine = [1.0,2.0]
    
    #print baseLine
    for line in a:
        #print line

        oldc21 = line.split(":")[1]
        #oldc21 = int(oldc21) - 200 * counter
        value = line.split(":")[3]
        T1 = calculateBeforeTime(oldc21,currentc21,currentT1,R)
        
        samplingPeriod = computeSamplingPeriod(T1,odd,baseLine)
        insertDataIntoDB(value,T1,samplingPeriod)
        if odd %2 == 0:
            baseLine[odd%2] = T1
            odd = 1
        elif odd %2 == 1:
            baseLine[odd%2] = T1
            odd = 2
        counter = counter +1
    print "bigdata finish \n\n"
def calculateBeforeTime(oldc21,currentc21,currentT1,R):
    currentc21 = Decimal(currentc21)
    oldc21 = Decimal(oldc21)
    R = Decimal(R) * Decimal(0.000001)

    oldT1 = currentT1 - (currentc21 - oldc21) * R 
    #print "calculateBeforeTime currentc21:"+str(currentc21)+" oldc21 "+str(oldc21)+" currentT1:"+str(currentT1)+"old:"+str(oldT1)
    return oldT1

def calculateAfterTime(oldc21,currentc21,oldT1,R):
    currentc21 = Decimal(currentc21)
    oldc21 = Decimal(oldc21)
    R = Decimal(R) * Decimal(0.000001)

    currentT1 = oldT1 + (currentc21 - oldc21) * R 
    #print "calculateAfterTime oldc21:"+str(oldc21)+" current21 "+str(c21)+" oldT1:"+str(oldT1)+"new:"+str(currentT1)
    return currentT1

if __name__ == "__main__":
    
    ## initialize part
    # Initial server address and port
    #host = "140.112.28.139"
    host = "192.168.11.3"
    #host = "192.168.0.103"
    port = 10005 #port=int(sys.argv[2])
    addr = (host,port)

    ## record variable
    longdata = "" ## for long data
    baseLine = [2.0,1.0]
    odd = 0 ## for sampling period

    actualT1 = 0  ## record old T1 for calculate after time
    oldc21 = 0 ## record old c21 for calculate after time
   
    ## protocol control variable
    alignRestart = 0 ## receive c22 once
    waitBigData = 5 ## receive long long data and wait current C1 and currentT1
    BigDataCounter = 0 ## control waitBigData

    # for shift clock data
    counter = 0
    
    #R
    R = 0.9995322189215448

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
    filename = sys.argv[1] + ".txt"
    if len(sys.argv[1]) == 0:
        print "please input arg for file name \n"
    
    # Wait for a connection
    print('waiting for a connection...')
    
    ## build socket connection
    connection, client_address = sock.accept()
    print('connection from %s:%d' % client_address)       
    
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example3')
    fo = open(filename,"wb")
    try:
        print "conntection\n"
        while True:
            waitBigData = waitBigData - BigDataCounter
            ## Receive the data one byte at a time
            #connection.settimeout(2.0)
            try:
                data = connection.recv(18000)
                ## data format
                ## head:C21:xxxx:v:xxxx,
                ## head:C22:xxxx:C23:xxxx
                ## long data: head:C21:xxxx:value:xxxx,C21:xxxx,value:xxxx


                fo.write("\nreceived:"+data+" len"+str(len(data)))
                print "received data:"+data+" len"+str(len(data))
                ## receive R at beginning of protocol
                whatCounter = data.split(":")[1]
                head = data.split(":")[0]
                if waitBigData == 0:## wait actualT1 data
                   
                    handleBigData(longdata,oldc21,actualT1,R)
                    

                if ',' in data: ##long data
                    BigDataCounter = 1
                    longdata += data 
                    print "received data:"+longdata+" len"+str(len(longdata))
                    print "long data"
                else: 
                    if whatCounter == 'C21' :
                        T1 = time.time() 
                        T2 = reply()
                        value = data.split(":")[4]
                        c21 = data.split(":")[2]
                        
                        #c21 = int(c21) - 232 * counter## adjsut counter shfit
                        
                        if alignRestart == 1:
                            
                            T1 = calculateAfterTime(oldc21,c21,actualT1,R)
                            print "clock:"+str(value)+" T1:"+str(T1)
                            samplingPeriod = computeSamplingPeriod(T1,odd,baseLine)
                            insertDataIntoDB(value,T1,samplingPeriod)
                            if odd %2 == 0:
                                baseLine[odd%2] = T1
                                odd = 1
                            elif odd %2 == 1:
                                baseLine[odd%2] = T1
                                odd = 2

                            
                        
                    elif whatCounter == 'C22' and alignRestart == 0:
                        T3 = time.time()
                        
                        c22 = data.split(":")[2]
                        c23 = data.split(":")[4]
                        
                        actualT1 = sync(T2,T3,c21,c22,c23,R)
                        oldc21 = c21
                        print "clock:"+str(value)+" T1:"+str(actualT1)
                        print "align"+str(alignRestart)

                        insertDataIntoDB(value,actualT1,0.0)
                        alignRestart = 1

                    counter+=1
                    
                    
            except socket.timeout:
                connection.close()
                print "no more data, timeout"
                print "waiting for a connection..."
                alignRestart = 0
                ## build socket connection
                odd = 0
                connection, client_address = sock.accept()
                print('connection from %s:%d' % client_address)       
                continue
    finally:
        # Clean up the connection
        connection.close()
        fo.close()

