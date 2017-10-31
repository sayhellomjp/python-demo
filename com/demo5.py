from contextlib import contextmanager, closing

# class Query():
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('begin')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             print('error')
#         else:
#             print('end')
#
#     def query(self):
#         print('query info... name: %s' % self.name)
#
# with Query('mjp') as f:
#     f.query()

class Query2():
    def __init__(self, name):
        self.name = name

    def query(self):
        print('query info... name: %s' % self.name)

@contextmanager
def create_query(name):
    print('begin')
    q = Query2(name)
    yield q
    print('end')

with create_query('rtt') as f:
    f.query()

@contextmanager
def tag(name):
    print('begin tag')
    yield
    print('close tag')

with tag('test'):
    print('hello world')

class Close_test():
    def __init__(self, name):
        self.name = name

    def close(self):
        print('%s is closing...' % self.name)

    def query(self):
        print('query one result: %s' % self.name)

with closing(Close_test('hahaha')) as f:
    f.query()
