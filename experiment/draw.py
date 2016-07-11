"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def curve(input_list,title,statistics):	
	output_list=[]
	
	##set subplot position 
	rect_curve = [0.1, 0.2, 0.8, 0.7]#left,bottom,width,height
	rect_table = [0.1, 0.1 ,0.8, 0.8]

	##curve
	curve = plt.axes(rect_curve)
	x = np.linspace(0, len(input_list),len(input_list))	
	with plt.style.context('fivethirtyeight'):
	   	curve.plot(x,input_list)

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
