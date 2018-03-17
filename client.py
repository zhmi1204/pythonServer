#coding:utf8

#python2
import socket

address = ('47.104.188.40',3471)
udpClientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data = raw_input("input >>> ")
    if not data:
        break
    udpClientSocket.sendto(data,address)
    print("Client has sent message!waiting for return!")
    data,address = udpClientSocket.recvfrom(2048)
    print 'received '+ data +' from ',address
udpClientSocket.close()
