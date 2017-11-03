
# def upper_attr(class_name, class_parents, class_attr):
#     # 排除所有__开头的属性
#     array = [(name, value) for name, value in class_attr.items() if not name.startswith('__')]
#     upper_array = [(name.upper(), value) for name, value in array]
#     upper_attr = dict(upper_array)
#     return type(class_name, class_parents, upper_attr)
#
# __metaclass__ = upper_attr
#
# class Foo(object):
#     bar = "pip"
#
# print(hasattr(Foo, 'bar'))
# print(hasattr(Foo, 'BAR'))
# f = Foo()
# print(f.BAR)

class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, attr):
        array = [(name, value) for name, value in attr.items() if not name.startswith('__')]
        upper_array = [(name.upper(), value) for name, value in array]
        upper_attr = dict(upper_array)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, upper_attr)

class Foo(object, metaclass=UpperAttrMetaclass):
    bar = 'pip'

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))
f = Foo()
print(f.BAR)

class Test(dict):
    pass

print(Test.mro())