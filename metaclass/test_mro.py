
class Base():
    def __init__(self):
        print("enter base")
        print("leave base")

class A(Base):
    def __init__(self):
        print('enter A')
        super(A, self).__init__()
        print('leave A')

class B(Base):
    def __init__(self):
        print('enter B')
        super(B, self).__init__()
        print('leave B')

class C(A, B):
    def __init__(self):
        print('enter C')
        super(C, self).__init__()
        print('leave C')

c = C();
print(C.mro())
A()
print(A.mro())