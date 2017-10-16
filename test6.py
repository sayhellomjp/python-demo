L = [1, 2, 3, 4, 5]
print(L[:3])
print(L[1: 3])
print(L[-2: -1])

t = range(5)
t = range(0, 5, 2)
for n in t:
    print(n)

tt = list(range(6))
tt[2] = 'test'
for n in tt:
    print(n)

print("-----")
tt = tuple(range(8))
for n in tt:
    print(n)
