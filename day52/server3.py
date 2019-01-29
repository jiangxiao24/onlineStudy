#__author__:jiangqijun
#__date__:2019/1/15

from wsgiref.simple_server import make_server


def f1(req):
    print(req['PATH_INFO'])
    with open('book.html', 'rb') as f:
        data = f.read()
    return [data]

def f2(req):
    print(req['PATH_INFO'])
    with open('web.html', 'rb') as f:
        data = f.read()
    return [data]


def application(environ, start):
    path = environ['PATH_INFO']
    print(environ)
    start('200 OK', [('Content-Type','text/html')]) #
    if path == '/book':
        return f1(environ)
    elif path == '/web':
        return  f2(environ)
    else:
        return [b'404']


httpd = make_server('', 8999, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()