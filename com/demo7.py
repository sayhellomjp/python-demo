from urllib import request, parse

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read();
#     print('Status:', f.status, f.reason)
#     print('Data:', data.decode('utf-8'))
#     for k, v in f.getheaders():
#         print('%s : %s' % (k, v))
#
# print('---')
#
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s : %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

str = parse.urlencode([('username', 'mjp'), ('password', '123'), ('realname', '马俊鹏')])
print(type(str))
print(str)
print(str.encode('utf-8'))
print(str.encode())