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
    
    ## transform epochTime into 
    ## Year-Month-Day Hour-minute-second-millisceond
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



if __name__ == "__main__":
    
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example3')
    #client.create_database('example3')
    #result = client.query('select * from cos where time > now() + 7h + 59m' and time )
    counter = 1
    while counter>0:
        counter +=1
        result = client.query('SELECT * FROM "arduino" WHERE time > now() - 1m  and time < now();')
        result2 = client.query('SELECT * FROM "edison" WHERE time > now() - 1m  and time < now();')
        arduino = list(result.get_points())
        edison = list(result2.get_points())
        #print("Result: {0}".format(result))
        #data=list(result.get_points(measurement='arduino'))

        #print data[0]['host']
        arduinoDate=[]
        arduinoEpoch=[]
        edisonDate=[]
        edisonEpoch=[]
        for x in range(0,120):
            arduinoDate.append(0)
            edisonDate.append(0)
            arduinoEpoch.append(0)
            edisonEpoch.append(0)
	    
        for x in arduino:
            secMillisecond = x['time'].split(":")[2]  ## select sec+millisecond
            sec = int(secMillisecond.split(".")[0])
            secMillisecond = float(secMillisecond[:len(secMillisecond)-1])
            clock = x['time'].split("T")[1]
            if int(x['value']) > 1000:  ## value is large than 1000, time is inserted 1th location. It is can asure data of arduino and edison same.
                arduinoDate[2*sec] = x['time']
                arduinoEpoch[2*sec] = clock

            elif int(x['value']) < 100:  ## value is large than 1000, time is inserted 2th location 
                 arduinoDate[2*sec+1] = x['time']
                 arduinoEpoch[2*sec+1] = clock
            #print "arduino sec"+str(sec) + ":value:"+str(x['value'])+" time:"+str(clock)
        for x in edison:           
            secMillisecond = x['time'].split(":")[2]  ## select sec+millisecond
            sec = int(secMillisecond.split(".")[0])
            secMillisecond = float(secMillisecond[:len(secMillisecond)-1])
            clock = x['time'].split("T")[1]

            if int(x['value']) > 1000:  ## value is large than 1000, time is inserted 1th location. It is can asure data of arduino and edison same.
                edisonDate[2*sec] = x['time']
                edisonEpoch[2*sec] = clock
            elif int(x['value']) < 100:  ## value is large than 1000, time is inserted 2th location 
                edisonDate[2*sec+1] = x['time']
                edisonEpoch[2*sec+1] = clock
            #print "edison sec"+str(sec) + ":value:"+str(x['value'])+" time:"+str(clock)
            #print x
            
        
        for x in range(0,120):
            #print "arduinoDate:"+str(arduinoDate[x])
            #print "edisonDate:"+str(edisonDate[x])
            if edisonDate[x] != 0 and arduinoDate[x] != 0:
                Atime = toMillisecond(arduinoEpoch[x])
                Etime = toMillisecond(edisonEpoch[x])
                error = abs(Atime - Etime)
                insertDataIntoDB(arduinoDate[x],error)
            else:
                error = 0.0
        #print "\n\n\n\n\n\n\n\n\n\n\n\n"
        # insert DB with timestamp (Date) error value    
        time.sleep(1)


	    
