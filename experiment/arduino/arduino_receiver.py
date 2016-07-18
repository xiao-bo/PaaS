import socket
import sys
import datetime
import time
import subprocess 

cmd=["ksh -c 'printf \"%(%s.%N)T\"'"]
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# Bind the socket to the port
server_address = ('10.8.0.9', 10005)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
 
try: 
    while True:
        
        filename=sys.argv[1]+"%.txt"
        if len(sys.argv[1])==0:
            print "please input arg for file name \n"
            break
        print filename

        # Wait for a connection
        print('waiting for a connection...')
        connection, client_address = sock.accept()
        print('connection from %s:%d' % client_address)       
        fo=open(filename,"wb")
        try:
            while True:
                # Receive the data one byte at a time
                data = connection.recv(16)
                if data:
                    rece_time=subprocess.check_output(cmd,shell=True)
                    ans=data+':sss:'+str(rece_time)
		    print ans
		    fo.write(ans+'\n')
                else:
                    print('no more data, closing connection.')
                    break
        finally:
            # Clean up the connection
            connection.close()
            fo.close()
except KeyboardInterrupt:
    print('exiting.')
