def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("type error")
    return a + b

def doAdd():
    a = 1
    b = 2
    result = add(a, b)
    print(result)

def test():
    pass

print(test())

# print(add('1', 'aaa'))