# python2
import socket

address=('127.0.0.1',3471)
udpServerSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpServerSock.bind(address)

while True:
    print 'waiting for message'
    data,addr=udpServerSock.recvfrom(2048)
    print("Got message!waiting for re-send!")
    if not data:
        break
    udpServerSock.sendto('Helloworld' ,addr)
    print 'received '+ data +' from ',addr
udpServerSock.close()
