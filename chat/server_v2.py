#python socket server by Leo Chen
import socket,_thread,time as t,os
n=socket.gethostname()
host=socket.gethostbyname(n)
print('server ip: '+host)
print('server name: '+n)
port=int(input('enter port: '))
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)
print('you might want to check your firewall settings and other\npossible problems and fix them')
print('server starts')
file=open('msgs.txt','a+')
file=open('msgs.txt','r')
checkf=open('check.py','w+')
code='''MAX=500
while True:
    file=open('msgs.txt','r')
    msg=file.readlines()
    if len(msg)>MAX:
        print('cleaning file...')
        file=open('msgs.txt','r')
        L=file.readlines()
        bla=''
        for i in range(len(L)-MAX,len(L)):
            bla+=L[i]
            file2=open('msgs.txt','w')
            file2.write(bla)
            file.close()
            file2.close()
        file=open('msgs.txt','r')
        L=file.readlines()
        msg=L
        file.close()'''
checkf.write(code)
checkf.close()
os.startfile('check.py')
msg=file.readlines()
R_users=[]
S_users=[]
def stuff(users1,users2,client):
    try:
        if client in users1:
            users1.remove(client)
        elif client in users2:
            users2.remove(client)
    except:
        stuff(users1,users2,client)
def handle(client,addr):
    global S_users
    global R_users
    global msg
    try:
        conmsg='ip: <'+addr[0]+'> has connected\n'
        print(conmsg)
        time=t.strftime('%Y/%m/%d %H:%M:%S',t.localtime())
        file=open('msgs.txt','a+')
        file.write('<'+addr[0]+'>'+': '+conmsg+'\n\n'+time+'\n\n')
        file.close()
        file=open('msgs.txt','r')
        msg=file.readlines()
        file.close()
        mode=client.recv(1024)
        for j in R_users:
            j.send(('<'+addr[0]+'>'+': '+conmsg+'\n\n'+time+'\n\n').encode())
            j.recv(1024)
        if mode==b'r':
            R_users.append(client)
            print('send mode users: ',len(S_users))
            print('read mode users: ',len(R_users))
            for i in msg:
                client.send(i.encode())
                client.recv(1024)
            while True:
                #To purposely create error when connection is closed
                #This is done to make the program run smoothly
                client.send(b' ')
                client.recv(1024)
        elif mode==b's':
            S_users.append(client)
            print('read mode users: ',len(R_users))
            print('send mode users: ',len(S_users))
            while True:
                cmsg=client.recv(1024).decode()
                client.send(b'confirm')
                time=t.strftime('%Y/%m/%d %H:%M:%S',t.localtime())
                file=open('msgs.txt','a+')
                file.write('<'+addr[0]+'>'+': '+cmsg+'\n\n'+time+'\n\n')
                file.close()
                file=open('msgs.txt','r')
                msg=file.readlines()
                file.close()
                for j in R_users:
                    j.send(('<'+addr[0]+'>'+': '+cmsg+'\n\n'+time+'\n\n').encode())
                    j.recv(1024)
    except Exception as e:
        print(e)
        dismsg='ip: <'+addr[0]+'> has disconnected\n'
        print(dismsg)
        stuff(R_users,S_users,client)
        print('read mode users: ',len(R_users))
        print('send mode users: ',len(S_users))
        time=t.strftime('%Y/%m/%d %H:%M:%S',t.localtime())
        file=open('msgs.txt','a+')
        file.write('<'+addr[0]+'>'+': '+dismsg+'\n\n'+time+'\n\n')
        file.close()
        file=open('msgs.txt','r')
        msg=file.readlines()
        file.close()
        for j in R_users:
            j.send(('<'+addr[0]+'>'+': '+dismsg+'\n\n'+time+'\n\n').encode())
            j.recv(1024)
def start_server():
    while True:
        client,addr=server.accept()
        _thread.start_new_thread(handle,(client,addr,))
start_server()
