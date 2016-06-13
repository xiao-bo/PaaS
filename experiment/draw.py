"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import data_processing as dp
def box():
	n_groups = 3
	input_list=dp.data_process()
	#print input_list[4][0]
	means_men = (input_list[4][0], input_list[4][1], input_list[4][2])
	std_men = (0.001, 0.001, 0.001)
	fig, ax = plt.subplots()

	index = np.arange(n_groups)
	#print index
	bar_width = 0.35

	opacity = 0.4
	error_config = {'ecolor': '0.3'}

	rects1 = plt.bar([0,1,2], means_men, bar_width,
    	             alpha=opacity,
					 color='b',
            	     yerr=std_men,
                	 error_kw=error_config
                 	)
	plt.xlabel('')
	plt.ylabel('average(ms)')
	plt.title('')
	plt.xticks(index + bar_width, ('A-E', 'A-S ',
			 'E-S'))
	plt.legend()

	plt.tight_layout()
	plt.show()

def curve(index):
	clock_shew=[]
	input_list=[]
	#print dp.data_process()
	input_list=dp.data_process()
	#print clock_shew
	#print input_list[index]
	x = np.linspace(0, len(input_list[index]),len(input_list[index]))

	with plt.style.context('fivethirtyeight'):
	    plt.plot(x,input_list[index])
	if index==0:
		title='A-E'
	elif index==1:
		title='A-S'
	elif index==2:
		title='S-S'
	elif index==3:
		title='S-S'
	plt.title(title)
	plt.xlabel('Number of data')
	plt.ylabel('Delay in second')
	plt.show()
	
if __name__=="__main__":
	#box()
	curve(int(sys.argv[1]))
	#dp.data_process()
