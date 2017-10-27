
class Animal:
    def run(self):
        print("animal running")

class Dog(Animal):
    def __init__(self):
        self.x = 9

    def run(self):
        print("dog running")

class Cat(Animal):
    def run(self):
        print("cat running")

Animal().run()
Dog().run()
Cat().run()

print("----")

def run_base(animal):
    animal.run()

dog = Dog()
cat = Cat()

run_base(dog)
run_base(cat)

print(type(dog))

print(dir(dog))

print(hasattr(dog, "x"))
print(getattr(dog, "x"))
print(dog.x)

class Student:
    __slots__ = ('name', 'score')

mjp = Student()
mjp.name = 'mjp'
mjp.score = 100
# mjp.aa = 123

class Person():
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        if not isinstance(value, int):
            raise ValueError("must be int")
        if value != 1 and value != 2:
            raise ValueError("must between 1 and 2")
        self._sex = value

    @property
    def age(self):
        return 23

p1 = Person()
p1.sex = 1
print(p1.sex)
print(p1)
print(p1.age)
# p1.age = 2 # AttributeError: can't set attribute

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("must be int")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("must be int")
        self._height = value

    @property
    def resolution(self):
        return str(self._width) + " * " + str(self._height)

s = Screen()
s.width = 1000
s.height = 800
print(s.resolution)
print(s.__dict__)