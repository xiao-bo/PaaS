import data_processing as dp
import draw
import sys
sys.path.insert(0,'/Users/xiao/Desktop/PaaS/experiment/ptpd')
import period


if __name__=="__main__":
	
	index=int(sys.argv[1])
	
	title=""
	offset=period.period("ptpd/data.txt")
	statistics=[]
	##choose title and list
	if index ==0:
		timestamp_former=dp.read_file("arduino/data.txt",2)
		timestamp_backer=dp.read_file('edison/data.txt',0)
		title='IP stack (arduino- Edison) '
	elif index==1:
		timestamp_former=dp.read_file("arduino/data.txt",2)
		timestamp_backer=dp.read_file("serial/data.txt",2)

		title='IP stack(arduino)-Serial'
	elif index==2:
		timestamp_former=dp.read_file('edison/data.txt',0)
		timestamp_backer=dp.read_file("serial/data.txt",2)
		title='Edison-Serial'
	elif index==3:
		timestamp_former=dp.read_file('edison/data.txt',3)##edison receiver
		timestamp_backer=dp.read_file('edison/data.txt',0)##edison sender
		
		###if sync ? ie , remove offset??
		#timestamp_backer=dp.time_sync(timestamp_backer,offset)
		title='Network delay (Mac_receiver-Edison_send)'
	elif index==4:
		title='ptpd'

	##error=former-backer
	if index!=4:
		error_data=dp.data_process_2(timestamp_former,timestamp_backer)
		if error_data:## check list is empty
			statistics=[dp.compute_statistics(error_data)]
	
	elif index==4:
		error_data=offset
		statistics=[[0,0,0]]
	#print offset
	#print error_data
	#print statistics
	draw.curve(error_data,title,statistics)
