
##### use python2.7 to urn
import time
import grovepi

#Sensor connected to A0 Port 
sensor = 16    # Pin 14 is A0 Port.
grovepi.pinMode(sensor,"INPUT")
change = 0
while True:
    try:
        sensorValue = grovepi.analogRead(sensor)
        if sensorValue !=change and (sensorValue==0 or sensorValue==1023):
            t = time.time()
            change = sensorValue
            print ("sensorValue:{}  time:{}".format(sensorValue,t))
        time.sleep(0.1)
    except IOError:
        print ("Error")
