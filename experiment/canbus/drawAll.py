"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import data_processing as dp
import matplotlib.patches as mpatches
from matplotlib.pyplot import figure, draw



def curve(input_list,title,statistics):	
	output_list=[]
        #plt.figure(figsize=[6, 6])	
	##set subplot position 
	#rect_curve = [0.1, 0.3, 0.8, 0.6]#left,bottom,width,height
	#rect_curve = [0.1, 0.3, 0.8, 0.6]#left,bottom,width,height
	#rect_table = [0.1, 0.2 ,0.8, 0.8]

	##curve
	curve = plt.axes()
	x = np.linspace(0, len(input_list),len(input_list))
	with plt.style.context('fivethirtyeight'):
	    line=curve.plot(x,input_list)	
	    plt.setp(line, linewidth=2)
	curve.axes.set_xlabel("sampling")
	curve.axes.set_ylabel("Error in Millisecond")
	curve.axes.set_title(title)
        '''
        #plt.ylim([0,40])
        font = {'family' : 'normal',
                'weight' : 'bold',
                'size'   : 24}
        plt.rc('font',**font)
	
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
        plt.savefig("/home/newslab/Desktop/test.svg")
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
	curve.axes.set_ylabel("variation in milliSecond")
	curve.axes.set_title(title)
	
	
	#table
	axTable = plt.axes(rect_table, frameon =False)
	axTable.axes.get_xaxis().set_visible(False)
	axTable.axes.get_yaxis().set_visible(False)
	
	table_rows=('0Mbit','100Mbit','500Mbit','800Mbit')
	table_columns = ('Mean', 'Standard_deviation')
        cell_text=statistics
        
	table_size=axTable.table(cellText=statistics, loc='bottom',
		colLabels=table_columns,rowLabels=table_rows)

	## set table size and font
	table_size.set_fontsize(12)
	table_size.scale(1,1)

	##set legend position
	curve.legend(bbox_to_anchor=(1.05, 1.05))
	
	plt.show()



if __name__=="__main__":

	print "draw.py"
        #dire = '/home/newslab/Desktop/PaaS/experiment/canbus/data/1v3/10hz/0%another/'
        dire = '/home/newslab/Desktop/PaaS/experiment/canbus/data/1v3/1hz/0%/long/'
	
        ## 1hz
        #value ="_0.txt"
        value ="_1023.txt"
        #value ="_all.txt"
        Etimestamp=dp.ReadEdisonFile(dire+'edison'+value,1)##edison sender
        S0timestamp,S1timestamp,S2timestamp=dp.ReadArduinoFile(dire+'offline0018'+value,9)##arduino sender
        length = 30000
        

        '''
        ES0data=dp.computeError(Etimestamp,S0timestamp,length)
        #ES0title = '10hz,back 0%,with jitter, backpri=13,pri=10,ES0'
        ES0title = '1hz,back 0%, with jitter,backpri=13,pri=10,ES0 '
	ES0statistics=dp.compute_statistics(ES0data) 
        curve(ES0data,ES0title,[ES0statistics])
        '''
        
        '''
        ###board1
        ES1data=dp.computeError(Etimestamp,S1timestamp,length)
        #ES1title = '10hz,back 0%,with jitter backpri=13,pri=11,ES1'
        ES1title = '1hz,back 0%, with jitter,backpri=13,pri=11,ES1'
	ES1statistics=dp.compute_statistics(ES1data) 
        curve(ES1data,ES1title,[ES1statistics])
        
        
        '''
        ##board2

        ES2data=dp.computeError(Etimestamp,S2timestamp,length)
	ES2statistics=dp.compute_statistics(ES2data) 
        #ES2title = '10hz,back 0%,with jitter backpri=13,pri=18,ES2'
        ES2title = '1hz,500kbit/s,1vs3,background 0%, with jitter,backpri=13,pri=18,ES2'
        curve(ES2data,ES2title,[ES2statistics])
        '''
        '''
        '''
        
        '''
        
        '''
        ## delay 
        fileRead = open(dire+'delay.txt','r')
        delay = []
        x = 0
        for line in fileRead:
            
            delay.append(float(line))
            x = x +1
            if x> length:
                break
        delayStat = dp.compute_statistics(delay)
        curve(delay,"delay between arduino's sendTime and pi's receiveTime",[delayStat])

        ## difference
          
        fileRead = open(dire+'rtime.txt','r')
        odiff = []
        ediff = []
        length = 999
        x = 0
        for line in fileRead:
            ans = line.split(":")   
            odiff.append(abs(float(ans[1])))
            ediff.append(abs(float(ans[3])))
            x = x +1
            if x> length:
                break
        odiffStat = dp.compute_statistics(odiff)
        ediffStat = dp.compute_statistics(ediff)
            curve(odiff,"the variation of pi's receiveTime interval",[odiffStat])
        curve(ediff,"the variation of edison's sendTime interval",[ediffStat])
        '''
        '''
        ## counter 
        fileRead = open(dire+'counter0018.txt','r')
        counterdiff = []
        length = 4634120
        x = 0
        for line in fileRead:
            ans = line.split(":")   
            counterdiff.append(float(ans[2]))
            x = x +1
            if x> length:
                break
        counterdiffStat = dp.compute_statistics(counterdiff)
        print counterdiff.index(min(counterdiff))
        print min(counterdiff)
        #for x in range(3000,3200):
        #    print counterdiff[x]
        curve(counterdiff,"period of the variation of arduino's counter interval(100,0018 board)",[counterdiffStat])
        '''  
