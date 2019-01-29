#__author__:jiangqijun
#__date__:2018/12/17
# from module1 import  add #调用模块下的某个方法
#
# print(add(2,1))

# from web.web1.module2 import * 调用模块下的所有的方法变量,不建议使用，可能覆盖当前相同名称的方法

#在每个包下面的__init__文件在引入的时候就会执行一遍

#相同目录下需要加完整路径才能执行

import  os
basedirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))
print(basedirname)
