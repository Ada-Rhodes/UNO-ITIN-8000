import socket
from datetime import datetime

server_address = ('localhost', 6789)  # set server address to localhost and port to 6789
max_size = 4096  # set max message size to 4096 bytes

print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create a socket to send a datagram
client.sendto(b'Hey!', server_address)  # send message to server
data, server = client.recvfrom(max_size)  # receive message back from the server
print('At', datetime.now(), server, 'said', data)  # print message back from server
client.close()  #close the client
