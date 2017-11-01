
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