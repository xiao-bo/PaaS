"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def curve(input_list,title):	
	output_list=[]
	x = np.linspace(0, len(input_list),len(input_list))	
	with plt.style.context('fivethirtyeight'):
	    ax1=plt.plot(x,input_list)
	##curve
	'''
	x = np.linspace(0, len(input_list),len(input_list))	
	with plt.style.context('fivethirtyeight'):
	    ax1=plt.plot(x,input_list)
	'''
	##table
	'''
	columns = ('Mean', 'Standard_deviation', 'Mean_square_error')
	cell_text=statistics
	the_table = plt.table(cellText=cell_text,
                      #colWidths = [0.3]*3,
                      colLabels=columns)
                      #loc='top')
	'''
	plt.title(title)
	plt.xlabel('sampling')
	plt.ylabel('Delay in millisecond')
	plt.show()


#def bar(input_list,index,title):

if __name__=="__main__":

	print "draw.py"
