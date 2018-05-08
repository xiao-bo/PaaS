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
	curve.axes.set_ylabel("Error in Millisecond")
	curve.axes.set_title(title)
        plt.ylim([0,40])
        font = {'family' : 'normal',
                'weight' : 'bold',
                'size'   : 24}
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
	curve.axes.set_ylabel("error in milliSecond")
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
	
        Etimestamp=dp.ReadEdisonFile('/home/newslab/Desktop/PaaS/experiment/canbus/data/multiSender/1v3/edison_all.txt',1)##edison sender
	
        S0timestamp,S1timestamp,S2timestamp=dp.ReadArduinoFile('/home/newslab/Desktop/PaaS/experiment/canbus/data/multiSender/1v3/3.txt',7)##arduino sender
        print Etimestamp
        '''
        '''
        ES0data=dp.dataProcess(Etimestamp,S0timestamp)
        ES0title = '1hz,500kbit/s,1vs3,no background,ES0'
	ES0statistics=dp.compute_statistics(ES0data) 
        print ES0data
        curve(ES0data,ES0title,[ES0statistics])
        
        ES1data=dp.dataProcess(Etimestamp,S1timestamp)
        ES1title = '1hz,500kbit/s,1vs3,no background,ES1'
	ES1statistics=dp.compute_statistics(ES1data) 
        curve(ES1data,ES1title,[ES1statistics])

        ES2data=dp.dataProcess(Etimestamp,S2timestamp)
        ES2title = '1hz,500kbit/s,1vs3,no background,ES2'
	ES2statistics=dp.compute_statistics(ES2data) 
        curve(ES2data,ES2title,[ES2statistics])
