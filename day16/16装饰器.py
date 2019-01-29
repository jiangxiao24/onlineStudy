#__author__:jiangqijun
#__date__:2018/11/12

import time
import json

#闭包：如果在内部函数中引用了外部函数得变量，则内部函数就是一个闭包。
# 条件1：内部函数2.引用了外部变量
# def outer():
#     x = 2
#
#     def inner():  #内部函数
#         print(x)  #对外部函数得变量进行了引用
#     return inner #结论：inner函数是一个闭包
#
# f = outer()
# f()

#这种情况得时候改变了调用方式，原本调用foo得现在变成了调用show_time
# def show_time(f):
#     start = time.time()
#     f()
#     end = time.time()
#     print(end - start)
#
# def foo():
#     time.sleep(3)
#     print('this is foo1')

#show_time(foo)

# 装饰器
# #通过原本得foo方式调用，结合闭包
# def show_time(f):
#     def inner():
#         start = time.time()
#         f()
#         end = time.time()
#         print(end - start)
#     return inner
#
# @show_time  #等价于foo = show_time(foo)得方式
# def foo():
#     time.sleep(3)
#     print('this is foo1')
#
# # foo = show_time(foo)
# foo()  #这样就直接调用foo实现了功能

#实现在装饰器里边添加参数
# def show_time(f):
#     def inner(*a, **b):
#         start = time.time()
#         res = f(*a, **b)
#         print(res)
#         end = time.time()
#         print(end - start)
#     return inner
#
# @show_time
# def foo(*a, **b):
#     sum = 0
#     for i in a:
#         sum+=i
#     return  sum
# l = [1,2,3,4,5,6,7,8]
# foo = show_time(foo,True)
# foo(*l)


#实现在装饰器函数加参数
# def logger(flag):
#     print('1')
#     def show_time(f):
#         print('2')
#         def inner(*a, **b):
#             print('3')
#             start = time.time()
#             res = f(*a, **b)
#             print(res)
#             end = time.time()
#             print(end - start)
#             if flag == 'true':
#                 print("我是rizhi")
#         print('4')
#         return inner
#     print('5')
#     return  show_time
#
# @logger('true')
# def foo(*a, **b):
#     sum = 0
#     for i in a:
#         sum+=i
#     return  sum
# l = [1,2,3,4,5,6,7,8]
# #foo = show_time(foo,True)
# foo(*l)

with open('account_jingdong.txt','w', encoding='utf-8') as f:
    f.writelines('jingdong\n123')

with open('account_weixin.txt','w', encoding='utf-8') as f:
    f.writelines('weixin\n456')

page = {'1': 'home', '2': 'finance', '3': 'book'}

login_status = False

def login(*auth_type):
    def navigate(function):
        def actul_action():
            print(auth_type)
            global login_status
            if login_status == False:
                username = input("please input username:")
                password = input('please input password:')
                if auth_type[0]=='jingdong':
                    with open('account_jingdong.txt','r', encoding='utf-8') as f:
                        name1 = f.readline().strip('\n')
                        pwd1 = f.readline().strip('\n')
                        print(name1,pwd1)
                    if name1 == username and pwd1 == password:
                        login_status = True
                else:
                    with open('account_weixin.txt','r', encoding='utf-8') as f:
                        name2 = f.readline().strip('\n')
                        pwd2 = f.readline().strip('\n')
                    if name2 == username and pwd2 == password:
                        login_status = True
            print(login_status)
            function(login_status)
        return actul_action
    return  navigate

@login('jingdong')
def home(login_status):
    if login_status:
        print("welcome to home page!")

@login('weixin')
def finance(login_status):
    if login_status:
        print("welcome to finance page!")

@login()
def book(login_status):
    if login_status:
        print("welcome to book page!")



# home()
# print(login_status)
# finance(False)

while True:
    for key in page:
        print('{key}.{value}\n'.format(key=key,value=page.get(key)))
    choose = input('pleas choose which page to go:')
    if choose == '1':
        home()
    elif choose == '2':
        finance()
    elif choose == '3':
        book()
    else:
        break