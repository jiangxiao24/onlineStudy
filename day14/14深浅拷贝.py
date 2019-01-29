#__author__:jiangqijun
#__date__:2018/11/4


# a = [[1, 2], 3, 4]
# b = a
# c = a.copy()
# # 修改了c中的列表则a,b,c均发生改变
# # 修改c中的整型，只有c发生改变，a,b不改变
# c[0][0] = 6
# print(id(a[0]))
# print(id(b[0]))
# print(id(c[0]))
#
# c[1] = 7
# print(id(a[1]))
# print(id(b[1]))
# print(id(c[1]))
#
# # 修改b中的列表则a，b，c均发生改变
# # 修改b中的整型则a改变，c不改变
#
# # b[0][0] = 6
# # print(id(a[0]))
# # print(id(b[0]))
# # print(id(c[0]))
# #
# # b[1] = 7
# # print(id(a[1]), a[1])
# # print(id(b[1]), b[1])
# # print(id(c[1]), c[1])
#
# # 修改了a中的列表,a,b,c均发生改变
# # 修改了a中的整型，a,b发生改变，c不发生改变
# # a[0][0] = 6
# # print(id(a[0]))
# # print(id(b[0]))
# # print(id(c[0]))
# #
# # print(id(a[1]), a[1])
# # print(id(b[1]), b[1])
# # print(id(c[1]), c[1])
#
# # 修改了e中的值对f不发生改变
# e = 1
# f = e
# e = 3
# print(id(e))
# print(id(f))
#
# # g=[1]
# # h=g
# # g[0] = 2
# # print(g, h)

# set
# 1、集合的创建
s = set('jiangqijun') #{'u', 'g', 'q', 'a', 'n', 'j', 'i'}
l = ['1', '2', '3']
s2 = set(l)

# # 2、集合转换为列表
# print(list(s2))
#
# # 3、集合的元素必须是可hash的（元素是不可变类型）
# s3 = set([[1,2], 3, 4]) #TypeError: unhashable type: 'list'
#
# # 4、可变集合与不可变集合,可变集合不能作为字典的键，原因是本身是不可hash的
# d = {s3:'2'} #报错 TypeError: unhashable type: 'list'

# 5、set是无序的只能通过for循环来访问或者iterator访问，in /not in
print(1 in s2)
print('1' in s2)

# 6、set添加add() update() remove()
# s2.add(0)  #作为单个元素添加
# print(s2)
# s2.update('wp') #更新添加进入保留原来的增加新内容,作为一个序列来添加
# s2.update(['jiang', 12]) #把每个元素添加到集合里边去
# print(s2)
s2.remove('1') # 将1这个元素移除
print(s2)
s2.pop() # 随机移除一个元素
print(s2)
s2.clear() #将集合清空
print(s2)


#7、关系测试 交集 并集 差集

a = set([1, 6, 8, 10, 12])
b = set([0, 6, 8, 11])

#intersection取交集 等于&
print(a.intersection(b))   #{8, 6}
print(a&b)

#union 取并集 等于|
print(a.union(b))  #{0, 1, 6, 8, 10, 11, 12}
print(a|b)

#取差集a中有b中没有 等于-
print(a.difference(b))  #{1, 10, 12}
print(a-b)

#反向差集 除了交集之外的所有数字集合 等于^
print(a.symmetric_difference(b)) #{0, 1, 10, 11, 12} 并集中去除交集后的补集
print(a^b)
