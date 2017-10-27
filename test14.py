
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_grade(self):
        if self.__age > 0 and self.__age < 18:
            return "未成年"
        elif self.__age > 18 and self.__age < 30:
            return "中年人"
        else:
            return "老年人"

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def test(self):
        print("test")

mjp = Student("majunpeng", 26)
rtt = Student("rentingting", 17)

print(mjp.get_name())

print("姓名：%s, 年龄：%d，阶段：%s" % (mjp.get_name(), mjp.get_age(), mjp.get_grade()))
print("姓名：%s, 年龄：%d，阶段：%s" % (rtt.get_name(), rtt.get_age(), rtt.get_grade()))

rtt.test()