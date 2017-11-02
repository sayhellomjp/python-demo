from collections import namedtuple

def test1():
    yield range(10)

def test2():
    yield from range(10)

t1 = test1()
t2 = test2()

print([x for x in t1])
print([x for x in t2])

print('----')

Result = namedtuple('Result', ['count', 'average'])

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        # main 函数发送数据到这里
        term = yield
        if term is None: # 终止条件
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average) # 返回的Result 会成为grouper函数中yield from表达式的值

def grouper():
    n = 0
    result_list = []
    r = yield from averager()
    result_list.append(r)
    print(result_list)
g = grouper()
# 激活 运行至25行暂停，等待next或者send
next(g)
# 发送值 直接到25行，term为25 继续向下运行，然后第二次迭代到24行，再次暂停并等待
g.send(15)
# 同上
g.send(20)
# send(None)意味赋值给24行term为None，进入终止条件，break，跳出循环并return，此时37行激活，r被赋值为刚刚返回的Result
try:
    g.send(None)
except StopIteration as exc:
    print(exc.value)