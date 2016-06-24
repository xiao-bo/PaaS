
import sys
sys.path.insert(0,'/Users/xiao/Documents/code/paas/git/PaaS/experiment')
import draw
def period(filename):
	readline=open(filename,"rb")
	offset=[]
	for x in readline:
		ans=x.split(":")[1]
		ans=ans.split("s")[0]
		offset.append(ans)
	return offset


if __name__=="__main__":
	offset=period("data.txt")
	draw.ptp_curve(offset)
