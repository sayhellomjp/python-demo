import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print('bind udp to 9999')

while True:
    data, addr = s.recvfrom(1024)
    print('receive data from %s:%s' % addr)
    print('data: %s' % data.decode('utf-8'))
    s.sendto(b'hello, mjp', addr)