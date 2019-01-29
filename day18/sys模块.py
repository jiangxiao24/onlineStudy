#__author__:jiangqijun
#__date__:2018/11/27
import sys

#sys模块主要用作与python解释器进行打交道

print(sys.argv) #获取调用该py文件运行的时候传入的参数，返回的参数以列表显示第一个元素是py文件本身的名称，接着显示其他两个参数
print(sys.path)#返回模块的搜索路径,首先在当前路径下查找再去导入的库文件下去查找，如果要添加其他路径则使用sys.path.append()
print(sys.platform)#返回操作系统的平台
