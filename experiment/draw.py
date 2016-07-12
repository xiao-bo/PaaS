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
	rect_table = [0.15, 0.2 ,0.8, 0.8]

	legeng_label=['0Mbit','100Mbit','500Mbit','800Mbit']
	##curve
	curve = plt.axes(rect_curve)
	for i in range(0,len(input_list)):
		x = np.linspace(0, len(input_list[i]),len(input_list[i]))
		with plt.style.context('fivethirtyeight'):
	   		line=curve.plot(x,input_list[i])#,label=legeng_label[i])	
			plt.setp(line, linewidth=2)
	'''
	x = np.linspace(0, len(input_list),len(input_list))
	with plt.style.context('fivethirtyeight'):
	   	curve.plot(x,input_list)#,label=legeng_label[i])
	'''
	curve.axes.set_xlabel("sampling")
	curve.axes.set_ylabel("Delay in second")
	curve.axes.set_title(title)
	
	
	#table
	axTable = plt.axes(rect_table, frameon =False)
	axTable.axes.get_xaxis().set_visible(False)
	axTable.axes.get_yaxis().set_visible(False)
	
	table_rows=('0Mbit','100Mbit','500Mbit','800Mbit')
	table_columns = ('Mean', 'Standard_deviation', 'Mean_square_error')
	#cell_text=statistics[0]
	#print statistics
	table_size=axTable.table(cellText=statistics, loc='bottom',
		colLabels=table_columns,rowLabels=table_rows)

	## set table size and font
	table_size.set_fontsize(12)
	table_size.scale(1,1)

	##set legend position
	curve.legend(bbox_to_anchor=(1.05, 1.05))
	
	plt.show()


#def bar(input_list,index,title):

if __name__=="__main__":

	print "draw.py"
	
	timestamp_former=dp.read_file('edison/data/0%.txt',3)##edison receiver
	timestamp_backer=dp.read_file('edison/data/0%.txt',0)##edison sender
	zero_data=dp.data_process_2(timestamp_former,timestamp_backer)

	timestamp_former=dp.read_file('edison/data/20%.txt',3)##edison receiver
	timestamp_backer=dp.read_file('edison/data/20%.txt',0)##edison sender
	ten_data=dp.data_process_2(timestamp_former,timestamp_backer)

	timestamp_former=dp.read_file('edison/data/50%.txt',3)##edison receiver
	timestamp_backer=dp.read_file('edison/data/50%.txt',0)##edison sender
	five_data=dp.data_process_2(timestamp_former,timestamp_backer)

	timestamp_former=dp.read_file('edison/data/90%.txt',3)##edison receiver
	timestamp_backer=dp.read_file('edison/data/90%.txt',0)##edison sender
	nine_data=dp.data_process_2(timestamp_former,timestamp_backer)

	zero_statistics=dp.compute_statistics(zero_data)
	ten_statistics=dp.compute_statistics(ten_data)
	five_statistics=dp.compute_statistics(five_data)
	nine_statistics=dp.compute_statistics(nine_data)
	statistics=[zero_statistics,ten_statistics,five_statistics,
				nine_statistics]
	error_data=[zero_data,ten_data,five_data,nine_data]
	title='Network delay (Mac_receiver-Edison_send)'
	
	'''
	timestamp_former=dp.read_file('arduino/data/0%.txt',2)##edison receiver
	timestamp_backer=dp.read_file('edison/data/0%.txt',0)##edison sender
	zero_data=dp.data_process_2(timestamp_former,timestamp_backer)

	timestamp_former=dp.read_file('arduino/data/20%.txt',2)##edison receiver
	timestamp_backer=dp.read_file('edison/data/20%.txt',0)##edison sender
	ten_data=dp.data_process_2(timestamp_former,timestamp_backer)

	timestamp_former=dp.read_file('arduino/data/50%.txt',2)##edison receiver
	timestamp_backer=dp.read_file('edison/data/50%.txt',0)##edison sender
	five_data=dp.data_process_2(timestamp_former,timestamp_backer)

	timestamp_former=dp.read_file('arduino/data/90%.txt',2)##edison receiver
	timestamp_backer=dp.read_file('edison/data/90%.txt',0)##edison sender
	nine_data=dp.data_process_2(timestamp_former,timestamp_backer)

	zero_statistics=dp.compute_statistics(zero_data)
	ten_statistics=dp.compute_statistics(ten_data)
	five_statistics=dp.compute_statistics(five_data)
	nine_statistics=dp.compute_statistics(nine_data)
	statistics=[zero_statistics,ten_statistics,five_statistics,
				nine_statistics]
	error_data=[zero_data,ten_data,five_data,nine_data]
	title='IP stack(arduino)-edison'
	'''

	
	curve(error_data,title,statistics)