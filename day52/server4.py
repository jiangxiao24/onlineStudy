#  __author__:jiangqijun
#  __date__:2019/1/15

from wsgiref.simple_server import make_server
import django

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

def resource():
    url=[
        ('/book', f1),
        ('/web', f2),
    ]
    return url

def application(environ, start):
    path = environ['PATH_INFO']
    start('200 OK', [('Content-Type','text/html')]) #
    items = resource()
    for item in items:
        path == item[0]
        data_temp = item[1]
        break
    if path:
        return data_temp(environ)
    else:
        return [b'404']


httpd = make_server('', 8999, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()