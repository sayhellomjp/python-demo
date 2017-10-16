from collections import Iterable

list = ['cd', 'sh', 'emei', 'ls', 'nc']
j = {"city": "emei", "province": "sichuan", "count": 120000, "position": "south west"}

for n in list:
    print(n)

print("----")

for key in j:
    print(key)
    print(j[key])

print("----")

for v in j.values():
    print(v)

print("----")

for k, v in j.items():
    print(k + ":", v)

print("----")

print(isinstance(list, Iterable))
print(isinstance(j, Iterable))

print("----")

for i, v in enumerate(list):
    print("i:", i, "v:", v)
