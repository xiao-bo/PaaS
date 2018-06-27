
from decimal import Decimal
import data_processing as dp

def checkEdisonReadTwice(dire):
    
    fileRead = open(dire+"edison.txt",'r')
    Etime = []
    value = []
    for line in fileRead:
        ans = line.split(":")
        Etime.append(float(ans[1]))
        value.append(int(ans[0]))
    
    ## print  number of line about jitter and remove jitter
    fo = open(dire+'edisonRT.txt','w')
    for x in range(1,len(Etime)-1):
        if Etime[x]-Etime[x-1]<0.1:
            print x
            continue
        ## print  number of line about jitter and remove jitter
        fo.write(str(value[x])+":"+str(Decimal(Etime[x]))+"\n")

def checkDataAlignment(dire):
    fileRead = open(dire+'1.txt','r')
    fileRead2 = open(dire+'offline2.txt','r')
    fo = open(dire+'delay.txt','w')
    S1time = []
    S2time = []
    for line in fileRead:
        ans = line.split(":")
        S1time.append(float(ans[7]))
    for line in fileRead2:
        ans = line.split(":")
        S2time.append(float(ans[7]))
     
    for x in range(0,8000):
        delay = S1time[x]-S2time[x]
        #print delay
        if delay != 0.0 :
            print delay
def checkDelayTime(dire):
    fileRead = open(dire+'offline2.txt','r')
    fo = open(dire+'delay.txt','w')
    Rtime = []
    Stime = []
    change = 1
    tmp = 1
    for line in fileRead:
        ans = line.split(":")
        Rtime.append(float(ans[9]))
        Stime.append(float(ans[7]))
    for x in range(0,len(Rtime)):
        delay = 1000*(Rtime[x]-Stime[x])
        if delay > 0 :
            change = 1
        elif delay <0:
            change = -1
        if tmp != change:
            print "======="+str(x)
            tmp = change
            print x
        fo.write(str(delay)+"\n")

def checkCounter(dire):
    value = '0010.txt'
    value = '0011.txt'
    value = '0018.txt'
    oRead = open(dire+'offline'+value,'r')
    fo = open(dire+'counter'+value,'w')
    counter = []
    for line in oRead:
        ans = line.split(":")
        counter.append(float(ans[3]))
    interval = 100
    for x in range(len(counter)-interval):
        if x % interval ==0:
            cdiff = counter[x+interval]-counter[x]
            print "x+interval:{},x:{}".format(x+interval,x)
            fo.write(str(x+interval)+"-"+str(x)+":c:"+str(cdiff-50000000)+"\n")

def getDatatime(dire):
     
    eRead = open(dire+'edison_1023.txt','r')
    oRead = open(dire+'offline2.txt','r')
    fo = open(dire+'rtime.txt','w')
    oRtime = []
    oStime = []
    counter = []
    Etime = []
    for line in oRead:
        ans = line.split(":")
        counter.append(float(ans[3]))
        oRtime.append(float(ans[9]))
        oStime.append(float(ans[7]))
    for line in eRead:
        ans = line.split(":")
        Etime.append(float(ans[1]))
    interval = 1
    for x in range(len(oRtime)-interval):
        if x >=0:
            #cdiff = counter[x+interval]-counter[x]-1000000
            #oSdiff = 1000*(oStime[x+interval]-oStime[x])
            oRdiff = 1000*(oRtime[x+interval]-oRtime[x]-1.0)
            Ediff = 1000*(Etime[x+interval]-Etime[x]-1.0)
            #fo.write(str(x+2)+"000-"+str(x+1)+"000:c:"+str(cdiff)+"\n")
            fo.write("ord:"+str(oRdiff))
            fo.write(":esd:"+str(Ediff)+"\n")
            #fo.write(":etime:"+str(Decimal(Etime[x]))+"\n")
            #fo.write(":sd:"+str(Decimal(oSdiff)))
            #fo.write("x:"+str(x)+":S:"+str(Decimal(oStime[x])))
            #fo.write(":R:"+str(Decimal(oRtime[x]))+"\n")

def getEdison0or1023(dire):
    fileRead = open(dire+'edison.txt','r')
    fo_1023 = open(dire+'edison_1023.txt','w')
    fo_0 = open(dire+'edison_0.txt','w')
    E0 = []
    E1023 = []
    for line in fileRead:
        ans = line.split(":")
        if ans[0] == '0':
            fo_0.write(line)
        elif ans[0] == '1023':
            fo_1023.write(line)

    
def fixOverflow(dire):
    
    filename = dire+'1.txt'
    fo = open(dire+'offline1.txt','w')

    S0counter,S1counter,S2counter = dp.ReadArduinoFile(filename,3)
    S0value,S1value,S2value = dp.ReadArduinoFile(filename,5)
    S0Rtime,S1Rtime,S2Rtime = dp.ReadArduinoFile(filename,9)
    S0Stime,S1Stime,S2Stime = dp.ReadArduinoFile(filename,7)

    ## S0
    length = len(S0counter)
    S0index = [] 
    S0overCount = 0
    for x in range(length-1):
        if S0counter[x]-S0counter[x+1] > 1000000:
            print x        
            S0index.append(x+1)
            #print "S0[{}]:{} S0[{}]:{}".format(x,S0counter[x],x+1,S0counter[x+1])
    #S0counter[index] = S0counter[index]+4294967295.0 * overCount
    S0index.append(length)
    print len(S0index)
    for x in range(length-1):
        if x == S0index[S0overCount]:
            S0overCount = S0overCount + 1
            print "x:{},count:{}".format(x,S0overCount)
        S0counter[x] = S0counter[x]+4294967295.0 * S0overCount
    for x in range(length-1):
        fo.write("ID:0010:c21:"+str(S0counter[x])+":value:"+str(S0value[x])+":time:"+str(Decimal(S0Stime[x]))+":receiveT1:"+str(Decimal(S0Rtime[x]))+"\n")

    ##S1
    length = len(S1counter)
    S1index = [] 
    S1overCount = 0
    for x in range(length-1):
        if S1counter[x]-S1counter[x+1] > 1000000:
            print x        
            S1index.append(x+1)
    S1index.append(length)
    print len(S1index)
    for x in range(length-1):
        if x == S1index[S1overCount]:
            S1overCount = S1overCount + 1
            print "x:{},count:{}".format(x,S1overCount)
        S1counter[x] = S1counter[x]+4294967295.0 * S1overCount
    for x in range(length-1):
        fo.write("ID:0011:c21:"+str(S1counter[x])+":value:"+str(S1value[x])+":time:"+str(Decimal(S1Stime[x]))+":receiveT1:"+str(Decimal(S1Rtime[x]))+"\n")
    ###s2
    length = len(S2counter)
    S2index = [] 
    S2overCount = 0
    for x in range(length-1):
        print x        
        if S2counter[x]-S2counter[x+1] > 1000000:
            print x        
            S2index.append(x+1)
    S2index.append(length)
    print len(S2index)
    for x in range(length-1):
        print x        
        if x == S2index[S2overCount]:
            S2overCount = S2overCount + 1
            print "x:{},count:{}".format(x,S2overCount)
        S2counter[x] = S2counter[x]+4294967295.0 * S2overCount

    for x in range(length-1):
        fo.write("ID:0018:c21:"+str(S2counter[x])+":value:"+str(S2value[x])+":time:"+str(Decimal(S2Stime[x]))+":receiveT1:"+str(Decimal(S2Rtime[x]))+"\n")

if __name__ == '__main__':
    dire = '/home/newslab/Desktop/PaaS/experiment/canbus/data/1v3/1hz/35%/'
    #fixOverflow(dire)
    #checkEdisonReadTwice(dire)
    #getEdison0or1023(dire)
    #getDatatime(dire)
    checkCounter(dire)
    #checkDelayTime(dire)
    #checkDataAlignment(dire)
