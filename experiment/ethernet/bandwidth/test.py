file_obj = open('downloaded.ext', 'wb')
interval = 1.0 # seconds eg. 0.5 or 2.0
# smaller the interval, the less bursty and smoother the throughput
max_speed = 51200 # 50k * 1024 = bytes
data_count = 0 # keep track of the amount of data transferred
time_next = time.time() + interval
while 1:
	buf = sock.recv(512) # smaller chunks = smoother, more accurate
	if len(buf) == 0:
		break
	data_count += len(buf)
	if data_count >= max_speed * interval:
		data_count = 0
		sleep_for = time_next - time.time()
	if sleep_for !=0:
		time.sleep(sleep_for)
	time_next = time.time() + interval
	file_obj.write(buf)
file_obj.close()
sock.close()