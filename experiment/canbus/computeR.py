def cal(counter):
    l = len(counter)
    print l
    print counter

    R = (l-2)*1000000.0/2
    print R
    tmp = 0.0
    #for x in range(0,l-2):
    x=0
    while x < l-2:
	print counter[x+2] - counter [x]
	tmp += counter[x+2] - counter [x]
	#print tmp
	x=x+2
    print tmp
    R=R/tmp
    print R
    return R
    
def main():
    with open("/home/newslab/Desktop/PaaS/experiment/canbus/data/multiSender/1v3/1.txt") as f:
        	content = f.readlines()

    counterB0 = []
    counterB1 = []
    counterB2 = []
    for x in content:
        if x.split(":")[1]=='0010':
            counterB0.append(int(x.split(":")[3]))
        elif x.split(":")[1]=='0011':
            counterB1.append(int(x.split(":")[3]))
        elif x.split(":")[1]=='0018':
            counterB2.append(int(x.split(":")[3]))

    R0 = cal(counterB0)
    R1 = cal(counterB1)
    R2 = cal(counterB2)
    print "R0:"+str(R0)
    print "R1:"+str(R1)
    print "R2:"+str(R2)
if __name__=='__main__':
    main()

