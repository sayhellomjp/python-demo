import base64

str = '任婷婷'
str_bytes = bytes(str, encoding='utf-8')
str_bytes1 = b'aa'
str_bytes2 = str.encode('utf-8')
str1 = b'\xe4\xbb\xbb\xe5\xa9\xb7\xe5\xa9\xb7'.decode('utf-8')

print(str)
print(str_bytes)
print(str_bytes1)
print(str_bytes2)
print(str1)