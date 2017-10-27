from enum import Enum, unique

Month = Enum("Month_", ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    Test = 'Test'

print(Weekday.Sun)
print(Weekday.Sun.value)
print(Weekday['Sat'])
print(Weekday('Test'))

def fn(self, name='World'):
    print("Hello, %s" % name)

Hello = type('Hello', (object,), dict(hello=fn))

s = Hello()
s.hello()