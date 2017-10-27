
def lazy_sum(*args):
    def sum():
        result = 0
        for x in args:
            result = result + x
        return result
    return sum

f = lazy_sum(*[1, 3, 5])
print(f)
print(f())


t1 = lambda x: x * x
print(t1)
print(t1(5))

def tt(x, y):
    return lambda: x + y

t2 = tt(5,6)
print(t2)
print(t2())