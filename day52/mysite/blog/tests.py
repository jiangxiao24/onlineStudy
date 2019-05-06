from django.test import TestCase

 # Create your tests here.
#
#
# a = '2'
# b=True
# l = [1,4,5]
# s = {'a':6, 'b':7}
# s1 = {'2','3'}
#
#
#
# def f(b):
#     b=False
#     print(b)
#
# f(b)
# print(b)
#
# l = [7,9,2,3]
# # for i in range(len(l)-1):
# #     for j in range(len(l)-i-1):
# #         print(j)
# #         if l[j]>l[j+1]:
# #             l[j+1],l[j] = l[j],l[j+1]
# # print(list(range(100)))
#
# for i in range(len(l)-1):
#     min = i
#     for j in range(i, len(l)):
#         if l[j]<l[min]:
#             min=j
#     l[i],l[min]=l[min],l[i]
#
# # print(l)
# #
# # li=[9,7,5,2]
# # for i in range(1,len(li)):  #i 代表每次摸到的牌的下标
# #         tmp=li[i]
# #         j = i-1  # j代表手里最后一张牌的下标
# #         while True:
# #             if j < 0 or tmp >= li[j]:
# #                 break
# #             li[ j + 1] = li [j]
# #             j -=1
# #         li[j+1] = tmp
# # print(li)
#
#
# l = [10,30,21,13]
# # for i in range(1,len(l)):
# #     temp = l[i]
# #     j=i-1
# #     while True:
# #         if j<0 or temp>=l[j]:
# #             break
# #         l[j+1] = l[j]
# #         j-=1
# #     l[j+1] = temp
#
# print(l)
#
# l = [3,7,10, 30]
# def f(l,g):
#     low = 0
#     high = len(l)-1
#     while low<high:
#         mid = (high + low) // 2
#         if l[mid] == g:
#             return mid
#         elif l[mid]<=g:
#             low = mid+1
#         else:
#             high=mid-1
#     return None
#
# print(f(l,10))

# class Test:
#     @staticmethod
#     def f():
#         print('ok')
#
#     @classmethod
#     def f2(cls):
#         print('ok2')
#
# t = Test()
# Test.f()
# t.f()
# t.f2()
# Test.f2()

import os

# with open(os.path.abspath(__file__), 'rb') as f:
#     l = [i for i in f if i== "from django.test import TestCase\r\n" ]
# print(l)
# l1 = 'hello'
# print(l1 == 'hello')
# l2 = 2
# print(l2 == 2)
# l3 = [1,2]
# print(l3 ==[1,2])
# s1 = 'helloworld'
# print(s1.find('wo'))
# print('wso' in s1)

def outer():
    e_var = 5     #嵌套变量
    def inner():
        #nonlocal e_var
        print(e_var)
        l_var = 2  #本地变量
        # e_var=3
        # print(e_var)
    inner()

outer()
