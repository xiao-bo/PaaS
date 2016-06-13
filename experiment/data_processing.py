
def data_process():
	### arduino timestamp
	file_read=open('arduino/data.txt','r')
	time_arduino=[]
	for line in file_read:
		ans=line.split(":")[2]
		time_arduino.append(float(ans))
	#print time_arduino
	print '==========='
	### edison timestamp
	#file_read=open('edison/data.txt','r')
	file_read=open('serial/two/new.txt','r')
	time_edison=[]
	for line in file_read:
		ans=float(line.split(":")[2])
		time_edison.append(ans)
	#print time_edison
	print '======='
	### serial timestamp

	file_read=open('serial/new.txt','r')
	time_serial=[]
	for line in file_read:
		ans=float(line.split(":")[2])
		time_serial.append(ans)
	#print time_serial
	

	a_delay=align(time_arduino)
	s_delay=align(time_serial)
	e_delay=align(time_edison)
	#s_delay=time_serial
	#e_delay=time_edison
	

	
	print 'aaaaaa'
	#print a_delay
	print '===eeeee'
	#print e_delay
	#print '===sss'
	#print s_delay
	#print '===a:'+str(a_delay[13])+' ===e: '+str(e_delay[13])
	#print e_delay

	a_e=[]
	a_s=[]
	e_s=[]
	line=0
	### evalute delay
	for a,e in zip(a_delay,e_delay):
		if a==0 or e==0 :
			continue
		elif a-e>-50: 
			a_e.append(a-e)
			#print 'line: '+str(line)+' a-e= '+str(a-e)
	
	for a,s in zip(a_delay,s_delay):
		if a==0 or s==0 :
			continue
		elif a-s>-50: 
			a_s.append(a-s)
	
	for e,s in zip(e_delay,s_delay):
		if e==0 or s==0 :
			continue
		elif e-s>-50: 
			e_s.append(e-s)

	##evalute average and summary 
	avg_a_e=0
	avg_a_s=0
	avg_e_s=0
	avg_a_e=sum(a_e)/len(a_e)
	avg_a_s=sum(a_s)/len(a_s)
	avg_e_s=sum(e_s)/len(e_s)
	print e_s
	print 'avg_a_e:'+str(avg_a_e)+' max:'+str(max(a_e))
	print 'avg_a_s:'+str(avg_a_s)+' max:'+str(max(a_s))
	print 'avg_a_s:'+str(avg_e_s)+' max:'+str(max(e_s))
	return [a_e,a_s,e_s,[max(a_e),max(a_s),max(e_s)],[avg_a_e,avg_a_s,avg_e_s]]
def align(time_list):
	## count number of zero because x can't ++ in loop and lead number of loop shorter 
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

data_process()
