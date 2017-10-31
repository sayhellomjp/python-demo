from io import StringIO, BytesIO

f = None
try:
    f = open("D:\\test123.txt", "r")
    str = f.read()
    print(str)
finally:
    if f:
        f.close()

with open("D:\\test123.txt", "r") as t:
    # str1 = t.read()
    # print(str1)

    for line in t.readlines():
        print(line.strip())

f1 = open("D:\\123.jpg", "rb")
print(f1.read())

f2 = open("D:\\tt.txt", "w")
f2.write("222222")
f2.close()

with open("D:\\tt.txt", "w") as f3:
    f3.write("0000")

f4 = StringIO("Hello,World\nI'm coming")
while True:
    temp = f4.readline()
    if temp == '':
        break
    print("result:", temp)

f5 = BytesIO()
f5.write("中文".encode("utf-8"))
print(f5.getvalue())