from socket import *
from time import ctime

host = ''
port = 12345
bufsize = 1024
addr = (host,port)

udpServer = socket(AF_INET,SOCK_DGRAM)
udpServer.bind(addr)

while True:
    print("waiting for connecting...")
    data,addr = udpServer.recvfrom(bufsize)
    data = data.decode(encoding='utf-8').upper()
    data = "at %s : %s "%(ctime(),data)
    udpServer.sendto(data.encode('utf-8'),addr)
    print("received from and return to :",addr)

udpServer.close()

