
class SayMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['say_' + name] = lambda self, value='world', first=name: print('%s, %s' % (first, value))
        attrs['age'] = 1
        return type.__new__(cls, name, bases, attrs)

class C1(object, metaclass=SayMetaClass):
    pass

class C2(object, metaclass=SayMetaClass):
    pass

c1 = C1()
c1.say_C1('mjp')
print(c1.age)

c2 = C2()
c2.say_C2('rtt')
print(c2.age)