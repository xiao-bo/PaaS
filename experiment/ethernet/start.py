import data_processing as dp
import draw
import sys
sys.path.insert(0,'/Users/xiao/Desktop/PaaS/experiment/ptpd')
import period


if __name__=="__main__":
	
	index=int(sys.argv[1])
	
	title=""
	#offset=period.period("ptpd/data.txt")
	statistics=[]
	##choose title and list
        '''
	if index ==0:
		timestamp_former=dp.read_file("edison/1.txt",3)
		timestamp_backer=dp.read_file('edison/2.txt',3)
		title='clock skew between Edison1 and Edison 2 '
	elif index==1:
		timestamp_former=dp.read_file("edison/1.txt",3)
		timestamp_backer=dp.read_file("edison/3.txt",3)

		title='clock skew between Edison1 and Edison 3 '
	elif index==2:
		timestamp_former=dp.read_file('edison/2.txt',3)
		timestamp_backer=dp.read_file("edison/3.txt",3)
		title='clock skew between Edison2 and Edison 3 '

	'''
        if index ==0:
		#timestamp_former=dp.read_file("save/scalable/different_subnet/95%/arduino.txt",2)
		#timestamp_backer=dp.read_file("save/scalable/different_subnet/95%/edison.txt",3)
		#timestamp_former=dp.read_file("arduino/arduino.txt",2)
		#timestamp_backer=dp.read_file('edison/edison.txt',0)
		#timestamp_former=dp.read_file("save/scalable/different_subnet/95%/arduino.txt",2)
		#timestamp_backer=dp.read_file("save/scalable/different_subnet/95%/edison.txt",3)
		#timestamp_former=dp.read_file("save/preliminary_study/95%/arduino_110.txt",2)
		#timestamp_backer=dp.read_file("save/preliminary_study/95%/edison_110.txt",2)
		#timestamp_former=dp.read_file("save/scalable/same_subnet/50%/arduino.txt",2)
		#timestamp_backer=dp.read_file("save/scalable/same_subnet/50%/edison.txt",3)
		timestamp_former=dp.read_file("save/preliminary_study/0%/arduino_110.txt",2)
		timestamp_backer=dp.read_file("save/preliminary_study/0%/edison_110.txt",2)
                
		#title='IP stack (arduino)- Edison (Tra-Tse) without background traffic'
                #title='Tra-Tre in the different subnet with background traffic 95% '
                #title='Tra-Tre in the different subnet and lab switch without background traffic '
                #title=' Tra-Tre in the different subnet with background traffic  95%'
                title=' Tra-Tre in the same subnet without background traffic'
	elif index==1:
                timestamp_former=dp.read_file("save/scalable/different_subnet/0%/arduino_remove_edison_jitter.txt",0)
		timestamp_backer=dp.read_file("save/scalable/different_subnet/0%/edison_remove_jitter.txt",0)
		#timestamp_former=dp.read_file("save/scalable/same_subnet/0%/all/arduino_remove_edison_jitter.txt",0)
		#timestamp_backer=dp.read_file("save/scalable/same_subnet/0%/all/edison_remove_jitter.txt",0)
		#timestamp_former=dp.read_file("save/scalable/same_subnet/0%/all/arduino.txt",0)
		#timestamp_backer=dp.read_file("save/scalable/same_subnet/0%/all/edison.txt",0)
		#timestamp_former=dp.read_file("save/preliminary_study/0%/arduino_110.txt",2)
		#timestamp_backer=dp.read_file("save/preliminary_study/0%/edison_110.txt",2)
		#timestamp_former=dp.read_file("arduino/arduino.txt",0)
		#timestamp_backer=dp.read_file("edison/edison.txt",0)
                #title='IP stack(arduino) - serial port (Tra-Trs) without background traffic '

		#title='Tsa-Tse in the different subnet with background traffic 50% and remove jitter'
                #title=' Tsa-Tse in the different subnet and lab switch with background traffic 950MBit/s'
                title=' Tsa-Tse in the different subnet without background traffic and remove jitter'
                #title=' Tsa-Tse in the same subnet without background traffic and remove jitter'
                #title='IP stack (arduino)-edison(Tra-Tse) without background traffic'
        elif index==2:
		timestamp_former=dp.read_file("save/preliminary_study/95%/edison_110.txt",2)
		timestamp_backer=dp.read_file("save/preliminary_study/95%/serial_110.txt",2)
		title='Edison - serial port (Tse-Trs) without background traffic'
	elif index==3:
		timestamp_former=dp.read_file('arduino/1.txt',2)##arduino1 sender
		timestamp_backer=dp.read_file('arduino/2.txt',2)##arduino2 sender
		
		###if sync ? ie , remove offset??
		#timestamp_backer=dp.time_sync(timestamp_backer,offset)
		title='Network delay (Mac_receiver-Edison_send)'
	elif index==4:
		title='ptpd'
	##error=former-backer
	if index!=4:
		error_data=dp.data_process_2(timestamp_former,timestamp_backer)
		print error_data
                if error_data:## check list is empty
			statistics=[dp.compute_statistics(error_data)]
        '''	
	elif index==4:
		error_data=offset
		statistics=[[0,0,0]]
        '''
        print statistics
	#print offset
	#print error_data
	#print statistics
	draw.curve(error_data,title,statistics)
