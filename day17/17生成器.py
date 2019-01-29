#__author__:jiangqijun
#__date__:2018/11/17

#1、列表生成式，可以在前边加入表达式或者函数
# a = [x*2 for x in range(10)]
# print(a)
#
# def f(n):
#     return n*n*n
# b = [f(x) for x in range(10)]
# print(b)

#2、a.生成器,每次使用得时候才会计算，每次只能取下一个而不能跳跃取值.生成器就是一个可以迭代得对象
#下边得i取值得是接着上边一起取得，由于上边已经取完了所以下边就没有了
#在循环中,i这个变量每次只引用一个值，所以只有一个值是占用内存，前面得引用都消失
#在循环中，最后一个变量时，会自己捕获到异常，从而自动停止
# a = (x*2 for x in range(3))
# print(type(a)) #<class 'generator'>
# print(next(a))
# print(next(a))
# print(next(a))
# #print(next(a)) #StopIteration
# for i in a:
#     print(i)

#b.迭代器得两种生成方式
# a = (x*2 for x in range(10))
#yield关键字，在这个关键字相当于return方法，不同之处是，调用next()时，在执行到这里得时候会保存函数得状态
#下次继续从该状态执行下去
# def foo():
#     print('NO1')
#     yield 1
#     print('NO2')
#     yield 2
#
# s = foo()
# print(s) #这里得s就是一个生成器,直接执行得时候是不会打印出来得，调用next(s)方法得时候才会执行
# next(s) #执行生成器，返回第一个生成器得值
# next(s)
# print(next(s))



# def f(max):
#     n, before, after = 0, 0, 1
#     while(n<max):
#         print(before)
#         before, after = after, before+after #这里先计算after before+after，再进行赋值
#         n = n+1
# f(3)
#迭代器实现斐波拉序列

# def f(max):
#     n, before, after = 0, 0, 1
#     while(n<max):
#         yield after
#         before, after =  after,before+after
#         n = n+1
#
# for i in f(5):
#     print(i)

#c.生成器得send方法,s.send('abc')方法等于next(s),调用s.send得时候，首先要进入才能将值传入。如果是send进入得话
#则首次需要使用s.send(None)，否则报错。或者通过next(s)来调用。后边得值才会传入
# def f():
#     print('ok1')
#     count1 = yield 1
#     print('ok2')
#     count2 = yield 2
#
# s = f()
# #c1 = s.send(None)
# c1 = next(s)
# print(c1)
# c2 = s.send('aaa') #这里得aaa赋值给了count1
# print(c2)

# def get_file_length(filepath):
#         with open(filepath, 'r', encoding='utf-8') as f:
#             while True:
#                 str = f.readline()
#                 if str:
#                     str_length = len(str)
#                     yield  str_length
#                 else:
#                     return
#
#
# max = 0
# index = 0
# index_temp = 0
#
# for i in get_file_length("2018-11-23-info.txt"):
#     index_temp = index_temp+1
#     if i>max:
#         max = i
#         index = index_temp
# print(next(get_file_length("2018-11-23-info.txt")))
#
# print(next(get_file_length("2018-11-23-info.txt")))
# with open("2018-11-23-info.txt", 'r', encoding='utf-8') as f:
#     print(f)
#
# [max(len(x)) for x in open("2018-11-23-info.txt", 'r', encoding='utf-8')]
#
#
# [x*x for x in range(10)]

# print(type(open("2018-11-23-info.txt", 'r', encoding='utf-8')))

def add(s, x):
    return s + x


def gen():
    for i in range(4):
        yield i


base = gen()
for n in [1, 10]:
    base = (add(i, n) for i in base)

print(base)
for i in base:
    print(i)
#print(list(base))