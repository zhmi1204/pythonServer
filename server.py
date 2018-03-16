# python2
import socket
from time import ctime
import time
import threading
import sys
#3471/udp
address=('127.0.0.1',3471)
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
    print("Got message!waiting for re-send!")
    if not data:
        break
    # udpServerSock.sendto('[%s]%s' %(ctime(),data),addr)
    udpServerSock.sendto('Helloworld' ,addr)
    print 'received '+ data +' from ',addr
udpServerSock.close()
