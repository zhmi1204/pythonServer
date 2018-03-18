#coding:utf8
#python2 client
import socket

address = ('127.0.0.1',3471)
#创建UDP套接字
udpClientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#关闭后清除端口占用
udpClientSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

while True:
    data = raw_input("input >>> ")
    if not data:
        break
    udpClientSocket.sendto(data,address)
    print 'Client has sent message!waiting for return!"'
    data,address = udpClientSocket.recvfrom(2048)
    print 'received '+ data +' from ',address
udpClientSocket.close()
