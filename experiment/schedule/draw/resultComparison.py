"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

def multibar():
    n_groups = 10
    data = [[ 152, 281, 127, 43,  120,210,74,13,1,0], ## big
            [ 712, 543, 587, 543, 493,481,478,406,573,952], ## equal
            ]
    small = (136, 176, 286, 414, 387,309,448,581,426,48)

    fig, ax = plt.subplots()
    
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    ## single bar

    
    columns = ('$Class_{1}$', '$Class_{2}$', '$Class_{3}$', '$Class_{4}$', '$Class_{5}$','$Class_{6}$','$Class_{7}$','$Class_{8}$','$Class_{9}$','$Class_{10}$')

    # Get some pastel shades for the colors

    index = np.arange(len(columns)) 
    bar_width = 0.4

    # Initialize the vertical-offset for the stacked bar chart.
    y_offset = np.zeros(len(columns))
    #for row in range(2):## single bar have 2 part.
    plt.bar(index, data[0], bar_width, bottom=y_offset, color='#99FFFF', label = '$max_i > CP_i$')
    y_offset = y_offset + data[0]
    plt.bar(index, data[1], bar_width, bottom=y_offset, color='#00CC00',label = '$max_i = CP_i$')

    rects2 = ax.bar(index + bar_width, small, bar_width,
                    alpha=opacity, color='r',
                    error_kw=error_config,
                    label='$max_i$ < $CP_{i}$')
    ## set label name
    ax.set_xlabel('Class')
    ax.set_ylabel('Number of comparisons')
    ax.set_title('Comparison of CP set and Max set ')

    ## set ticks size
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(columns)
    
    ## set class_i size
    #ax.xaxis.set_tick_params(labelsize=28)

    ## set legend position
    ax.legend(loc = 'best')

    ## set font
    '''
    font = {'family' : 'normal',
                'weight' : 'bold',
                'size'   : 20}
    plt.rc('font',**font)
    '''

    fig.tight_layout()

    ## save svg file
    #plt.savefig("/home/newslab/Pictures/schedule/test.svg")
    plt.show()

if __name__=="__main__":
    fo = open('resultComparison.txt','r')

    multibar()



