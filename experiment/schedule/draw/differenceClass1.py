"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches


def singleClass(diff,title):
    title = str(title)
    ## set class number
    number = title

    index = np.arange(0., 1000.,1)
    # red dashes,
    
    fig,ax = plt.subplots()
    ax.plot(index,diff,'bo',label = 'diff')
    
    ## set latex format for title and y label
    title = title + '}$'
    ax.set_title('$Class_{'+title)
    ax.set_xlabel("Index of Experiments")
    ax.set_ylabel("$Diff_{"+title)
    
    '''
    font = {'family' : 'normal',
                'weight' : 'bold',
                'size'   : 40}
    plt.rc('font',**font)
    '''
    ## set legend
    #legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')

    ## save svg file
    #plt.savefig(dire+"class"+number+".svg")
    
    plt.show()

if __name__=="__main__":
    #test()
    #dire = 'data/70sensor1000iterationFinally/'
    number = '1'
    fd = open("differenceClass"+number+".txt",'r')
    difference = []
    for line in fd:
    	difference.append(str(float(line)))
    
    
    singleClass(difference,number)

