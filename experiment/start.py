import data_processing as dp
import draw
import sys
if __name__=="__main__":
	data=dp.data_process()
	index=int(sys.argv[1])
	draw.curve(data[0],index)
