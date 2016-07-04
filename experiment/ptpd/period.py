
import sys
<<<<<<< HEAD
=======
sys.path.insert(0,'/home/newslab/Desktop/PaaS/experiment')
import draw
>>>>>>> 6bd1f662aa06819929c5e35cb578604aed6429dd
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
