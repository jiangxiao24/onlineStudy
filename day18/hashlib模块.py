#__author__:jiangqijun
#__date__:2018/11/27

import hashlib

#md5加密方式
m1 = hashlib.md5()
m1.update('hello'.encode('utf-8')) #字符串再python3中是unicode字符要转换成字节类型
print(m1.hexdigest())#进行加密
m1.update('world'.encode('utf-8'))#这里相当于将helloworld当作整体进行加密
print(m1.hexdigest())

#SHA加密方式
#加密之后不可逆转，撞库是因为用了很多猜测的字符加密后来匹配
m3 = hashlib.sha256
#m3.update('hello'.encode('utf-8'))
print(hashlib.sha256('hello'.encode('utf-8')).hexdigest())
