
import sys
def period(filename):
	readline=open(filename,"rb")
	offset=[]
	for x in readline:
		ans=x.replace(" ","")
		
		ans=ans.split(":")[1]
		ans=ans.split("s")[0]
		offset.append(float(ans))
	return offset


if __name__=="__main__":
	offset=period("data.txt")
	print offset
