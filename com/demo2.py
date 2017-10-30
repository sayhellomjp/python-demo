import struct

a = 100
b = 200

str = struct.pack('ii', a, b)
a1, b1 = struct.unpack('ii', str)

print(str)
print(a1)
print(b1)