import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
print(buffer)
s.close()

print(type(buffer))
print(type(b''.join(buffer)))

data = b''.join(buffer).decode('utf-8')
header, html = data.split("\r\n\r\n", 1)


print('---')
print("header:", header)
print("html:", html)

b = b'dddd 111111'
b1, b2 = b.split(b' ', 1)
print(b1)
print(b2)