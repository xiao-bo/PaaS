"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import data_processing as dp
import matplotlib.patches as mpatches
import matplotlib
import sampling as sa

def curve(input_list,title,statistics):	
	output_list=[]
	##set subplot position 
	rect_curve = [0.1, 0.3, 0.8, 0.6]#left,bottom,width,height
	rect_table = [-0.10, 0.18 ,1,2.0]
	##curve
	curve = plt.axes(rect_curve)
	x = np.linspace(0, len(input_list),len(input_list))
	with plt.style.context('fivethirtyeight'):
	    line=curve.plot(x,input_list)	
	    plt.setp(line, linewidth=3)
	curve.axes.set_xlabel("sampling",fontsize=40)
	curve.axes.set_ylabel("period in millisecond",fontsize=40)
	curve.axes.set_title(title,fontsize=32)
        curve.axes.set_xlim([0,20000])
        #curve.axes.set_ylim([0,20])

        #curve.axes.set_xlim([0,400])
        #matplotlib.rc('xtick',labelsize=40)
        matplotlib.rcParams.update({'font.size':50})
	#table
	axTable = plt.axes(rect_table, frameon =False)
	axTable.axes.get_xaxis().set_visible(False)
	axTable.axes.get_yaxis().set_visible(False)
	
	table_columns = ('Mean', 'Standard_deviation')
        cell_text=statistics
        
	table_size=axTable.table(cellText=statistics, loc='bottom',
		colLabels=table_columns)

	## set table size and font
        table_size.auto_set_font_size(False)
	table_size.set_fontsize(50)
        table_size.scale(1.2,2)
	plt.show()
def multicurve(input_list,title,statistics):	
	output_list=[]
	
	##set subplot position 
	rect_curve = [0.1, 0.3, 0.8, 0.6]#left,bottom,width,height
	rect_table = [-0.10, 0.18 ,1,2.0]

	#legend_label=['remove jitter','sampling jitter']
	legend_label=['0%','500Mbit/s','950Mbit/s']
	curve = plt.axes(rect_curve)
	for i in range(0,len(input_list)):
		x = np.linspace(0, len(input_list[i]),len(input_list[i]))
		with plt.style.context('fivethirtyeight'):
	   		line=curve.plot(x,input_list[i],label=legend_label[i])	
			plt.setp(line, linewidth=3)
	curve.axes.set_xlabel("sampling",fontsize=40)
	curve.axes.set_ylabel("Delay in millisecond",fontsize=40)
	curve.axes.set_title(title,fontsize=28)
        #curve.axes.set_ylim([0,20])
    
        plt.legend(line)	
	##set legend position
	curve.legend(bbox_to_anchor=(1.05, 1.0),fontsize=30)

        matplotlib.rcParams.update({'font.size':50})
	#table
        '''
	axTable = plt.axes(rect_table, frameon =False)
	axTable.axes.get_xaxis().set_visible(False)
	axTable.axes.get_yaxis().set_visible(False)
	
	table_columns = ('Mean', 'Standard_deviation')
        cell_text=statistics
        
	table_size=axTable.table(cellText=statistics, loc='bottom',
		colLabels=table_columns)
	## set table size and font
        table_size.auto_set_font_size(False)
	table_size.set_fontsize(50)
        table_size.scale(1.2,3)
        '''
	plt.show()



if __name__=="__main__":
        ## main code for multicurve
	## sender
	print "draw.py"
        '''
        '''
	#send_former=dp.read_file('save/scalable/different_subnet/50%/arduino.txt',0)##edison receiver
	#send_backer=dp.read_file('save/scalable/different_subnet/50%/edison.txt',0)##edison sender
	send_former=dp.read_file('save/scalable/same_subnet/0%/arduino_remove_edison_jitter.txt',0)##edison receiver
	send_backer=dp.read_file('save/scalable/same_subnet/0%/edison_remove_jitter.txt',0)##edison sender
	send_remove_jitter=dp.data_process_2(send_former,send_backer)
        print send_remove_jitter
        ## receive
        receive_former=dp.read_file('save/scalable/different_subnet/95%/arduino_remove_edison_jitter.txt',2)##edison receiver
	receive_backer=dp.read_file('save/scalable/different_subnet/95%/edison_remove_jitter.txt',3)##edison sender
        #receive_former=dp.read_file('save/scalable/arduino_is_late/same_subnet/arduino_remove_edison_jitter.txt',2)##edison receiver
	#receive_backer=dp.read_file('save/scalable/arduino_is_late/same_subnet/edison_remove_jitter.txt',3)##edison sender
	receive_remove_jitter=dp.data_process_2(receive_former,receive_backer)
       
        ##sampling error
        send_time=[]
        receive_time=[]
        send_interval=[]
        send_sampling_bias=[]
        receive_interval=[]
        receive_sampling_bias=[]
        ##sampling sending error
        #send_time=dp.read_file('save/scalable/arduino_is_late/different_subnet/95%/edison.txt',0)##sender
	send_time=dp.read_file('save/scalable/same_subnet/0%/edison_110.txt',0)##sender
        send_interval=sa.real_clock_interval(send_time)
        send_sampling_bias=sa.sampling_bias(send_interval,1.0)
        receive_time=dp.read_file('save/scalable/different_subnet/95%/edison_remove_jitter.txt',3)##receive
        #receive_time=dp.read_file('save/scalable/arduino_is_late/same_subnet/edison.txt',3)##receive
        receive_interval=sa.real_clock_interval(receive_time)
        receive_sampling_bias=sa.sampling_bias(receive_interval,1.0)	
            
        send_remove_jitter_statistics=dp.compute_statistics(send_remove_jitter)
        receive_remove_jitter_statistics=dp.compute_statistics(receive_remove_jitter)
        index=int(sys.argv[1])
        if index==0:
            statistics=[send_remove_jitter_statistics]
	    error_data=[send_remove_jitter,send_sampling_bias]
	    #title='Tsa-Tse in different subnet with background traffic 95%, and edison remove jitter'
	    #title='Tsa-Tse in different subnet without background traffic , and edison remove jitter'
	    title='Tsa-Tse in same subnet without background traffic , and edison remove jitter'
        elif index==1:
            #statistics=[receive_remove_jitter_statistics]
	    #error_data=[receive_remove_jitter,receive_sampling_bias]
	    #title='Tra-Tre in same subnet without background traffic , and edison remove jitter'
	    title='Tra-Tre in different subnet with background traffic 95%, and edison remove jitter'
        elif index==2:
            #preliminary study
	    send_former_0=dp.read_file('save/preliminary_study/0%/arduino_110.txt',2)
	    send_backer_0=dp.read_file('save/preliminary_study/0%/edison_110.txt',2)##edison sender
	    send_former_50=dp.read_file('save/preliminary_study/50%/arduino_remove_edison_jitter.txt',2)##edison receiver
	    send_backer_50=dp.read_file('save/preliminary_study/50%/edison_remove_jitter.txt',2)##edison sender
	    send_former_95=dp.read_file('save/preliminary_study/95%/arduino_remove_edison_jitter.txt',2)##edison receiver
	    send_backer_95=dp.read_file('save/preliminary_study/95%/edison_remove_jitter.txt',2)##edison sender
            '''
	    send_former_0=dp.read_file('save/scalable/same_subnet/0%/arduino_110.txt',0)
	    send_backer_0=dp.read_file('save/scalable/same_subnet/0%/edison_110.txt',0)##edison sender
	    send_former_50=dp.read_file('save/scalable/same_subnet/50%/arduino_110.txt',0)##edison receiver
	    send_backer_50=dp.read_file('save/scalable/same_subnet/50%/edison_110.txt',0)##edison sender
	    send_former_95=dp.read_file('save/scalable/same_subnet/95%/arduino_110.txt',0)##edison receiver
	    send_backer_95=dp.read_file('save/scalable/same_subnet/95%/edison_110.txt',0)##edison sender
            '''
	    send_0=dp.data_process_2(send_former_0,send_backer_0)
	    send_50=dp.data_process_2(send_former_50,send_backer_50)
	    send_95=dp.data_process_2(send_former_95,send_backer_95)
            statistics_0=dp.compute_statistics(send_0)
            statistics_50=dp.compute_statistics(send_50)
            statistics_95=dp.compute_statistics(send_95)
            error_data=[send_0,send_50,send_95]
            #title="Tsa-Tse in same subnet with different background traffic"
            title="IP stack(arduino)-edison (Tra-Tse) in same subnet with different background traffic and remove jitter"
            print statistics_0
            print statistics_50
            print statistics_95
        #print receive_remove_jitter
        multicurve(error_data,title,statistics_0)
