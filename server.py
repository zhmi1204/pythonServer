# python3
from socket import *
from time import ctime

# host = ''
# port = 12345
# bufsize = 1024
# addr = (host,port)
#
# udpServer = socket(AF_INET,SOCK_DGRAM)
# udpServer.bind(addr)
#
# while True:
#     print("waiting for connecting...")
#     data,addr = udpServer.recvfrom(bufsize)
#     data = data.decode(encoding='utf-8').upper()
#     data = "at %s : %s "%(ctime(),data)
#     udpServer.sendto(data.encode('utf-8'),addr)
#     print("received from and return to :",addr)
#
# udpServer.close()

# dwhadwadwad
# python2
import socket
from time import ctime

buffer=2048
address=('127.0.0.1',31204)
udpServerSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# udpsock.listen(5)
udpServerSock.bind(address)
while True:
    print 'waiting for message...'
    data,addr=udpServerSock.recvfrom(buffer)
    udpServerSock.sendto('[%s]%s' %(ctime(),data),addr)
    print 'received data '+ data +' from and retuned ',addr
udpServerSock.close()
