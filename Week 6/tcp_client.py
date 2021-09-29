import socket
from datetime import datetime

address = ('localhost', 6789)  # define server id and port
max_size = 1000  # set max size to 1000 bytes

print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create default socket instance with TCP (SOCK_STREAM)
client.connect(address)  # connect to the server address
client.sendall(b'Hey!')  # send a stream of data and maintain connection
data = client.recv(max_size)  # max receive message from server of up to 1000 bytes
print('At', datetime.now(), 'someone replied', data)  # print response
client.close()  # close client
