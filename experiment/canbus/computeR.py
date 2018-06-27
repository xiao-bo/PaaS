def test():
    name =['a','b','c']
    enumerate()

def cal(counter):
    l = len(counter)
    print l
    #print counter

    R = (l-2)*1000000.0/2
    print R
    tmp = 0.0
    #for x in range(0,l-2):
    x=0
    while x < l-2:
	#print counter[x+2] - counter [x]
	tmp += counter[x+1] - counter [x]
	#print tmp
	x=x+1
    print "tmp:"+str(tmp)
    R=R/tmp
    print "R:"+str(R)
    return R
def calwithReceive(counter,receiveTime,x):
    R = 0
    l = len(counter)
    l = 40000
    R = (l-2)*1000000.0/2
    #x = 1
    tmp = 0.0
    while x < l-4:
        tmp = tmp+ counter[x+2]-counter[x]
        x = x+2
        #print "x:{} diff:{}".format(x,counter[x+1]-counter[x])
    elapsedTime = receiveTime[l-1]-receiveTime[0]
    #print elapsedTime
    print tmp
    #R = elapsedTime/tmp
    R=R/tmp
    return R    
def main(dire):
    arduinoRead = open(dire+"offline1.txt",'r')
    #with open("/home/newslab/Desktop/PaaS/experiment/canbus/data/multiSender/1v3/10hz/0%/offline1.txt") as f:

    counterB0 = []
    counterB1 = []
    counterB2 = []
    receiveB0 = []
    receiveB1 = []
    receiveB2 = []
    for x in arduinoRead:
        ID = x.split(":")[1]
        if ID == '0010':
            counterB0.append(float(x.split(":")[3]))
            receiveB0.append(float(x.split(":")[9]))
        elif ID =='0011':
            counterB1.append(float(x.split(":")[3]))
            receiveB1.append(float(x.split(":")[9]))
        elif ID =='0018':
            counterB2.append(float(x.split(":")[3]))
            receiveB2.append(float(x.split(":")[9]))
    print len(counterB1)
    print len(receiveB1)
    #R0 = calwithReceive(counterB0,receiveB0)
    #R1 = calwithReceive(counterB1,receiveB1)
    R2_1023 = calwithReceive(counterB2,receiveB2,1)
    R2_0 = calwithReceive(counterB2,receiveB2,0)

    #R0 = cal(counterB0)
    #R1 = cal(counterB1)
    #R2 = cal(counterB2)
    #print "R0:"+str(R0)
    #print "R1:"+str(R1)
    print "R2_1023:{}".format(R2_1023)
    print "R2_0:{}".format(R2_0)
if __name__=='__main__':
    dire = "/home/newslab/Desktop/PaaS/experiment/canbus/data/multiSender/1v3/1hz/longdata/0%/test3/"
    main(dire)
