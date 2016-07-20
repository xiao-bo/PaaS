import socket
import sys
import datetime
import time
import subprocess 
from decimal import Decimal

cmd=["ksh -c 'printf \"%(%s.%N)T\"'"]
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# Bind the socket to the port
server_address = ('10.8.0.9', 10005)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
i=0

def reply():
    connection.sendto("c",client_address)#request
    T2=time.time()
    #T2=str(datetime.datetime.now())
    #T2=T2.split(":")[2]
    #print "T2: "+T2
    return T2

def sync(T2,T3,C21,C22,C23):
    T2=Decimal(T2)
    T3=Decimal(T3)
    C21=Decimal(C21)
    C22=Decimal(C22)
    C23=Decimal(C23)
    R=Decimal(0.000001)
    #delay=((T3-T2)-(C23-C22)/1000000)/2
    delay=((T3-T2)-(C23-C22)*R)/2
    #R=(T3-T2-2*delay)/(C23-C22)
    T1=T3-delay-(C23-C21)*R
    #print "delay= "+str(delay)
    #print "R= "+str(R)
    #print "actual T1= "+str(T1)
    #print "sync" 
    return T1
try: 
    while True:
        """ 
        filename=sys.argv[1]+"%.txt"
        if len(sys.argv[1])==0:
            print "please input arg for file name \n"
            break
        print filename
        """
        filename="11.txt"
        # Wait for a connection
        print('waiting for a connection...')
        connection, client_address = sock.accept()
        print('connection from %s:%d' % client_address)       
        fo=open(filename,"wb")
        try:
            print "conntection\n"
            while True:
                # Receive the data one byte at a time
                data = connection.recv(60)
                T1=time.time() 
                if len(data)>=5 and len(data)<40:
                    c21=data.split(":")[1]
                    #T1=rece_time.split(":")[2]
		    #fo.write(ans+'\n')
                    #T2=reply()
                    #print "C21:"+str(c21)
                    print "T1: %.20f"%T1
                    #print "T2:"+str(T2)
                elif len(data)>=40:
                    #print data
                    #T3=str(datetime.datetime.now())
                    T3=time.time()
                    #T3=T3.split(":")[2]
                    #print "T3:"+T3
                    """ debug message
                    print "split[1]: "+str(data.split(":")[1])
                    print "split[3]: "+str(data.split(":")[3])
                    """
                    c22=data.split(":")[1]
                    c23=data.split(":")[3]
                    actual_T1=sync(T2,T3,c21,c22,c23)
                    print "actual_T1: "+str(actual_T1)+":rece_T1:%.20f"%T1
                    fo.write("actual_T1: "+str(actual_T1)+":rece_T1:"+str(T1)+'\n')
                else:
                    print('no more data, closing connection.')
                    break 
        finally:
            # Clean up the connection
            connection.close()
            fo.close()
except KeyboardInterrupt:
    print('exiting.')


