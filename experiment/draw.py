"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import data_processing as dp
def curve(input_list,title,statistics):	
	output_list=[]
	
	##set subplot position 
	rect_curve = [0.1, 0.2, 0.8, 0.7]#left,bottom,width,height
	rect_table = [0.1, 0.1 ,0.8, 0.8]

	##curve
	curve = plt.axes(rect_curve)
	for i in range(0,4):
		x = np.linspace(0, len(input_list[i]),len(input_list[i]))	
		with plt.style.context('fivethirtyeight'):
	   		curve.plot(x,input_list[i])

	curve.axes.set_xlabel("sampling")
	curve.axes.set_ylabel("Delay in second")
	curve.axes.set_title(title)
	
	#table
	axTable = plt.axes(rect_table, frameon =False)
	axTable.axes.get_xaxis().set_visible(False)
	axTable.axes.get_yaxis().set_visible(False)
	
	columns = ('Mean', 'Standard_deviation', 'Mean_square_error')
        cell_text=statistics
        
	table_size=axTable.table(cellText=statistics, loc='bottom',
		colLabels=columns)

	## set table size and font
	table_size.set_fontsize(14)
	table_size.scale(1.2,1.2)
	
	
	plt.show()


#def bar(input_list,index,title):

if __name__=="__main__":

	print "draw.py"
	timestamp_former=dp.read_file('edison/0%.txt',3)##edison receiver
	timestamp_backer=dp.read_file('edison/0%.txt',0)##edison sender
	zero_data=dp.data_process_2(timestamp_former,timestamp_backer)

	timestamp_former=dp.read_file('edison/10%.txt',3)##edison receiver
	timestamp_backer=dp.read_file('edison/10%.txt',0)##edison sender
	ten_data=dp.data_process_2(timestamp_former,timestamp_backer)

	timestamp_former=dp.read_file('edison/50%.txt',3)##edison receiver
	timestamp_backer=dp.read_file('edison/50%.txt',0)##edison sender
	five_data=dp.data_process_2(timestamp_former,timestamp_backer)

	timestamp_former=dp.read_file('edison/90%.txt',3)##edison receiver
	timestamp_backer=dp.read_file('edison/90%.txt',0)##edison sender
	nine_data=dp.data_process_2(timestamp_former,timestamp_backer)

	statistics=[dp.compute_statistics(zero_data)]
	error_data=[zero_data,ten_data,five_data,nine_data]
	title='Network delay (Mac_receiver-Edison_send)'
	curve(error_data,title,statistics)
