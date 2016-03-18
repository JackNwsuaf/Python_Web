import socket

target_host="vhacker.me"
target_port=2015

client=socket.socket(socket.AF_INET6)
client.connect((target_host,target_port))
client.send("Hello!")
response=client.recv(1024)
print response

