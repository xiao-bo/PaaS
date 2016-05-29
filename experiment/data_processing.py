### arduino timestamp
file_read=open('arduino/arduino_data.txt','r')
#print f.read()
time_arduino=[]
for line in file_read:
	time_arduino.append(float(line.split()[1]))
print time_arduino

### edison timestamp
file_read=open('edison/edison_data.txt','r')
time_edison=[]
for line in file_read:
	time_edison.append(float(line.split()[1]))
print time_edison


for a,e in zip(time_arduino,time_edison):
	print a-e
	
