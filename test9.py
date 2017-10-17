from collections import Iterable

t1 = [x for x in range(10)]
print(t1)

t2 = (x * x for x in range(10))
print(t2)
print(isinstance(t2, Iterable))

for x in t2:
    print(x)

# 1, 1, 2, 3, 5, 8, 13, 21, 34

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        # temp = b
        # b = a + b
        # a = temp
        # 可简化为如下写法
        a, b = b, a + b

        n = n + 1
    return "done"

fib(6)

print("---")
def fibgenerator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return "done"

g1 = fibgenerator(10)
g2 = fibgenerator(5)
print(g1)
for x in g1:
    print(x)

print("")
while True:
    try:
        v = next(g2)
        print("v:", v)
    except StopIteration as e:
        print("error:", e.value)
        break

print("---")

def test1():
    print("step1")
    yield 1
    print("step2")
    yield 2
    print("step3")
    yield 3

o = test1()
next(o)
next(o)
next(o)