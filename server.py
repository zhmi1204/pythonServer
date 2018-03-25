#coding:utf8
# python server
import socket
import pymysql

def saveInf(data):
	conn = pymysql.connect(host='localhost',user='root',password='root',charset='utf8',port=3306,database='pythonServer')
	cur = conn.cursor()
	sql = "insert into received (text) values " + (str(data))
	cur.execute(sql)
	conn.commit()
	cur.close()
	conn.close()

address=('0.0.0.0',3471)
udpServerSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpServerSock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
udpServerSock.bind(address)
conn = pymysql.connect(host='localhost',user='root',password='root',charset='utf8',port=3306,database='pythonServer')
cur = conn.cursor()
while True:
	print('waiting for message')
	data,addr=udpServerSock.recvfrom(2048)
	data = data.decode('utf-8')
	sql = "insert into received(text) values(%s)"
	cur.execute(sql,data)
	conn.commit()
	print('Got message!')
	if not data:
		break
	string=str(data) + "--- from---  " +str(addr)
	print('received '+ data +' from ',addr)
	data = data.encode('utf-8')
	udpServerSock.sendto(data,addr)
cur.close()
conn.close()
udpServerSock.close()
