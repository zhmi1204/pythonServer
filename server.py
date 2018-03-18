#coding:utf8
# python2 server
import socket

address=('0.0.0.0',3471)
udpServerSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#server关闭后清除port占用
udpServerSock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 端口绑定
udpServerSock.bind(address)
while True:
    print 'waiting for message'
    data,addr=udpServerSock.recvfrom(2048)
    print 'Got message!waiting for re-send!'
    if not data:
        break
    udpServerSock.sendto('Helloworld' ,addr)
    print 'received '+ data +' from ',addr
udpServerSock.close()