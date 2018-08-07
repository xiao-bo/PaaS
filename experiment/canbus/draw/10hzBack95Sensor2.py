"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
from matplotlib.pyplot import figure, draw

def compute_statistics(delay_list):
    ##evalute average , standard deviation, mean square error
    delay_list=np.array(delay_list)
    length = len(delay_list)
    mean = np.mean(delay_list)
    std = np.std(delay_list)
    ste = std/math.sqrt(length)
    samplingError = ste/mean*100
    print "mean: "+str(mean)
    print "standard deviation: "+str(std)
    print "standard error:"+str(ste)
    print "sampling error:"+str(samplingError)+"%"
    
    return [np.mean(delay_list),np.std(delay_list),ste]


def curve(input_list,title,statistics):	
	output_list=[]


	##curve
	curve = plt.axes()
	x = np.linspace(0, len(input_list),len(input_list))
	with plt.style.context('fivethirtyeight'):
	    line=curve.plot(x,input_list)	
	    plt.setp(line, linewidth=2)
	curve.axes.set_xlabel("sampling")
	curve.axes.set_ylabel("Error (ms)")
	curve.axes.set_title(title)

        ## set y seies range from 0 to 40
        #plt.ylim([0,40])

        ## set font property
        '''
        font = {'family' : 'normal',
                'weight' : 'bold',
                'size'   : 40}
        plt.rc('font',**font)

        ## set table	
	#table
	axTable = plt.axes(rect_table, frameon =False)
	axTable.axes.get_xaxis().set_visible(False)
	axTable.axes.get_yaxis().set_visible(False)
	
	table_columns = ('Mean', 'Standard Deviation','Standard Error')
        cell_text=statistics
        
	table_size=axTable.table(cellText=statistics, loc='bottom',
		colLabels=table_columns)
    
	## set table size and font
        table_size.auto_set_font_size(False)
	table_size.set_fontsize(40)
	table_size.scale(1.2,3)
        '''
        
        ## save svg file 
        #plt.savefig("/home/newslab/Desktop/test.svg")
	plt.show()


if __name__=="__main__":

        filename = "10hzBack95ES2data.txt"
        fileRead = open(filename,'r')
        ES2data = []
        ## read error data
        for x in fileRead:
            ES2data.append(float(x))

        ## set title
        ES2title = '10hz,back 95%, with jitter,backpri=13,pri=14,ES2 '

        ## get mean,std,std_err
	ES2statistics=compute_statistics(ES2data) 
        
        ## draw
        curve(ES2data,ES2title,[ES2statistics])
