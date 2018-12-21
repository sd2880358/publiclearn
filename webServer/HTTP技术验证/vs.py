import socket
import time
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(('127.0.0.1', 8080))
print('已经绑定端口')

sock.listen()

skt, addr = sock.accept()
print('已经收到传入socket:{0}'.format(addr))

msg = skt.recv(100)
print('已经收到消息')
print(type(msg))

print(msg.decode())

msgre = 'I am your father'
print('成功编辑消息')
skt.send(msgre.encode())

time.sleep(10)
skt.close()
sock.close()


