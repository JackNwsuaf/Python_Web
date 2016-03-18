import socket

bind_ip="2402:9e80:0:1000::1:f3db"
bind_port=2015

server=socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)
print "[*]Listening on %s:%d" %(bind_ip,bind_port)
client,addr =server.accept()
print "[*]Accepted connection from %s:%d" %(addr[0],addr[1])
request=client.recv(1024)
print "Recived:%s" % request
