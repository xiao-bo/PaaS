
def getData():
    fileRead = open('2.txt','r')
    
    fc = open('cpUtility.txt','w')
    fo = open('optimalUtility.txt','w')
    fd = open('diffUtility.txt','w')
    
    for line in fileRead:
        ans = line.split(":")
        fo.write(str(float(ans[1]))+'\n')
        fc.write(str(float(ans[3]))+'\n')
        fd.write(str(float(ans[5]))+'\n')
if __name__ == '__main__':
   
    getData()
