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
	curve.axes.set_ylabel("different with exhausted method")
	curve.axes.set_title(title)
        plt.ylim([0,40])
        font = {'family' : 'normal',
                'weight' : 'bold',
                'size'   : 20}
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

	legeng_label=['0Mbit','100Mbit','500Mbit']
	##curve
	curve = plt.axes(rect_curve)
	for i in range(0,len(input_list)):
		x = np.linspace(0, len(input_list[i]),len(input_list[i]))
		with plt.style.context('fivethirtyeight'):
	   		line=curve.plot(x,input_list[i])#,label=legeng_label[i])	
			plt.setp(line, linewidth=2)
        font = {'family' : 'normal',
                'weight' : 'bold',
                'size'   : 20}
        plt.rc('font',**font)
	curve.axes.set_xlabel("sampling")
	curve.axes.set_ylabel("diff")
	curve.axes.set_title(title)
	
	
	#table
	axTable = plt.axes(rect_table, frameon =False)
	axTable.axes.get_xaxis().set_visible(False)
	axTable.axes.get_yaxis().set_visible(False)
	
	table_rows=('select','exhausted','diff')
	table_columns = ('Mean', 'Standard_deviation')
        cell_text=statistics
        
	table_size=axTable.table(cellText=statistics, loc='bottom',
		colLabels=table_columns,rowLabels=table_rows)

	## set table size and font
	table_size.set_fontsize(20)
	table_size.scale(1,1)

	##set legend position
	curve.legend(bbox_to_anchor=(1.05, 1.05))
	
	plt.show()



if __name__=="__main__":
	## main code for multicurve
	print "draw.py"
	title  = "10 node,weight 0~20, deadline = 128+c+0~100,arrival = 0~100"

	select = [45.0, 33.0, 53.0, 28.0, 38.0, 33.0, 44.0, 34.0, 33.0, 36.0, 30.0, 28.0, 42.0, 32.0, 41.0, 35.0, 31.0, 43.0, 38.0, 29.0, 46.0, 29.0, 40.0, 31.0, 42.0, 38.0, 38.0, 31.0, 35.0, 40.0, 51.0, 48.0, 33.0, 33.0, 52.0, 52.0, 42.0, 54.0, 55.0, 33.0, 29.0, 30.0, 36.0, 52.0, 51.0, 42.0, 59.0, 34.0, 46.0, 36.0, 40.0, 48.0, 20.0, 33.0, 36.0, 31.0, 56.0, 37.0, 42.0, 37.0, 44.0, 32.0, 43.0, 38.0, 31.0, 35.0, 35.0, 44.0, 31.0, 51.0, 41.0, 36.0, 55.0, 39.0, 52.0, 34.0, 38.0, 33.0, 26.0, 36.0, 34.0, 36.0, 36.0, 37.0, 25.0, 33.0, 33.0, 24.0, 23.0, 30.0, 41.0, 41.0, 36.0, 56.0, 46.0, 36.0, 33.0, 36.0, 52.0, 29.0]

	exhausted =[45.0, 35.0, 53.0, 30.0, 39.0, 33.0, 44.0, 34.0, 33.0, 36.0, 33.0, 28.0, 42.0, 32.0, 41.0, 35.0, 31.0, 43.0, 39.0, 33.0, 46.0, 34.0, 40.0, 31.0, 42.0, 38.0, 38.0, 33.0, 40.0, 40.0, 53.0, 48.0, 33.0, 41.0, 52.0, 52.0, 42.0, 54.0, 55.0, 39.0, 29.0, 34.0, 36.0, 57.0, 51.0, 42.0, 59.0, 39.0, 46.0, 36.0, 40.0, 48.0, 24.0, 33.0, 36.0, 31.0, 56.0, 45.0, 44.0, 49.0, 46.0, 32.0, 43.0, 38.0, 31.0, 44.0, 43.0, 49.0, 34.0, 54.0, 41.0, 36.0, 55.0, 39.0, 52.0, 40.0, 40.0, 34.0, 27.0, 36.0, 38.0, 36.0, 36.0, 37.0, 25.0, 35.0, 33.0, 24.0, 23.0, 33.0, 41.0, 50.0, 42.0, 56.0, 46.0, 38.0, 35.0, 36.0, 52.0, 33.0]

	diffdata = [0.0, 2.0, 0.0, 2.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 4.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 5.0, 0.0, 2.0, 0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0, 0.0, 4.0, 0.0, 5.0, 0.0, 0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 8.0, 2.0, 12.0, 2.0, 0.0, 0.0, 0.0, 0.0, 9.0, 8.0, 5.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0, 2.0, 1.0, 1.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 3.0, 0.0, 9.0, 6.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 4.0]
	diffSt=dp.compute_statistics(diffdata)
        
        exhaustedSt = dp.compute_statistics(exhausted)
        selectSt = dp.compute_statistics(select)
	#curve(zero_data,title,[zero_statistics])
        multicurve([select,exhausted,diffdata],title,[selectSt,exhaustedSt,diffSt])
