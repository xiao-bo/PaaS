from influxdb import InfluxDBClient
import time

def toMillisecond(time):
	hour = float(time.split(":")[0])
	minute = float(time.split(":")[1])
	secMillisecond = time.split(":")[2]
	secMillisecond = float(secMillisecond[:len(secMillisecond)-1])
	epoch = hour * 60 * 60 + minute * 60 + secMillisecond
	epoch = epoch * 1000
	#print epoch
	return epoch

def insertDataIntoDB(timestamp,error,ip):
    
    #print str(error)+"  "+str(timestamp)
    client = InfluxDBClient(ip, 8086, 'root', 'root', 'example4')
    jsonBody =[
        {
            "measurement":"errorForArduinoEdison",
            "tags":{
                "host":"errorForArduinoEdison"
            },
            "time":str(timestamp),

            "fields":{
                "error":error
            }
        }
    ]
    #print jsonBody
    client.write_points(jsonBody)



if __name__ == "__main__":
    ip = "10.88.3.131"    
    client = InfluxDBClient(ip, 8086, 'root', 'root', 'example4')
    
    counter = 1
    while counter>0:
        counter += 1
        result = client.query('SELECT * FROM "arduino" WHERE time > now() - 1m  and time < now() ;')
        result2 = client.query('SELECT * FROM "edison" WHERE time > now() - 1m  and time < now() ;')
        arduino = list(result.get_points())
        pi = list(result2.get_points())
        #print("Result: {0}".format(result))
        #data=list(result.get_points(measurement='arduino'))

        ## declare width = 2, height = 60
        arduinoEpoch = [[0 for x in range(2)] for y in range(60)]
        piEpoch = [[0 for x in range(2)] for y in range(60)]
        arduinoDate = [[0 for x in range(2)] for y in range(60)]
        arduinoPeriod = []
        arduinoPeriodDate = []

        for x in arduino:
            ## insert data into piEpoch list by 
            ## [sec]=sec.
            
            ## data processing to get sec and clock
            secMillisecond = x['time'].split(":")[2]  ## select sec+millisecond
            sec = secMillisecond.split(".")[0]
            if 'Z' in sec:
                sec = sec[len(sec)-1]
            sec = int(sec)
            secMillisecond = float(secMillisecond[:len(secMillisecond)-1])
            timestamp = x['time'].split("T")[1]

            ## 
            if int(x['value']) > 1000:  ## value is large than 1000, time is inserted 1th location. It is can asure data of arduino and pi same.
                arduinoEpoch[sec][0] = timestamp
                arduinoDate[sec][0] = x['time']
                #print "arduino[0]:"+str(arduinoEpoch[sec][1])
            elif int(x['value']) < 100:  ## value is large than 1000, time is inserted 2th location 
                arduinoEpoch[sec][1] = timestamp
                arduinoDate[sec][1] = x['time']
                #print "arduino[1]:"+str(arduinoEpoch[sec][1])
            #print "arduino sec"+str(sec) + ":value:"+str(x['value'])+" time:"+str(timestamp)

            ## for arduino period 
            arduinoPeriod.append(timestamp)
            arduinoPeriodDate.append(x['time'])


        for x in pi:  

            ## insert data into pinEpoch list by 
            ## [sec]=sec.
            #print x         
            secMillisecond = x['time'].split(":")[2]  ## select sec+millisecond
            sec = secMillisecond.split(".")[0]
            if 'Z' in sec:
                sec = sec[:len(sec)-1]
            sec = int(sec)
            secMillisecond = float(secMillisecond[:len(secMillisecond)-1])
            timestamp = x['time'].split("T")[1]

            if int(x['value']) > 1000:  ## value is large than 1000, time is inserted 1th location. It is can asure data of arduino and pi same.
                
                piEpoch[sec][0] = timestamp
                #print "pi[0]:"+str(piEpoch[sec][0])
            elif int(x['value']) < 100:  ## value is large than 1000, time is inserted 2th location 
                
                piEpoch[sec][1] = timestamp
                #print "pi[1]:"+str(piEpoch[sec][1])
            #print "pi sec"+str(sec) + ":value:"+str(x['value'])+" time:"+str(timestamp)
       
        

        
        for x in range(60):
            for y in range(2):
                #print " arduino epoch:"+str(arduinoEpoch[x][y])
                #print " pi  epoch:"+str(piEpoch[x][y])
                
                # pi and arduino must be have value
                if piEpoch[x][y] != 0 and arduinoEpoch[x][y] != 0: 
                    Atime = toMillisecond(arduinoEpoch[x][y])
                    Ptime = toMillisecond(piEpoch[x][y])
                    
                    #error = min(abs(Atime - Ptime),abs(Atime - Ptime2))

                    #print 'arduino:'+str(Atime)+' pi:'+str(Ptime)
                    #print 'arduino:'+str(arduinoEpoch[x])+' pi:'+str(piEpoch[x])
                    error = Atime - Ptime
                    print str(x)+":"+str(error)
                    insertDataIntoDB(arduinoDate[x][y],error,ip)
                else:  ## insert 0.0
                    #print "xxxx"+str(x)
                    error = 0.0                
        time.sleep(4)
        

	    
