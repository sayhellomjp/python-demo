import hashlib

# str = '123456'
#
# md5 = hashlib.md5()
# md5.update(str.encode('utf-8'))
# print(md5.hexdigest())
#
# md5_1 = hashlib.md5()
# md5_1.update('123'.encode('utf-8'))
# md5_1.update('456'.encode('utf-8'))
# print(md5_1.hexdigest())

db = {}
tt = '123'

def get_md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()

def register(username, pwd):
    db[username] = get_md5(username + pwd + '-salt')

def login(username, pwd):
    if db[username] and db[username] == get_md5(username + pwd + '-salt'):
        print('登录成功')
    else:
        print('登录失败，帐号或者密码错误')

register('rtt', '111111')
register('mjp', '123456')

login('rtt', '566')
login('rtt', '111111')
