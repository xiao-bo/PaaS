import datetime
import time
import sys
import draw
import numpy
import data_processing as dp

def counter_interval(counter_list):
    list_interval=[]
    for x in range(0,len(counter_list)-1):
        list_interval.append((float(counter_list[x+1])-float(counter_list[x]))/1000000)
    for x in list_interval:
        print x
    return list_interval

def real_clock_interval_for_ms(real_clock_list):
    list_interval=[]
    real_clock_list_us=[]## microsecond
    
    ## get part of time ms because data contain problem, for example
    ## in 10HZ, 9.923 become 10.23  , in fact, 10.23 mean 10.023,
    ## because of ms overflow.
    for x in range(0,len(real_clock_list)-1):
        real_clock_list_us.append(real_clock_list[x].split(".")[1])

    for x in range(0,len(real_clock_list_us)-1):
        interval=float(real_clock_list_us[x+1])-float(real_clock_list_us[x])
        
        ##prevent 1.100-0.99000 , because split time into s , ms,
        ## so above become 0.100-0.99000, and I will skip this situation
        if interval>0.0:
            list_interval.append(interval/10000000)
    return list_interval

def real_clock_interval(real_clock_list):
    list_interval=[]
    for x in range(0,len(real_clock_list)-1):
        list_interval.append(float(real_clock_list[x+1])-float(real_clock_list[x]))
    
    return list_interval

def sampling_bias(list_interval,freq):
    bias=[]
    for x in list_interval:
        bias.append(float(x)-1.0/freq)
    return bias


if __name__=='__main__':
    #readline=open("arduino/arduino.txt","rb")
    readline=open("arduino/arduino_1Hz.txt.txt","rb")
    send_time=[]
    receive_time=[]
    send_interval=[]
    receive_interval=[]
    send_sampling_bias=[]
    receive_sampling_bias=[]
    
    for line in readline:
	send=line.split(":")[0]## for arduino
	send_time.append(send)
        #send_time.append(line)## for edison
	receive=line.split(":")[2]
	receive_time.append(receive)
    
    send_interval=counter_interval(send_time) ##for arduino
    #send_interval=real_clock_interval_for_ms(send_time)## for edison
    send_sampling_bias=sampling_bias(send_interval,1.0)
    

    receive_interval=real_clock_interval(receive_time)
    receive_sampling_bias=sampling_bias(receive_interval,1.0)
    
    title="arduino_sender_sampling_bias(in 1Hz)"
    statistics=[dp.compute_statistics(send_sampling_bias)]
    draw.curve(send_sampling_bias,title,statistics)
    
    title="server_receive_arduino_sampling_bias(in 1Hz)"
    statistics=[dp.compute_statistics(receive_sampling_bias)]
    draw.curve(receive_sampling_bias,title,statistics)
