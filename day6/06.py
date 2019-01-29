#__author__:jiangqijun
#__date__:2018/8/28

#列表创建方式
# a = list([1, 2, 3])
# b = list((1, 2, 3))
# print(a)
# print(b)

#字典创建方式
# c = dict((('name','jiangqijun'),))
# d = dict((("name","jiangqijun"),))
# print(c)
# print(d)

# d = {"age":18}
# #如果某个键存在则返回原来的值,且不修改原来的值
# print(d.setdefault("age",30))
# print(d)
#
# #如果某个键不存在则返回新增加的值
# print(d.setdefault("name",'jiangqijun'))
# print(d)
#
# #获取所有的键值
# print(d.keys())
#
# #获取所有的值
# print(d.values())
#
# #获取所有的键值对
# print(d.items())

# #修改操作
# e = {"name":"jiangqijun", "age":"18"}
# f = {"name":"xiaojiang", "city":"shenzhen"}
# e.update(f)
# print(e)

# #删除操作del,clear,pop
# g = {"name":"xiaojiang", "city":"shenzhen","phone":"18812344321"}
# del(g["name"])#删除键值对
# print(g)
# print(g.pop("city"))#删除键值对并返回值
# print(g)
# g.clear()#清空整个字典
# print(g)
#字符串
a = "hello"
b = "world!"
#采用下标访问获取字符
print(a[0])
#采用切片方式获取字符串
print(a[1:])
#字符串的连接方法
print("---".join([a,b]))
#重复输出*
print(a*10)
#ing关键字
print("h"in a)
#格式化%s
print("%s is very good"%"it")

print('\tMy tLtle\n'.strip())

#字符串的常用方法
str = "hello,world"
#一个字符出现的次数
print(str.count("o"))
#居中显示
print(str.center(50,"#"))
#判断是否以某个字符开始
print(str.startswith("he"))
#查找某个字符第一次出现的索引位置
print(str.find('e'))
#格式化输出
print("hello {name} ".format(name="jiangqijun"))
#大小写
print(str.upper())
print(str.lower())
#strip从左边以字符切割
print(str.strip('h'))
#替换字符
print(str.replace("ello","i"))
#分割字符为列表
print(str.split(","))