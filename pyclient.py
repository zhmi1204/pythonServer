# coding=utf-8

#python2

import socket

s = socket.socket()  # 生成一个socket对象
server = socket.gethostname()
port = 3471
s.connect((server, port))  # 连接服务器
print s.recv(1024)  # 读取数据
s.close()  # 关闭连接