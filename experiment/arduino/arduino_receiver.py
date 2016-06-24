import socket
import sys
import datetime
import time
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('10.8.0.8', 10005)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
 
try: 
    while True:
        # Wait for a connection
        print('waiting for a connection...')
        connection, client_address = sock.accept()
        print('connection from %s:%d' % client_address)
        fo=open("data.txt","wb")
        try:
            while True:
                # Receive the data one byte at a time
                data = connection.recv(4)
                if data:
                    # Send back in uppercase
					ans=data+' '+str(datetime.datetime.now())
					print ans
					fo.write(ans+'\n')
					#connection.sendall(data.upper())
                else:
                    print('no more data, closing connection.')
                    break
        finally:
            # Clean up the connection
            connection.close()
            fo.close()
except KeyboardInterrupt:
    print('exiting.')
finally:
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
