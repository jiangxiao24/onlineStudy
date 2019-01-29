#__author__:jiangqijun
#__date__:2019/1/13


from wsgiref.simple_server import make_server


def f1(req):
    print(req['PATH_INFO'])
    return [b'<h1>hello, book!</h1>']

def f2(req):
    print(req['PATH_INFO'])
    return [b'<h1>hello, web!</h1>']

def application(environ, start):
    path = environ['PATH_INFO']
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
