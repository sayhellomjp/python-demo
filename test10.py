from functools import reduce

def add(x, y, f):
    return f(x) + f(y)

result = add(5, 12, abs)
print(result)

def f(x):
    return x * x

l1 = [2, 4, 6, 8]
l2 = list(map(f, [2, 4, 6, 8]))
print("l1:", l1)
print("l2:", l2)

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def fn(x, y):
    return x * 10 + y

print(list(map(char2num, '13579')))

print(reduce(fn, map(char2num, '13579')))
print(reduce(fn, list(map(char2num, '13579'))))

print("----")

test1 = ['adam', 'LISA', 'barT']
def normalize(name):
    if name:
        name = name.capitalize()
        # name = name[:1].upper() + name[1:].lower()
    return name

resultTest1 = list(map(normalize, test1))
print(resultTest1)

def prod(L):
    def f(x, y):
        return x * y
    return reduce(f, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def is_odd(num):
    return num % 2 == 1

print(list(filter(is_odd, [2, 3, 5, 6, 8, 9])))

def not_empty(str):
    return str and str.strip()

print(list(filter(not_empty, ['A', 'B', "C  ", None, '  '])))

test2 = [36, 5, -12, 9, -21]
print(sorted(test2, key=abs))

test3 = ["Abc", "Zero", "majunpeng", "Rtt"]
print(list(sorted(test3, key=str.lower, reverse=True)))