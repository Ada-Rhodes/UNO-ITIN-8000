import zmq

host = '127.0.0.1'
port = 6789
context = zmq.Context()  # create a zmp Context object to maintain state
client = context.socket(zmq.REQ)  # create a REQ (request) socket
client.connect("tcp://%s:%s" % (host, port))  # connect to the server
for num in range(1, 6):
    request_str = "message #%s" % num
    request_bytes = request_str.encode('utf-8')  # encode request string as utf-8
    client.send(request_bytes)  # send string to server
    reply_bytes = client.recv()  # receive reply
    reply_str = reply_bytes.decode('utf-8')  # convert reply to utf-8
    print("Sent %s, received %s" % (request_str, reply_str))  # print reply