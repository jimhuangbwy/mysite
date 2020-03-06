#python socket user by Leo Chen
import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((input('enter host ip: '),int(input('port: '))))
server.send(b's')
print('connected')
name=input('enter name: ')
while True:
    server.send((name+': '+input('enter message: ')).encode())
    server.recv(1024)
