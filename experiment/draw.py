"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt

def curve(input_list,title):

	#x = np.linspace(0, len(input_list[index]),len(input_list[index]))	
	x = np.linspace(0, len(input_list),len(input_list))	

	with plt.style.context('fivethirtyeight'):
	    #plt.plot(x,input_list[index])
	    plt.plot(x,input_list)

	plt.title(title)
	plt.xlabel('sampling')
	plt.ylabel('Delay in second')
	plt.show()

#def bar(input_list,index,title):

if __name__=="__main__":
	
	curve(int(sys.argv[1]))
