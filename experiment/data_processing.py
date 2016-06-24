import sys
sys.path.insert(0,'/Users/xiao/Documents/code/paas/git/PaaS/experiment/ptpd')
import period

def read_file(filename,index):
	##read data and append list
	file_read=open(filename,'r')
	timestamp=[]
	for line in file_read:
		ans=line.split(":")[index]
		timestamp.append(float(ans))

	return timestamp

def compute_delay(list_1,list_2):
	delay=[]
	for first,second in zip(list_1,list_2):
		if first==0 or second==0 :
			continue
		elif abs(first-second)<50:
		### minute different will lead value larger 50
			delay.append(first-second)
			
	return delay

def align(time_list):
	## count number of zero because x can't ++ in 
	##loop and lead number of loop shorter 
	count=0
	for x in range(0,len(time_list)-1): 
		diff=time_list[x+1]-time_list[x]
		#print diff
		if diff<0:
			diff=diff+60
		if diff>0.6:
			for y in range(0,int(round(diff/0.5))-1):
				count=count+1
	for x in range(0,len(time_list)-1+count):
		if time_list[x]==0:
			continue
		diff=time_list[x+1]-time_list[x]
		if diff<0:
			diff=diff+60
		if diff>0.6:
			for y in range(0,int(round(diff/0.5))-1):## insert multiple zero
				time_list.insert(x+1,0.0)

	return time_list

def time_sync(edison,offset):
	sync=[]
	for x,y in zip(edison,offset):
			sync.append(x-float(y))
	return sync
def data_process():
	###read data and append list
	timestamp_arduino=read_file("arduino/data.txt",2)
	timestamp_edison_send=read_file('edison/data.txt',2)
	timestamp_edison_receive=read_file('edison/data.txt',5)
	timestamp_serial=read_file("serial/data.txt",2)
	offset=period.period("ptpd/data.txt")
	print offset
	
	### insert integer 0.0 to recover miss part
	timestamp_arduino=align(timestamp_arduino)
	timestamp_edison_send=align(timestamp_edison_send)
	timestamp_edison_receive=align(timestamp_edison_receive)
	timestamp_serial=align(timestamp_serial)
	
	timestamp_edison_receive=time_sync(timestamp_edison_receive,offset)
	

	##debug message
	'''
	print '------------\ntimestamp_arduino\n------------'
	print timestamp_arduino
	print '------------\ntimestamp_edison_send\n------------'
	print timestamp_edison_send
	print '------------\ntimestamp_edison_receive\n------------'
	print timestamp_edison_receive
	print '------------\ntimestamp_serial\n------------'
	print timestamp_serial
	'''
	
	### compute delay between list
	delay_arduino_edison=compute_delay(timestamp_arduino,timestamp_edison_send)
	delay_arduino_serial=compute_delay(timestamp_arduino,timestamp_serial)
	delay_edison_serial=compute_delay(timestamp_edison_send,timestamp_serial)
	delay_edison_receive_send=compute_delay(timestamp_edison_receive,
		timestamp_edison_send)
	
	
	##evalute average and summary
	avg_a_e=sum(delay_arduino_edison)/len(delay_arduino_edison)
	avg_a_s=sum(delay_arduino_serial)/len(delay_arduino_serial)
	avg_e_s=sum(delay_edison_serial)/len(delay_edison_serial)
	avg_e_r_s=sum(delay_edison_receive_send)/len(delay_edison_receive_send)
	
	###debug message
	'''
	#print a_e
	#print a_s
	#print e_s
	#print 'avg_a_e:'+str(avg_a_e)+' max:'+str(max(a_e))
	#print 'avg_a_s:'+str(avg_a_s)+' max:'+str(max(a_s))
	#print 'avg_a_s:'+str(avg_e_s)+' max:'+str(max(e_s))
	'''
	return [[delay_arduino_edison,delay_arduino_serial,delay_edison_serial
			,delay_edison_receive_send],
			[max(delay_arduino_edison),max(delay_arduino_serial),
			max(delay_edison_serial),max(delay_edison_receive_send)],
			[avg_a_e,avg_a_s,avg_e_s,avg_e_r_s]]
	


if __name__=='__main__':
	data_process()
