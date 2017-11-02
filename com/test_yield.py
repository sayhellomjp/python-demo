
list = [x*x for x in range(10)]
print(list)

list1 = (x*2 for x in range(5))
print(list1)
# 第一次迭代
print('first for')
for x in list1:
    print(x)
# 第二次迭代
print('second for')
for x in list1:
    print(x)

# 协程
def consumer():
    print('init consumer')
    r = 'r: first init'
    while True:
        n = yield r
        if not n:
            break
        print('[consumer] n: %s' % n)
        r = '200 ok'

def provider(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[provider] n: %s' % n)
        r = c.send(n)
        print('[provider] receive result: %s' % r)
    c.close()

c = consumer()
provider(c)

# yield from
def t1():
    for x in range(10):
        yield x
f = t1()
print(f)

for x in f:
    print(x)

def test():
    yield from range(1, 5)

ff = test()
for x in ff:
    print(x)

print('----')

def test1():
    count = 0
    print('count %d' % count)
    a = yield
    print('a %d' % a)

a1 = test1()
next(a1)
a1.send(20)

