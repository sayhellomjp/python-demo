import os

L = [1, 2, 3]
print(L)

L2 = list(range(2, 10))
print(L2)

L3 = [x * x for x in range(1, 5)]
print(L3)

L4 = [x * x for x in range(1, 5) if x % 2 == 0]
print(L4)

L5 = [A + B for A in "ABC" for B in "XYZ"]
print(L5)

L6 = [d for d in os.listdir(".")]
print(L6)