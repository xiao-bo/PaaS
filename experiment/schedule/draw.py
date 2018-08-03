"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import data_processing as dp
import matplotlib.patches as mpatches




def curve(input_list,title,statistics):	
	output_list=[]
	
	##set subplot position 
	rect_curve = [0.1, 0.3, 0.8, 0.6]#left,bottom,width,height
	rect_table = [0.1, 0.2 ,0.8, 0.8]

	##curve
	curve = plt.axes(rect_curve)
	x = np.linspace(0, len(input_list),len(input_list))
	with plt.style.context('fivethirtyeight'):
	    line=curve.plot(x,input_list)	
	    plt.setp(line, linewidth=2)
	curve.axes.set_xlabel("sampling")
	curve.axes.set_ylabel("Delay in Millisecond")
	curve.axes.set_title(title)
        plt.ylim([5,40])
        font = {'family' : 'normal',
                'weight' : 'bold',
                'size'   : 40}
        plt.rc('font',**font)
	
	#table
	axTable = plt.axes(rect_table, frameon =False)
	axTable.axes.get_xaxis().set_visible(False)
	axTable.axes.get_yaxis().set_visible(False)
	
	table_columns = ('Mean', 'Standard Deviation')
        cell_text=statistics
        
	table_size=axTable.table(cellText=statistics, loc='bottom',
		colLabels=table_columns)

	## set table size and font
	table_size.set_fontsize(40)
	table_size.scale(1.2,3)

	
	plt.show()
def multicurve(input_list,title,statistics):	
	output_list=[]
	
	##set subplot position 
	rect_curve = [0.1, 0.3, 0.8, 0.6]#left,bottom,width,height
	rect_table = [0.15, 0.2 ,0.8, 0.8]

	legeng_label=['0Mbit','100Mbit','500Mbit','800Mbit']
	##curve
	curve = plt.axes(rect_curve)
	for i in range(0,len(input_list)):
		x = np.linspace(0, len(input_list[i]),len(input_list[i]))
		with plt.style.context('fivethirtyeight'):
	   		line=curve.plot(x,input_list[i])#,label=legeng_label[i])	
			plt.setp(line, linewidth=2)

	curve.axes.set_xlabel("sampling")
	curve.axes.set_ylabel("Delay in milliSecond")
	curve.axes.set_title(title)
	
	##set legend position
	curve.legend(bbox_to_anchor=(1.05, 1.05))
	
	plt.show()

def singleClass(opt,cp,diff,title):
    title = str(title) 
    number = title
    # evenly sampled time at 200ms intervals
    index = np.arange(0., 1000.,1)
    #print t
    print index
    #print len(t)
    print len(index)
    #legeng_label=['0Mbit','100Mbit','500Mbit','800Mbit']
    # red dashes, blue squares and green triangles
    fig,ax = plt.subplots()#(index, opt, 'ro', index, cp, 'bs', index, diff, 'g^')
    #ax.plot(index,opt,'ro',label = 'opt')
    #ax.plot(index,cp,'bs',label = 'cp')
    ax.plot(index,diff,'g^',label = 'class_10')
    title = title + '}$'
    ax.set_title('$class_{'+title)
    ax.set_xlabel("")
    ax.set_ylabel("$Diff_{"+title)
    font = {'family' : 'normal',
                'weight' : 'bold',
                'size'   : 40}
    plt.rc('font',**font)
    #legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')
    plt.savefig(dire+"class"+number+".svg")
    plt.show()
def multibar():
    n_groups = 10
    font = {'family' : 'normal',
                'weight' : 'bold',
                'size'   : 20}
    plt.rc('font',**font)
    data = [[ 152, 281, 127, 43,  120,210,74,13,1,0], ## big
            [ 712, 543, 587, 543, 493,481,478,406,573,952], ## equal
            ]
    data2 = [[ 152, 281, 127, 43,  120,210,74,13,1], ## big
            [ 712, 543, 587, 543, 493,481,478,406,573], ## equal
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
    
    ax.set_xlabel('Class', fontsize = 36)
    ax.set_ylabel('Amount of comparisons',fontsize = 36)
    ax.set_title('Comparison of CP set and Max set ',fontsize = 36)
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(columns)
    ax.xaxis.set_tick_params(labelsize=28)
    ax.legend(loc = 'best')

    fig.tight_layout()
    plt.savefig("/home/newslab/Pictures/schedule/test.svg")
    plt.show()

if __name__=="__main__":
    #test()
    dire = 'data/70sensor1000iteration/'
    number = '10'
    fd = open(dire+"differenceClass"+number+".txt",'r')
    fo = open(dire+"optimalClass"+number+".txt",'r')
    fc = open(dire+"CPClass"+number+".txt",'r')
    difference = []
    optimal = []
    CP = []
    for line in fd:
    	difference.append(str(float(line)))
    for line in fo:
        optimal.append(str(float(line)))
    for line in fc:
        CP.append(str(float(line)))
    #singleClass(optimal,CP,difference,number)
    #singleClass(optimal,CP,difference,number)

    multibar()
    multibar()
    #t()
