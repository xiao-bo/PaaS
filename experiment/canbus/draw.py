"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import data_processing as dp
import matplotlib.patches as mpatches




def curve(input_list,title,statistics):	
	output_list=[]
	
	##set subplot position 
	rect_curve = [0.1, 0.3, 0.8, 0.6]#left,bottom,width,height
	rect_table = [0.1, 0.2 ,0.8, 0.8]

	##curve
	curve = plt.axes(rect_curve)
	x = np.linspace(0, len(input_list),len(input_list))
	with plt.style.context('fivethirtyeight'):
	    line=curve.plot(x,input_list)	
	    plt.setp(line, linewidth=2)
	curve.axes.set_xlabel("sampling")
	curve.axes.set_ylabel("Delay in Millisecond")
	curve.axes.set_title(title)
        plt.ylim([5,40])
        font = {'family' : 'normal',
                'weight' : 'bold',
                'size'   : 28}
        plt.rc('font',**font)
	
	#table
	axTable = plt.axes(rect_table, frameon =False)
	axTable.axes.get_xaxis().set_visible(False)
	axTable.axes.get_yaxis().set_visible(False)
	
	table_columns = ('Mean', 'Standard Deviation')
        cell_text=statistics
        
	table_size=axTable.table(cellText=statistics, loc='bottom',
		colLabels=table_columns)

	## set table size and font
	table_size.set_fontsize(40)
	table_size.scale(1.2,3)

	
	plt.show()
def multicurve(input_list,title,statistics):	
	output_list=[]
	
	##set subplot position 
	rect_curve = [0.1, 0.3, 0.8, 0.6]#left,bottom,width,height
	rect_table = [0.15, 0.2 ,0.8, 0.8]

	legeng_label=['0Mbit','100Mbit','500Mbit','800Mbit']
	##curve
	curve = plt.axes(rect_curve)
	for i in range(0,len(input_list)):
		x = np.linspace(0, len(input_list[i]),len(input_list[i]))
		with plt.style.context('fivethirtyeight'):
	   		line=curve.plot(x,input_list[i])#,label=legeng_label[i])	
			plt.setp(line, linewidth=2)
	curve.axes.set_xlabel("sampling")
	curve.axes.set_ylabel("Delay in milliSecond")
	curve.axes.set_title(title)
	
	
	#table
	axTable = plt.axes(rect_table, frameon =False)
	axTable.axes.get_xaxis().set_visible(False)
	axTable.axes.get_yaxis().set_visible(False)
	
	table_rows=('0Mbit','100Mbit','500Mbit','800Mbit')
	table_columns = ('Mean', 'Standard_deviation')
        cell_text=statistics
        
	table_size=axTable.table(cellText=statistics, loc='bottom',
		colLabels=table_columns,rowLabels=table_rows)

	## set table size and font
	table_size.set_fontsize(12)
	table_size.scale(1,1)

	##set legend position
	curve.legend(bbox_to_anchor=(1.05, 1.05))
	
	plt.show()



if __name__=="__main__":
        ## main code for multicurve

	print "draw.py"
	
        timestamp_former=dp.read_file('/home/newslab/Desktop/PaaS/experiment/canbus/data/dataRate500kbits/Wave500mHz/twoNodeNetwork/otherNodeAt500mHz/SyncWithHighestPriority/Edison.txt',1)##edison sender
	timestamp_backer=dp.read_file('/home/newslab/Desktop/PaaS/experiment/canbus/data/dataRate500kbits/Wave500mHz/twoNodeNetwork/otherNodeAt500mHz/SyncWithHighestPriority/Arduino.txt',5)##arduino sender
	
        #timestamp_former=dp.read_file('/home/newslab/Desktop/PaaS/experiment/canbus/data/dataRate500kbits/Wave500mHz/oneNodeNetwork/edison.txt',1)##edison sender
	#timestamp_backer=dp.read_file('/home/newslab/Desktop/PaaS/experiment/canbus/data/dataRate500kbits/Wave500mHz/oneNodeNetwork/arduino.txt',5)##arduino sender
	
        zero_data=dp.data_process_2(timestamp_former,timestamp_backer)
        
        #title = '1NodeNetworkSamplingErrorBetweenArduinoAndEdisonAt500mHz'
        title = ''
        #title = '2NodeNetworkSamplingErrorBetweenArduinoAndEdisonWithHighestPriorityAt500mHz,other500mHz'
        
	zero_statistics=dp.compute_statistics(zero_data)
        
        curve(zero_data,title,[zero_statistics])
