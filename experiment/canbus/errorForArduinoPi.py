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

def insertDataIntoDB(timestamp,error):
    
    #print str(error)+"  "+str(timestamp)
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example3')
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

def insertPeriodIntoDB(timestamp,samplingPeriod):
    ## insert Arduino period into DB
    
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example3')
    jsonBody =[
        {
            "measurement":"period",
            "tags":{
                "host":"period"
            },
            "time":str(timestamp),

            "fields":{
                "samplingPeriod":samplingPeriod
            }
        }
    ]
    #print jsonBody
    client.write_points(jsonBody)


if __name__ == "__main__":
    
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example3')
    
    counter = 1
    while counter>0:
        counter += 1
        result = client.query('SELECT * FROM "arduino" WHERE time > now() - 1m  and time < now() ;')
        result2 = client.query('SELECT * FROM "edison" WHERE time > now() - 1m  and time < now() ;')
        arduino = list(result.get_points())
        edison = list(result2.get_points())
        #print("Result: {0}".format(result))
        #data=list(result.get_points(measurement='arduino'))

        ## declare width = 2, height = 60
        arduinoEpoch = [[0 for x in range(2)] for y in range(60)]
        edisonEpoch = [[0 for x in range(2)] for y in range(60)]
        arduinoDate = [[0 for x in range(2)] for y in range(60)]
        arduinoPeriod = []
        arduinoPeriodDate = []

        for x in arduino:
            ## insert data into edisonEpoch list by 
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
            if int(x['value']) > 1000:  ## value is large than 1000, time is inserted 1th location. It is can asure data of arduino and edison same.
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


        for x in edison:  
            ## insert data into edisonEpoch list by 
            ## [sec]=sec.
            #print x         
            secMillisecond = x['time'].split(":")[2]  ## select sec+millisecond
            sec = secMillisecond.split(".")[0]
            if 'Z' in sec:
                sec = sec[:len(sec)-1]
            sec = int(sec)
            secMillisecond = float(secMillisecond[:len(secMillisecond)-1])
            timestamp = x['time'].split("T")[1]

            if int(x['value']) > 1000:  ## value is large than 1000, time is inserted 1th location. It is can asure data of arduino and edison same.
                
                edisonEpoch[sec][0] = timestamp
                #print "edison[0]:"+str(edisonEpoch[sec][0])
            elif int(x['value']) < 100:  ## value is large than 1000, time is inserted 2th location 
                
                edisonEpoch[sec][1] = timestamp
                #print "edison[1]:"+str(edisonEpoch[sec][1])
            #print "edison sec"+str(sec) + ":value:"+str(x['value'])+" time:"+str(timestamp)
       
        
        for x in range(0,len(arduinoPeriod)-1):
            period = toMillisecond(str(arduinoPeriod[x+1])) - toMillisecond(str(arduinoPeriod[x]))
            period = period *2 / 1000
            insertPeriodIntoDB(arduinoPeriodDate[x],period)

        
        for x in range(60):
            for y in range(2):
                #print " arduino epoch:"+str(arduinoEpoch[x][y])
                #print " edison  epoch:"+str(edisonEpoch[x][y])
                
                # edison and arduino must be have value
                if edisonEpoch[x][y] != 0 and arduinoEpoch[x][y] != 0: 
                    Atime = toMillisecond(arduinoEpoch[x][y])
                    Etime = toMillisecond(edisonEpoch[x][y])
                    
                    #error = min(abs(Atime - Etime),abs(Atime - Etime2))

                    #print 'arduino:'+str(Atime)+' edison:'+str(Etime)
                    #print 'arduino:'+str(arduinoEpoch[x])+' edison:'+str(edisonEpoch[x])
                    error = abs(Atime - Etime)
                    print error
                    insertDataIntoDB(arduinoDate[x][y],error)
                else:  ## insert 0.0
                    print "xxxx"+str(x)
                    error = 0.0                
        
        time.sleep(4)
        

	    
