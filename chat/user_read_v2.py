#python socket user by Leo Chen
import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((input('enter host ip: '),int(input('port: '))))
server.send(b'r')
print('connected')
while True:
    msg=server.recv(1024).decode()
    if msg!=' ':
        print(msg)
    server.send(b'online')
