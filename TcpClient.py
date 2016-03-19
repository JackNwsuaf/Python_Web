import socket

target_host="2001:250:1002:2466:5cc7:3eb1:28b2:e40"
target_port=2015

client=socket.socket(socket.AF_INET6)
client.connect((target_host,target_port))
message=raw_input(":")
while message != "exit":
    client.send(message)
    response=client.recv(1024)
    print response
    message=raw_input(":")
client.send(message)    #Let server receive the message to close the sockset
print response


