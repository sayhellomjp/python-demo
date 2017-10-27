import functools

# def now():
#     print("2012-12-12")
#
# now()
# print(now.__name__)
#
# f = now
# print(f.__name__)


# 装饰函数
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("execute %s()" % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def base():
    print("real execution")
    return "done"

print(base())
print(base.__name__)

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("begin call: %s" % text)
            result = func(*args, **kw)
            print("end call: %s" % text)
            return result
        return wrapper
    return decorator

print("---------")

@log2("majunpeng")
def base2():
    print("real execution")
    return "done"

print(base2())
print(base2.__name__)


