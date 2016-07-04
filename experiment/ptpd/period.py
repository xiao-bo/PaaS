
import sys
sys.path.insert(0,'/home/newslab/Desktop/PaaS/experiment')
import draw
def period(filename):
	readline=open(filename,"rb")
	offset=[]
	for x in readline:
                tmp=x.replace(" ","")
                tmp=tmp.split(":")[1]
                tmp=tmp.split("s")[0]
		offset.append(float(tmp)*1000)
	return offset


if __name__=="__main__":
	offset=period("data.txt")
	print offset
        #draw.curve(offset)
