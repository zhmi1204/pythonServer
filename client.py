#coding:utf8

#python2
import socket

# address = ('47.104.188.27',31204)
# address = ('47.95.233.40',31204)
# address = ('172.16.252.50',180)
# address = ('106.39.0.94',180)
# address = ('127.0.0.1',50000)
#3471/udp
address = ('47.95.233.40',3471)
udpClientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# udpClientSocket.bind(address)
while True:
    data = raw_input("input >>> ")
    if not data:
        break
    udpClientSocket.sendto(data,address)
    data,address = udpClientSocket.recvfrom(2048)
    print 'received '+ data +' from ',address
udpClientSocket.close()
