from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    return [b'<h1>hello world</h1>']

httpd = make_server('', 9595, application)
print('Serving HTTP on port 9595...')
httpd.serve_forever()