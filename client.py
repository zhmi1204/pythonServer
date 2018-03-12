from socket import *

# PC端公网IP为106.39.0.94
host = '192.168.1.1'
port =12345
bufsize = 1024

addr = (host,port)
udpClient = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input('>>>')
    if not data:
        break
    data = data.encode(encoding="utf-8")
    udpClient.sendto(data,addr)
    data.addr = udpClient.recvfrom(bufsize)
    print(data.decode(encoding="utf-8"),'from',addr)

udpClient.close()