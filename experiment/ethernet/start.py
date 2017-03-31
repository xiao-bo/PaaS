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
		timestamp_former=dp.read_file("arduino/1.txt",2)
		timestamp_backer=dp.read_file('edison/1.txt',3)
		#timestamp_former=dp.read_file("save/scalable/800MBit/arduino.txt",2)
		#timestamp_backer=dp.read_file('save/scalable/800MBit/edison.txt',3)
                
		#title='IP stack (arduino- Edison) '
                title='Tra-Tre without background traffic '
	elif index==1:
		timestamp_former=dp.read_file("arduino/1.txt",0)
		timestamp_backer=dp.read_file("edison/1.txt",0)
		#timestamp_former=dp.read_file("save/scalable/800MBit/arduino.txt",0)
		#timestamp_backer=dp.read_file('save/scalable/800MBit/edison.txt',0)

		title='Tsa-Tse without background traffic '
	elif index==2:
		timestamp_former=dp.read_file('edison/data.txt',0)
		timestamp_backer=dp.read_file("serial/data.txt",2)
		title='Edison-Serial'
	elif index==3:
		timestamp_former=dp.read_file('edison/data3.txt',3)##edison receiver
		timestamp_backer=dp.read_file('edison/data3.txt',0)##edison sender
		
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
	#print offset
	#print error_data
	#print statistics
	draw.curve(error_data,title,statistics)
