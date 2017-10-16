def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(1))
print(fact(2))
print(fact(3))


def hanoi(n, a, b, c):
    if n == 1:  # 1个环的情况，也是递归的出口
        print(a, '->', c)
    else:  # n > 1时，用抽象出的3步来移动
        hanoi(n - 1, a, c, b)  # 将n-1个环从a移动到b上
        print(a, '->', c)  # 将底盘从a移动到c上
        hanoi(n - 1, b, a, c)  # 将b上的n-1个环移动到c上


hanoi(3, 'a', 'b', 'c')
