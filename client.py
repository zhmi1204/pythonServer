#coding:utf8
# python3
# from socket import *
#
# # PC端公网IP为106.39.0.94
# host = '47.95.233.40'
# port =12345
# bufsize = 1024
#
# addr = (host,port)
# udpClient = socket(AF_INET,SOCK_DGRAM)
#
# while True:
#     data = input('>>>')
#     # if not data:
#     #     break
#     data = data.encode(encoding="utf-8")
#     udpClient.sendto(data,addr)
#     data.addr = udpClient.recvfrom(bufsize)
#     print(data.decode(encoding="utf-8"),'from',addr)
#     # print(data,addr)
#
# udpClient.close()

#python2
import socket

address = ('47.95.233.40',80)
# address = ('172.16.252.50',180)
# address = ('106.39.0.94',180)
# address = ('127.0.0.1',10372)
udpClientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# udpClientSocket.bind(address)
while True:
    data = raw_input("input >>> ")
    if not data:
        break
    udpClientSocket.sendto(data,address)
    data,address = udpClientSocket.recvfrom(2048)
    print 'received data ----- '+ data +' ----- from and retuned to addr ----- ',address
udpClientSocket.close()
