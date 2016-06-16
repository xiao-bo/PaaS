
import sys
sys.path.insert(0,'/Users/xiao/Documents/code/paas/git/PaaS/experiment')
import draw
readline=open("data.txt","rb")
offset=[]
for x in readline:
	ans=x.split(":")[1]
	ans=ans.split("s")[0]
	offset.append(ans)

print offset
draw.ptp_curve(offset)
