s = input("please enter your age:")
age = int(s)
if age < 6:
    print('%d岁是小学生' % age)
elif age >= 6 and age <= 18:
    print('%d岁是初中生' % age)
else:
    print('%d岁是大学生' % age)

array = [1, 5, 79, 22]
for s in array:
    print(s)

count = len(array)
n = 0
while n < count:
    print("value:", array[n])
    n = n + 1

print("end")
