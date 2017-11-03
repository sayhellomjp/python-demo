class Student(object):
    def say_hello(self, name='world'):
        print('hello %s' % name)

s = Student()
s.say_hello()

def fn(self, name='world'):
    print('hello %s' % name)
Stduent1 = type('Stduent1', (object,), dict(test=fn))

s1 = Stduent1()
s1.test('mjp')

t1 = lambda a, b, c='mjp': print('%s %s %s' % (a, b, c))
t1('first', 'second', 'rtt')