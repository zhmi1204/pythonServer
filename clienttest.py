#coding:utf8
import socket
udpclient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_ip_port=('127.0.0.1',8083)
while True:
	msg=input('>>>')
	udpclient=sendto(msg.encode('utf-8'),server_ip_port)
	data.server_ip=udpclient.recvfrom(1024)
	print(data.decode("utf-8"))

