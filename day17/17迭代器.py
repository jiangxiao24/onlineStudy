#__author__:jiangqijun
#__date__:2018/11/18

#1、元祖、列表、字典、字符串、集合都是可迭代对象，存在__iter__方法得就是可迭代对象
#2、生成器一定是迭代器，迭代器不一定是生成器
#3、迭代器得两个等价条件a.一定有iter()方法b.有next()方法
#4、一个for循环就是做了a.将可迭代对象进行迭代话生成一个迭代器iterator b.通过next()方法进行取值c.try catch结束值

t1 = (1,3,5)
l1 = [2,4,6]
d1 = {'a':'aa','b':'bb','c':'cc'}
print(iter(t1)) #得到一个迭代器 <tuple_iterator object at 0x000001998AE3EA58>
s = iter(t1)
print(next(s))
print(next(s))

