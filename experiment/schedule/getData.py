
def getData():
    dire = 'under/'
    fileRead = open(dire+'10.txt','r')
    
    ft = open(dire+'totalUtility.txt','w')
    fo = open(dire+'optimalUtility.txt','w')
    fc = open(dire+'cpUtility.txt','w')
    fd = open(dire+'diffUtility.txt','w')
    fa = open(dire+"c.txt",'w')
    count = 0
    same = 0
    diff = 0
    x = 0
    for line in fileRead:
        ans = line.split(":")
        #print ans
        ft.write(str(float(ans[1]))+'\n')
        fo.write(str(float(ans[3]))+'\n')
        fc.write(str(float(ans[5]))+'\n')
        fd.write(str(float(ans[7]))+'\n')
        fa.write(str(x)+'\n')
        if float(ans[7])<0:
            count = count +1
        if float(ans[1])==float(ans[3]):
            same = same +1
            print x+1
        if float(ans[7])==0.0:
            diff = diff+1
        x = x +1
        if x >70000:
            break
    print "number of difference <0 {}".format(count)
    print "optimal = total {}".format(same)
    print "number of difference =0 {}".format(diff)
if __name__ == '__main__':
   
    getData()
