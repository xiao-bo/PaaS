
import data_processing as dp
import ast
from decimal import Decimal
def calculateAfterTime(oldc21,currentc21,oldT1,R):
    currentc21 = Decimal(currentc21)
    oldc21 = Decimal(oldc21)
    R = Decimal(R) * Decimal(0.000001)
    oldT1 = Decimal(oldT1)
    
    #print(Decimal(0.0000133)/Decimal(hz))
    #print "x = {} current c21 {} - oldc21 {} = {}".format(x,currentc21,oldc21,(currentc21-oldc21)*R)
    currentT1 = oldT1 + (currentc21 - oldc21) * R 
    #print "x = {} c21-old {} R*(c21-old)= {}".format((x+1)/2,(currentc21-oldc21),(currentc21-oldc21)*R)
    #print "calculateAfterTime oldc21:"+str(oldc21)+" current21 "+str(c21)+" oldT1:"+str(oldT1)+"new:"+str(currentT1)
    return currentT1,R

def sync(T2,T3,C21,C22,C23,R):
    T2 = Decimal(T2)
    T3 = Decimal(T3)
    C21 = Decimal(C21)
    C22 = Decimal(C22)
    C23 = Decimal(C23)

    R = Decimal(R) * Decimal(0.000001)
    if C23-C22 ==0:
        C23 = C22+4
    delay = ((T3 - T2) - (C23 - C22) * R) / 2
    #delay = Decimal(0.0004)
    T1 = T3 - delay - (C23 - C21) * R
    '''
    print ("C21:"+str(C21))
    print ("C22:"+str(C22))
    print ("C23:"+str(C23))
    print ("T2:"+str(T2))
    print ("T3:"+str(T3))
    print ("R:"+str(R))
    print ("R*(C23-C21): "+str((C23-C21)*R))
    print ("R*(C23-C22): "+str((C23-C22)*R))
    print ("T3-T2:"+str(T3-T2))
    print ("delay = ((T3-T2)-(C23-C22)*R)/2 = "+str(delay))
    print ("R= "+str(R))
    print ("actual T1 = T3 - delay - (C23-C21) * R =  "+str(T1))
    print ("sync") 
    '''
    return T1

if __name__=='__main__':

    S0Stime = []
    S1Stime = []
    S2Stime = []
    ## 1hz
    
    dire = '/home/newslab/Desktop/PaaS/experiment/canbus/data/1v3/10hz/0%another/'
    
    #dire = '/home/newslab/Desktop/PaaS/experiment/canbus/data/1v3/10hz/95%/'
    dire = '/home/newslab/Desktop/PaaS/experiment/canbus/data/1v3/1hz/0%/long/'
    
    filename = 'offline0018.txt'
    filename = dire+filename
    
    S0value,S1value,S2value = dp.ReadArduinoFile(filename,5)
    S0Rtime,S1Rtime,S2Rtime = dp.ReadArduinoFile(filename,9)
    S0counter,S1counter,S2counter = dp.ReadArduinoFile(filename,3)
    
    
    
    ReadS0SyncData = open(dire+'0010.txt','r')
    ReadS1SyncData = open(dire+'0011.txt','r')
    ReadS2SyncData = open(dire+'0018.txt','r')

    s0 ={'oldc21':0,'actualT1':0,'R':0,'shift':0,'hz':0,'t2':0,'t3':0,'c22':0}
    s1 ={'oldc21':0,'actualT1':0,'R':0,'shift':0,'hz':0,'t2':0,'t3':0,'c22':0}
    s2 ={'oldc21':0,'actualT1':0,'R':0,'shift':0,'hz':0,'t2':0,'t3':0,'c22':0}
    for line in ReadS0SyncData:
        ans = line.split(":")
        s0['ID'] = '0010'
        s0['oldc21'] = int(ans[3])
        s0['actualT1'] = float(ans[5])
        s0['R'] = float(ans[7])
        s0['shift'] = int(ans[9])
        s0['hz'] = int(ans[11])
        s0['t2'] = Decimal(ans[13])
        s0['t3'] = Decimal(ans[15])
        s0['c22'] = int(ans[17])
        s0['actualT1'] = sync(s0['t2'],s0['t3'],s0['oldc21'],s0['c22'],s0['c22'],s0['R'])
    for line in ReadS1SyncData:
        ans = line.split(":")
        s1['ID'] = '0011'
        s1['oldc21'] = int(ans[3])
        s1['actualT1'] = float(ans[5])
        s1['R'] = float(ans[7])
        #s1['R']= 1.00015839496
        s1['shift'] = int(ans[9])
        s1['hz'] = int(ans[11])
        s1['t2'] = Decimal(ans[13])
        s1['t3'] = Decimal(ans[15])
        s1['c22'] = int(ans[17])
        s1['actualT1'] = sync(s1['t2'],s1['t3'],s1['oldc21'],s1['c22'],s1['c22'],s1['R'])
    for line in ReadS2SyncData:
        ans = line.split(":")
        s2['ID'] = '0018'
        s2['oldc21'] = int(ans[3])
        s2['R'] = float(ans[7])
        s2['shift'] = int(ans[9])
        s2['hz'] = int(ans[11])
        s2['t2'] = Decimal(ans[13])
        s2['t3'] = Decimal(ans[15])
        s2['c22'] = int(ans[17])
        s2['actualT1'] = sync(s2['t2'],s2['t3'],s2['oldc21'],s2['c22'],s2['c22'],s2['R'])
    
    ## S0
    '''
    value = '0.txt'
    value = '1023.txt'
    #value = 'all.txt'
    fo0010 = open(dire+'offline0010_'+value,'w')
    z = 0
    #s0['R'] = 0.9995558414 #for 95%
    
    print s0['R']
    s0['actualT1'] = sync(s0['t2'],s0['t3'],s0['oldc21'],s0['c22'],s0['c22'],s0['R'])
    for x in range(0,30000):
        if S0value[x]==0.0: 
            ## for 6 dasy data
            #print x
            r = 1
            continue
        elif S0value[x]==1023.0:
            r = 1
            #continue
            #s0['R'] = 1.00020020414
        ## for 10hz, 95% data
        if x> 8000 and x < 16000:
            s0['R'] = 0.9995488414
        elif x >= 16000 and x <= 20000:
            s0['R'] = 0.9995458414
        elif x >= 20000 and x<=24000:
            s0['R'] = 0.9995428414
        elif x >= 24000 :
            s0['R'] = 0.9995408414
        st0,R=calculateAfterTime(s0['oldc21'],S0counter[x],s0['actualT1'],s0['R'])
        S0Stime.append(st0)
        fo0010.write("ID:"+str(s0['ID'])+":c21:"+str(S0counter[x])+":value:"+str(S0value[x])+":time:"+str(S0Stime[z])+":receiveT1:"+str(Decimal(S0Rtime[x]))+"\n")

        z = z+1 
    '''

    '''

    ## S1
    #value = '0.txt'
    value = '1023.txt'
    #value = 'all.txt'
    fo0011 = open(dire+'offline0011_'+value,'w')
    z = 0
    #s1['R'] = 1.00019800414## for 10hz 95%
    print s1['R']
    s1['actualT1'] = sync(s1['t2'],s1['t3'],s1['oldc21'],s1['c22'],s1['c22'],s1['R'])
    for x in range(0,30000):#len(S1value)-1):
        if S1value[x]==0.0: 
            ## for 6 day data
            r = 1
            continue
        elif S1value[x]==1023.0:
            r = 1
            #continue
        ## for 10hz,95% data
        if x> 22000 and x <30000:
            s1['R'] = 1.00019000414
        ## for 1hz 35% data
        if x> 0 and x <7000:
            s1['R'] = 1.00015900414
        elif x >= 7000 and x<11000:
            s1['R'] = 1.00015700414
        elif x >= 11000 and x < 12000:
            s1['R'] = 1.00015850414
        elif x >= 12000 and x < 13000:
            s1['R'] = 1.00015950414
        elif x >= 13000 :
            s1['R'] = 1.00015990414
        st1,R=calculateAfterTime(s1['oldc21'],S1counter[x],s1['actualT1'],s1['R'])
        S1Stime.append(st1)
        fo0011.write("ID:"+str(s1['ID'])+":c21:"+str(S1counter[x])+":value:"+str(S1value[x])+":time:"+str(S1Stime[z])+":receiveT1:"+str(Decimal(S1Rtime[x]))+"\n")

        z = z+1
    '''
    ## S2
    z = 0
    #value = '0.txt'
    value = '1023.txt'
    #value = 'all.txt'
    
    #s2['R'] =  1.00029430416
    s2['actualT1'] = sync(s2['t2'],s2['t3'],s2['oldc21'],s2['c22'],s2['c22'],s2['R'])
    print s2['R']
    fo0018 = open(dire+'offline0018_'+value,'w')
    for x in range(0,30000):#len(S2value)-2000):
        if S2value[x]==0.0: 
            ## for 6 day data
            r = 1
            continue
        elif S2value[x]==1023.0:
            r = 1 
            #continue
        '''
        
        ### for 10hz, 95% data
        if x> 16000 and x <20000:
            s2['R'] = 1.00028830416
        elif x >= 20000 and x<24000:
            s2['R'] = 1.00028530416
        elif x >= 24000 and x<30000:
            s2['R'] = 1.00028330416
        ## for 35% data
        if x> 0 and x <6000:
            s2['R'] = 1.00025130416
        elif x >= 6000 and x<7000:
            s2['R'] = 1.00024930416
        elif x >= 7000 and x<11000:
            s2['R'] = 1.00024830416
        elif x >= 11000 and x<12000:
            s2['R'] = 1.00024930416
        '''
        st2,R=calculateAfterTime(s2['oldc21'],S2counter[x],s2['actualT1'],s2['R'])
        S2Stime.append(st2)
        fo0018.write("ID:"+str(s2['ID'])+":c21:"+str(S2counter[x])+":value:"+str(S2value[x])+":time:"+str(S2Stime[z])+":receiveT1:"+str(Decimal(S2Rtime[x]))+"\n")
        z = z+1 





