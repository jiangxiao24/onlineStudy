#__author__:jiangqijun
#__date__:2018/11/5
from functools import  reduce


# def action1(n):
#     print('start write log')
#     with open('test',mode='a', encoding='utf-8') as f:
#         f.write("this is an log")
#     print('log end %s'%n)
#
#
# action1(10)

#4、不定长函数
# 传入的是元祖
# def add(*args):
#     print(args)
#     sum = 0
#     for i in args:
#         sum =+ i
#     print(sum)
# add(1)

# 传入的是字典
# def print_info(**kwargs):
#     for key in kwargs:
#         print("{key} is {value}".format(key=key, value=kwargs.get(key)))
#
# print_info(name='jiangqijun', age='18')

#这里先给的是默认值，再者是分给args再者给kwargs
# def f(sex='female', *args, **kwargs):
#     print(sex)
#     print(args)
#     print(kwargs)
#
# f(1, 2,7,'hello',name='jiangqijun')

#return的功能
#1、如果没有添加return则默认返回一个none 2、结束函数 3、返回某个对象
# def f():
#     print('hello')
#     return
# #4、如果返回的是多个对象则将多个对象封装为元祖返回
# def f2():
#     return 'a',4,[1,7]
#
# print(f2())

#作用域
# 1、L local ,局部作用域，函数中定义的变量
# 2、E enclosing 嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的
# 3、G global，全局变量，就是模块级别定义的变量
# 4、B built_in，系统固定模块里边的变量，比如int bytearray
#搜索顺序是:local>enclosing>global>built-in

# b_var = int(8.9) #这里的int函数是built-in变量
# g_var = 6        #这里是全局变量
#
# def outer():
#     e_var = 5     #嵌套变量
#     def inner():
#         l_var = 2  #本地变量


# #a.此处前边已经使用过count，所以后边不能对全局变量进行修改，报错。这里报错的原因是调用test的时候代码全部
# #加载到内存，print(count)找到下面的局部变量count,所以报错count使用应该在声明之后
# count = 2
# def test():
#     print(count)
#     count=1
# test()
#b.此处函数里的count是一个新的count
# count = 2
# def test():
#     count=1
#     print(count)
# test()

#c.通过一个关键字global声明进行修改
# count = 2
# def test():
#     global count
#     print(count)
#     count=1
#     print(count)
#
# test()

#d.通过关键字nolocal修改嵌套变量
# def outer():
#     e_var = 5     #嵌套变量
#     def inner():
#         nonlocal e_var
#         print(e_var)
#         l_var = 2  #本地变量
#         e_var=3
#         print(e_var)
#     inner()
# outer()

# def f1(*args):
#     print(args)
#
# l = [1, 2, 3]
# f1(l)#这种得到的结果是([1, 2, 3],)
# f1(*l)#这种得到的结果是(1, 2, 3)

#

# 高阶函数
#1、函数名称就是一个变量，里边的指向代码块，函数名可以赋值给其他变量
#2、函数名可以作为函数参数
#3、函数名作为函数的返回值eg.foo3()，如果return inner()则会调用，如果是return inner则只返回一个变量
# def func(n):
#     return n*n
#
#
# def foo(a, b, f):
#     print(func(a)+f(b))
#
# foo(1, 2, func)

# def foo3():
#     def inner():
#         return 3
#     return inner
#
# print(foo3())  #返回的是inner的对象地址

#递归的特点
#1、一定要调用自身的函数
#2、有一个结束条件
#3、但凡是递归能够实现的用循环一定能实现
#4、递归在有些时候调用效率很低
# def count(n):
#     if n < 1:
#         return -1
#     elif n == 1:
#         return 1
#     return n*count(n-1)

#1、eval传入的参数locals()则只能用函数内部的，传入的参数globals()则使用全局变量，这里表示等与x+y
# x = '1'
# y = '2'
# def test():
#     x = 2
#     y = 3
#     num1 = eval('x+y')
#     print(num1)
#     num2 = eval('x+y', globals())
#     print(num2)
# test()

#2、filter()用作过滤，传入的是函数和迭代器,里边加的函数必须包含判断条件,使用filter得到的是一个迭代器对象。需要其他函数进行强制转换
# def test(s):
#     if s!='a':
#         return s
#
# s = 'abcd'
# result = filter(test, s)
# print(list(result))

#3、map()方法,传入的是函数和迭代器，返回的是一个迭代器，需要其他函数进行强制转换
# def test(n):
#     return n*n
# result = map(test, [1,2,3])
# print(list(result))

#4、reduce() 传入函数和一个迭代器，这里表示先传入1，2得到结果3再传入3，3，以此类推，返回得是一个结果
# def test(x, y):
#     res = x + y
#     return res
#
# l = [1, 2, 3, 4, 5, 6, 7]
# print(reduce(test, l))

#5、lambda 命名规则是，在左边传入函数的参数，冒号右边传入函数的返回值，创建时没有名字所以叫做匿名函数
# add = lambda x,y:x+y
# print(add(1,2))