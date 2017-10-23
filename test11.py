
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