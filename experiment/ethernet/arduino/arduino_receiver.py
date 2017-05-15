import socket
import sys
import datetime
import time
import subprocess 
from decimal import Decimal

# Initial server address and port
#host="140.112.28.139"
#host="192.168.11.3"
host="192.168.0.103"
#port=int(sys.argv[2])
port=10005
addr=(host,port)

## sync flag
flag=0
def reply():
    connection.sendto("counter:xxxxxxx",client_address)#request
    T2=time.time()
    #T2=str(datetime.datetime.now())
    #T2=T2.split(":")[2]
    #print "T2: "+T2
    return T2

def sync(T2,T3,C21,C22,C23,R):
    T2=Decimal(T2)
    T3=Decimal(T3)
    C21=Decimal(C21)
    C22=Decimal(C22)
    C23=Decimal(C23)

    R=Decimal(R)*Decimal(0.000001)
    if C23-C22==0:
        C23=C23+4
    delay=((T3-T2)-(C23-C22)*R)/2
    
    T1=T3-delay-(C23-C21)*R
    
    """ debug message
    print "C21:"+str(C21)
    print "T2:"+str(T2)
    print "T3:"+str(T3)
    print "R:"+str(R)
    print "C23-C21: "+str((C23-C21)*R)
    print "delay= "+str(delay)
    print "T3-T2:"+str(T3-T2)
    print "R= "+str(R)
    print "actual T1= "+str(T1)
    print "sync" 
    """

    return T1

if __name__=="__main__":
    
    ## Inital socket property
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ## AF_INET can send data to public IP
    ## sock_stream as TCP
    ## reuse socket immediately
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    ## Bind the socket to the port and ip address
    sock.bind(addr)

    ## Listen for incoming connections
    sock.listen(5)
    
    ##name of file
    filename=sys.argv[1]+".txt"
    '''
    if len(sys.argv[1])==0:
        print "please input arg for file name \n"
    print filename
    '''

    # Wait for a connection
    print('waiting for a connection...')
    
    ## build socket connection
    connection, client_address = sock.accept()
    print('connection from %s:%d' % client_address)       
    
    fo=open(filename,"wb")
    try:
        print "conntection\n"
        while True:
            ## Receive the data one byte at a time
            data = connection.recv(1800)
            print data
            ## receive R at beginning of protocol
            if len(data)==0:
                print "disconnect"
                '''
                connection.close()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connection, client_address = sock.accept()
                '''
            elif len(data)>0 and len(data)<20 :
                 R=data
            elif len(data)>=20 and len(data)<40:
                ## receive c21
            
                T1=time.time() 
                T2=reply()
                clock=data.split(":")[0]
                c21=data.split(":")[2]
                """ debug message
                #print "C21:"+str(c21)
                #print "T1: %.9f"%T1
                """
                ## receive c22,c23
            elif len(data)>=40:
                T3=time.time()
                """ debug message
                print "split[1]: "+str(data.split(":")[2])
                print "split[3]: "+str(data.split(":")[4])
                """

                ##process receive message
                c22=data.split(":")[2]
                c23=data.split(":")[4]
                actual_T1=sync(T2,T3,c21,c22,c23,R)

                #print "clock:"+str(clock)+" T1:"+str(actual_T1)+":rece_T1:%.9f"%T1
                delay=Decimal(T1)-actual_T1
                #print delay
                fo.write("value:"+str(clock)+":"+str(actual_T1)+":rece_T1:"+str(Decimal(T1))+'\n')
            else:
                connection.close()
                print('no more data, closing connection.')
    finally:
        # Clean up the connection
        connection.close()
        fo.close()


