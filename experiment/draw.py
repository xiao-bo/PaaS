"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt
import data_processing as dp
def box():
	n_groups = 3

	means_men = (20, 100, 30)
	std_men = (2, 6, 10)
	fig, ax = plt.subplots()

	index = np.arange(n_groups)
	print index
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
	plt.ylabel('clock skew(ms)')
	plt.title('')
	plt.xticks(index + bar_width, ('S-A', 'S-E ',
			 'A-E'))
	plt.legend()

	plt.tight_layout()
	plt.show()

def curve():
	clock_shew=[]
	#print dp.data_process()
	clock_shew=dp.data_process()
	#print clock_shew
	
	x = np.linspace(0, len(clock_shew),len(clock_shew))
	#print x
	with plt.style.context('fivethirtyeight'):
	    #plt.plot(x, np.sin(x) + x + np.random.randn(10))
	    #plt.plot(x, np.sin(x) + 0.5 * x + np.random.randn(50))
	    #plt.plot(x, np.sin(x) + 2 * x + np.random.randn(50))
	    plt.plot(x,clock_shew)
	plt.title('E-S')
	plt.xlabel('Number of data')
	plt.ylabel('Delay in second')
	plt.show()
	#"""
if __name__=="__main__":
	#box()
	curve()
	#dp.data_process()
