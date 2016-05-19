import mraa
import sys
import time
pot=mraa.Aio(0)
while 1:
    potVal = float(pot.read())
    print potVal
    #time.sleep(0.1)
