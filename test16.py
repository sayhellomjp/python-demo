
class Student:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return "Student Object (name: %s)" % self.__name

s = Student("majunpeng")
print(s)