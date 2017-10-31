import socket, time, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('server is listening...')

def tt(sock, addr):
    print(type(addr))
    print('收到新的连接, %s : %s' % (addr[0], addr[1]))
    sock.send(b'welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('收到消息 %s 准备回发...' % data.decode())
        sock.send(('hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('来自 %s:%s 的连接已关闭' % addr)

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tt, args=(sock, addr))
    t.start()