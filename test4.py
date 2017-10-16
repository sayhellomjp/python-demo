import math
from test3 import add

result = add(1, 2)
print(result)

def move(x, y, step, angle = 0):
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("error")

    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

result = move(100, 100, 60, math.pi / 6)
print(result)
print(result[0])
print(result[1])


def test(l=None):
    if l == None:
        l = []
    l.append("end")
    return l

t = test()
t = test()
print(t)

def cal(*nums):
    sum = 0
    for n in nums:
        sum = sum + n * n
    return sum

print(cal(1, 2, 3))
print(cal(1, 2))
print(cal(*[1, 2, 5]))

def person(name, age, **extra):
    print("name:", name, "age:", age, "extra:", extra)

person("majunpeng", 16)
person("mjp", 20, city="chengdu", province="sichuan")
person("mjp", 20, **{"city": "emei", "province": "sichuan"})
extra = {"s": 12}
person("rtt", 19, **extra)

def person1(name, age, *, city="cd", province="sc"):
    print("name:", name, "age:", age, "city:", city, "province:", province)

person1("tt", 20)
person1("tt", 20, city="emei")

def person2(name, age, *args, city="cd", province="sc"):
    print("name:", name, "age:", age, "args:", args, "city:", city, "province:", province)

person2("t", 99, "yy", 66, city="shanghai")