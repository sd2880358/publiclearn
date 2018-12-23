import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(('127.0.0.1', 8000))
print('已经绑定端口')

sock.listen()

skt, addr = sock.accept()
print('已经收到传入socket:{0}'.format(skt))

msg = skt.recv(100)
print('已经收到消息')
print(type(msg))

print(msg.decode())

msgre = 'I am your father'
print('成功编辑消息')
skt.send(msgre.encode())

rst = {}

def getline(skt):

    b1 = skt.recv(1)
    b2 = 0
    date = b''
    while b2 != b'\r' and b1 != b'\n':
        b2 = b1
        # a += 1
        b1 = skt.recv(1)
        date += bytes(b2)

    date.strip(b'\r')
    return date.decode()

def getHttpHeader(skt):

    line = getline(skt)
    while line:
        r = line.split(r': ')
        if len(r) == 2:
            rst[r[0]] = r[1]
        else:
            r = line.split(r' ')
            print(r)
        line = getline(skt)
    return rst



getHttpHeader(skt)
skt.close()
sock.close()




