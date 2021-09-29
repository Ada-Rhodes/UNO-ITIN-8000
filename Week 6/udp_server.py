from datetime import  datetime
import socket

server_address = ('localhost', 6789) # set server address to localhost and port to 6789
max_size = 4096 # set max size in bytes

print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # creates a socket instance, default address family = AF_INET, socket type datagram = SOCK_DGRAM
server.bind(server_address) # assigns an IP address and a port number to a socket instance

data, client = server.recvfrom(max_size) #receive data from the socket, size in bytes

print('AT', datetime.now(), client, 'said', data)
server.sendto(b'Are you talking to me?', client)
server.close()
