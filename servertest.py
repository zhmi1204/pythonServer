#coding:utf8

#python3

import socketserver
class My_server(socketserver.BaseRequestHandler):
	def handle(self):
		data=self.request[0]
		print(data.decode('utf-8'))
		print(self.client_address,self.request[1])
		self.request[1].sendto('bbbb'.encode('utf-8'),self.client_address)
if __name__ == "__main__":
	ip_port=('127.0.0.1',8083)
	obj=socketserver.ThreadingUDPServer(ip_port,My_server)
	obj.serve_forever()
