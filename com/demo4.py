import itertools

# t = itertools.count(1)
# for x in t:
#     print(x)

# t1 = itertools.cycle('ABC')
# for x in t1:
#     print(x)

# t2 = itertools.repeat('acb', 3)
# for x in t2:
#     print(x)

t = itertools.count(1)
ns = itertools.takewhile(lambda x: x<=10, t)
print(list(ns))

for x in itertools.chain('abc', '123'):
    print(x)

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

print('----')

for key, group in itertools.groupby('AaaBBbcCAAa', lambda x: x.upper()):
    print(key, list(group))