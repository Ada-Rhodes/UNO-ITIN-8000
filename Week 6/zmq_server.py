import zmq  # you need to install with pip install pyzmq

host = '127.0.0.1'
port = 6789
context = zmq.Context()  # the Context object is a ZMQ object that maintains state
server = context.socket(zmq.REP)  # create a zmq socket of the REP (reply) type
server.bind("tcp://%s:%s" % (host, port))  # bind server socket to host ip address and port
while True:  # hold open and keep waiting for signals
    #  Wait for next request from client
    request_bytes = server.recv()  # get a request (message from client) and record it
    request_str = request_bytes.decode('utf-8')  # decode it from utf-8 to a string
    print("That voice in my head says: %s" % request_str)
    reply_str = "Stop saying: %s" % request_str  # create a reply to the request
    reply_bytes = bytes(reply_str, 'utf-8')  # encode the reply to utf-8
    server.send(reply_bytes)  # send the reply back to the client

# what did we not do?
