import socket
import sys
import datetime 
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('10.8.0.35', 10005)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
 
try: 
    while True:
        # Wait for a connection
        print('waiting for a connection...')
        connection, client_address = sock.accept()
        print('connection from %s:%d' % client_address)
        fo=open("arduino_data.txt","wb")
        try:
            while True:
                # Receive the data one byte at a time
                data = connection.recv(3)
                #sys.stdout.write(data)
                if data:
                    # Send back in uppercase
					#print data
					#print datetime.datetime.now()
					ans=data+' '+str(datetime.datetime.now())
					print ans
					fo.write(ans+'\n')
					connection.sendall(data.upper())
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
