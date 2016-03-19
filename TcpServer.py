import socket
import threading
bind_ip="2001:250:1002:2466:5cc7:3eb1:28b2:e40"
bind_port=2015

def handle_client(client_socket):
    request=client.recv(1024)
    while request != "exit":
        print "Recived:%s" % request
        client_socket.send("Accpted")
        request=client.recv(1024)
   # client_socket.send("See you!") #client has closed
    client_socket.close()

server=socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(64)
print "[*]Listening on %s:%d" %(bind_ip,bind_port)
client,addr =server.accept()
print "[*]Accepted connection from [%s]:%d" %(addr[0],addr[1])
client_handler=threading.Thread(target=handle_client,args=(client,))
client_handler.start()
