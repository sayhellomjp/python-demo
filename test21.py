from datetime import datetime
from collections import namedtuple, deque, defaultdict
import base64

print(datetime.now())
print(datetime.now().timestamp())
print(datetime(2015, 5, 15, 14, 12, 36))

t = 1509346975.007392
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

print(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))

Point = namedtuple('Point', ['x', 'y'])
p = Point(20, 30)
print(p)
print(p.x, p.y)

Circle =namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(15, 20, 5)
print(c)

q = deque(['A', 'B', 3])
print(q)
q.append(6)
print(q)
q.appendleft(77)
print(q)
q.pop()
print(q)
q.popleft()
print(q)

d = defaultdict(lambda: 'error', a=1, b=2)
print(d)
print(d['a'])
print(d['c'])

def base64_decode_my(str):
    num = len(str)%4
    if num:
        for i in range(num):
            str = str + b"="
    print(str)
    return base64.b64decode(str)

rr = base64_decode_my(b'YWJjZA')
print(rr)

print(base64.b64encode('东方'.encode(encoding="utf-8")))
print(base64.b64decode('5Lic5pa5'))

base_str = "我已经将我的狗狗送人了"
print(type(base_str))

bytes_utf_8 = base_str.encode(encoding="utf-8")
print(bytes_utf_8)
