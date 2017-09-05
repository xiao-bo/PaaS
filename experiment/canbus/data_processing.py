import sys
sys.path.insert(0,'/home/newslab/Desktop/PaaS/experiment/ptpd')
#import period
import numpy
import draw
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
			delay.append(abs(first-second))
			
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
	##offset = slave - master=mac - edison
	##
	for x,y in zip(edison,offset):
			sync.append(x+float(y))
	return sync

def compute_statistics(delay_list):
	##evalute average , standard deviation, mean square error
	delay_list=numpy.array(delay_list)
        '''
	summary=0.0
	for x in delay_list:
		summary = summary+x*x
	mse=summary/len(delay_list)
	'''
	print "mean: "+str(numpy.mean(delay_list))
	print "standard deviation: "+str(numpy.std(delay_list))
	#print "mse: "+str(mse)
	return [numpy.mean(delay_list),numpy.std(delay_list)]


def data_process_2(list_former,list_backer):

	### insert integer 0.0 to recover miss part 
	timestamp_former=align(list_former)
	timestamp_backer=align(list_backer)
	### compute delay between list
	delay=compute_delay(timestamp_former,timestamp_backer)
	#delay=compute_delay(list_former,list_backer)
	
	#if delay:## check list is empty
	#	compute_statistics(delay)
	return delay
	

def data_process():
	###read data and append list
	timestamp_arduino=read_file("arduino/data.txt",1)
	timestamp_edison_send=read_file('edison/data.txt',2)
	#timestamp_edison_receive=read_file('edison/data.txt',3)
	#timestamp_serial=read_file("serial/data.txt",2)
	#offset=period.period("ptpd/data.txt")
	#print offset
	
	### insert integer 0.0 to recover miss part
	#timestamp_arduino=align(timestamp_arduino)
	#timestamp_edison_send=align(timestamp_edison_send)
	#timestamp_edison_receive=align(timestamp_edison_receive)
	#timestamp_serial=align(timestamp_serial)
	
	#timestamp_edison_receive=time_sync(timestamp_edison_receive,offset)
	#print timestamp_edison_receive	

	##debug message
	print '------------\ntimestamp_arduino\n------------'
	print timestamp_arduino
	print '------------\ntimestamp_edison_send\n------------'
	print timestamp_edison_send	
	'''
	print '------------\ntimestamp_serial\n------------'
	print timestamp_serial
	print '------------\ntimestamp_edison_receive\n------------'
	print timestamp_edison_receive
	
	'''
        arduino_tmp=[]
        edison_tmp=[]
        for x in timestamp_arduino:
            arduino_tmp.append(x/1000000000)
        for y in timestamp_edison_send:
            edison_tmp.append(x/1000000000)
	delay_arduino_edison=compute_delay(arduino_tmp,edison_tmp)
	### compute delay between list
	#delay_arduino_edison=compute_delay(timestamp_arduino,timestamp_edison_send)
	#delay_arduino_serial=compute_delay(timestamp_arduino,timestamp_serial)
	#delay_edison_serial=compute_delay(timestamp_edison_send,timestamp_serial)
	#delay_edison_receive_send=compute_delay(timestamp_edison_receive,
	#	timestamp_edison_send)
	print '------------\ndelay_arduino_edison\n------------'
	print delay_arduino_edison
	
	'''
	print '------------\ndelay_arduino_serial\n------------'
	print delay_arduino_serial
	print '------------\ndelay_edison_serial\n------------'
	print delay_edison_serial
	print '------------\ndelay_edison_receive_send\n------------'
	print delay_edison_receive_send
	
	'''
	
	##evalute average , standard deviation, mean square error
	'''
	if delay_arduino_edison:## check list is empty
		compute_statistics(delay_arduino_edison)
	if delay_arduino_serial:
		compute_statistics(delay_arduino_serial)
	if delay_edison_serial:
		compute_statistics(delay_edison_serial)
	if delay_edison_receive_send:
		compute_statistics(delay_edison_receive_send)
	'''
	###debug message
	
	
	return [delay_arduino_edison]
	'''
	#return offset
	#return [delay_edison_receive_send,max(delay_edison_receive_send)]
	return delay_edison_receive_send
	'''
if __name__=='__main__':
        error_data=data_process()
        draw.curve(error_data,"s")
