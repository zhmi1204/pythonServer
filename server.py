# python2
import socket
from time import ctime
import time
import threading
import sys

address=('127.0.0.1',50583)
udpServerSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpServerSock.bind(address)

# def thread_wait():
#     thread = threading.Thread
#
# def thread_print():b
#     pass

while True:
    print 'waiting for message'
    data,addr=udpServerSock.recvfrom(2018)
    if not data:
        break
    # udpServerSock.sendto('[%s]%s' %(ctime(),data),addr)
    udpServerSock.sendto('Helloworld' ,addr)
    print 'received '+ data +' from ',addr
udpServerSock.close()
