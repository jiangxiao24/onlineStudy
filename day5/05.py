#!-*- coding:utf-8 -*-
#__author__:jiangqijun
#__date__:2018/8/26
#!-*- coding:utf-8 -*-
# name = input("name:")
# age = input("age:")
# job  = input("job：")
# salary = input("salary:")
#
# if salary.isdigit():
#     salary = int(salary)
# else:
#     print("must be digit！")
#     exit("程序退出！")
#
# print(name, age, job, salary)
# msg = '''
# =====info of %s=====
# name:%s
# age:%s
# job:%s
# salary:%d
# =====end=====
# '''%(name, name, age, job, salary)
# print(msg)

# list1 = [6, 5, 7, 9, 10]
# # print(list[1:-1:2])
# # print(list[3:-1:1])#到最后一位位置不包含最后一位
# # print(list[1::-2])
# # print(list[1:3:-2])
# # print(list[-2::-1])
# # print(list[1:4])#到第四位为止不包含第四位
# # #添加就是apend insert
# # list.append("32")
# # list.insert(0,12)
# # print(list)
# # list[1:5:1]=[2,2,3]
# # print(list)
# #删除就是remove pop del
# list1.remove(6)#删除对应的值
# print(list1)
# a=list1.pop(2)#删除对应索引处的值并且返回
# print(a)
# print(list1)
# del(list1[0])#按照对应值删除
# print(list1)
# # del list1#删除列表，从内存中删除
# # print(list1)
# #修改
# list1[0]="99"
# print(list1)

#列表的count extend,index,reverse,sort
a = [1, 4, 3, 6, 9, 3]
print(a.count(3))#3这个值出现的次数
b = ["1","2"]
a.extend(b) #a扩增了b的内容
print(a)
print(b)
print(a.index("1"))#"1"这个元素出现的位置,存在重复的位置则给出第一个出现的位置
a.reverse()#没有返回值就直接反向
print(a)
#a.sort()#排序里边必须是数值
c = [10, 2, 2.1, 1,]
c.sort(reverse=True)
print(c)