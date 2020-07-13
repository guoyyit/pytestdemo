#Python3 网络编程
import socket
from socket import *
from time import ctime
import sys
#创建 socket 对象
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#获取本地主机名
host = socket.gethostname()
print(host)
port = 9999
# 连接服务，指定主机和端口
clientsocket.connect((host, port))
# 接收小于 1024 字节的数据
msg = clientsocket.recv(1024)
clientsocket.close()
print(msg.decode('utf-8'))

#TCP
HOST = '192.168.164.141' #服务端ip
PORT = 21566 #服务端端口号
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM) #创建socket对象
tcpCliSock.connect(ADDR) #连接服务器
while True:
    data = input('>>').strip()
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8')) #发送消息
    data = tcpCliSock.recv(BUFSIZ) #读取消息
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close() #关闭客户端