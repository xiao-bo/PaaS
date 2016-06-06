
def data_process():
	### arduino timestamp
	file_read=open('arduino/data.txt','r')
	#print f.read()
	time_arduino=[]
	for line in file_read:
		#value=float(line.split(" ")[0])
		#if value!=0.0:
		ans=line.split(":")[2]
		time_arduino.append(float(ans))
			#print ans
	#print time_arduin
	print '==========='
	### edison timestamp
	file_read=open('edison/data.txt','r')
	#file_read=open('serial/serial_data.txt','r')
	time_edison=[]
	for line in file_read:
		#value=float(line.split(" ")[0])
		#if value!=0.0:

		ans=float(line.split(":")[2])
		time_edison.append(ans)
	### serial timestamp

	file_read=open('serial/data.txt','r')
	time_serial=[]
	for line in file_read:
		#print line
		#value=float(line.split(" ")[0])
		#if value!=0.0:
		ans=float(line.split(":")[2])
		time_serial.append(float(line.split(":")[2]))
			#print ans
	ans=[]
	"""
	for a,e in zip(time_arduino,time_serial):
		#e=e+13.40
		if abs(a-e)<50:
			#a=a+60
			ans.append(a-e)
			#print a-e
	#print ans
	#return ans
	"""
	a_delay=[]
	for x in range(0,len(time_arduino)-1):
		a_delay.append(time_arduino[x+1]-time_arduino[x])
	s_delay=[]
	for x in range(0,len(time_serial)-1):
		s_delay.append(time_serial[x+1]-time_serial[x])
	e_delay=[]
	for x in range(0,len(time_edison)-1):
		e_delay.append(time_edison[x+1]-time_edison[x])
	"""
	as_delay=[]
	for a,s in zip(a_delay,s_delay):
		if abs(a-s)<50:
			as_delay.append(a-s)
			#print a-s
	print max(as_delay)
	print sum(as_delay)/len(as_delay)
	return as_delay
	ae_delay=[]
	for a,e in zip(a_delay,e_delay):
		if abs(a-e)<50:
			ae_delay.append(a-e)
	pos=0
	neg=0
	for x in ae_delay:
		if x>0:
			pos=pos+1
		else:
			neg=neg+1
	print 'pos: '+str(pos)+'neg: '+str(neg)
	print max(ae_delay)
	print min(ae_delay)
	print sum(ae_delay)/len(ae_delay)
	return ae_delay
	"""
	es_delay=[]
	for e,s in zip(e_delay,s_delay):
		if abs(e-s)<50:
			es_delay.append(e-s)
	pos=0
	neg=0
	for x in es_delay:
		if x>0:
			pos=pos+1
		else:
			neg=neg+1
	print 'pos: '+str(pos)+'neg: '+str(neg)
	print max(es_delay)
	print min(es_delay)
	print sum(es_delay)/len(es_delay)
	return es_delay
data_process()
