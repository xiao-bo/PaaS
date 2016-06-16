"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
def ptp_curve(input_list):
	x = np.linspace(0, len(input_list),len(input_list))		
	with plt.style.context('fivethirtyeight'):
	    plt.plot(x,input_list)
	title='ptpd'
	plt.title(title)
	plt.xlabel('Number of data')
	plt.ylabel('Delay in second')
	plt.show()
def curve(input_list,index):

	x = np.linspace(0, len(input_list[index]),len(input_list[index]))	

	with plt.style.context('fivethirtyeight'):
	    plt.plot(x,input_list[index])
	if index==0:
		title='Arduino-Edison'
	elif index==1:
		title='Arduino-Serial'
	elif index==2:
		title='Edison-Serial'
	elif index==3:
		title='Edison_receiver-send'
	plt.title(title)
	plt.xlabel('Number of data')
	plt.ylabel('Delay in second')
	plt.show()
	
if __name__=="__main__":
	
	curve(int(sys.argv[1]))
	
