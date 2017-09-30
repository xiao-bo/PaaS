import sys
import numpy

def read_file(filename,index):
    ##read data and append list
    file_read=open(filename,'r')
    timestamp=[]
    for line in file_read:
        ans=line.split(":")[index]
        timestamp.append(float(ans))
    return timestamp

def compute_statistics(delay_list):
    ##evalute average , standard deviation, mean square error
    delay_list=numpy.array(delay_list)
    print "mean: "+str(numpy.mean(delay_list))
    print "standard deviation: "+str(numpy.std(delay_list))
    return [numpy.mean(delay_list),numpy.std(delay_list)]

    return delay
