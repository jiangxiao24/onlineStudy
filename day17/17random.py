#__author__:jiangqijun
#__date__:2018/11/25

import random

print(random.random())#取出来得数字小于1
print(random.randint(1,10))#包含了1-10
print(random.randrange(3))#0-2
print(random.choice([[1,2,3],89,'o']))#随机取列表中任一一位
print(random.sample([1,23,4,5,6],3)) #可以取到3位数字

def gen_code():
    code = ''
    for i in range(4):
        add_num = str(random.randrange(10))
        add_ala =chr(random.randrange(65,91))
        code=code+random.choice([add_num,add_ala])
    return code

print(gen_code())