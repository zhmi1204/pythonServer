#coding:utf8
#python3 client
import socket

address = ('47.104.188.27',3471)
#创建UDP套接字
udpClientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#关闭后清除端口占用
udpClientSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

while True:
    data = input("input >>> ")
    if not data:
        break
    data = data.encode('utf-8')
    udpClientSocket.sendto(data,address)
    print('Client has sent message!waiting for return!"')
    data,address = udpClientSocket.recvfrom(2048)
    data = data.decode('utf-8')
    print('received '+ data +' from ',address)
udpClientSocket.close()
