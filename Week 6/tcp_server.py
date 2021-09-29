from datetime import datetime
import socket

address = ('localhost', 6789)  # set address and port for the server
max_size = 1000  # set max message size to 1000 bytes

print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # initiate default socket for TCP (SOCK_STREAM)
server.bind(address)  # bind the address for the server to listen for incoming messges
server.listen(5)  # it will queue up to 5 client connections before refusing new ones

client, addr = server.accept()  # get client id and port
data = client.recv(max_size)  # receive the message from the client

print('At', datetime.now(), client, 'said', data)
client.sendall(b'Are you talking to me?')  # stream the string to the client
client.close()  # close the client connection
server.close()  # close the server
