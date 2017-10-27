import functools
import sys
from PIL import Image
print(int("0x12f", base=16))

int2 = functools.partial(int, base=2)

print(int2("1011"))

print(int2("30", base=10))

print(max(2, 4, 1))

print(functools.partial(max, 10)(2, 5, 1))

print(sys.path)

im = Image.open("D://123.jpg")
print(im.format, im.size, im.mode)