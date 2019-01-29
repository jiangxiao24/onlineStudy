#__author__:jiangqijun
#__date__:2018/11/25
import os

#字符串前边加r表示一个原生字符串，不表示任意转义
#print(os.getcwd())#获取当前运行python所在的目录路径
#os.chdir('D:\pyScripts\onlineStudy\day17')#改变当前路径相当于cmd中的cd
#print(os.getcwd())
#print(os.curdir)#返回当前目录'.'
#print(os.pardir)#返回父目录'..'
#print(os.makedirs('dir1/dir2'))#生成递归文件
#os.mkdir('dir3')#生成单级目录
#os.rmdir('dir1/dir2')#删除单机空目录，若目录下不位空则无法删除
#print(os.listdir('.'))#列出制定目录下的文件,包含隐藏文件
#os.remove('rename1')#只能删除文件不能删除文件夹
#os.rename('rename','rename1')
#print(os.stat('os模块.py')) #st_atime=1543243644(最后一次打开的时间), st_mtime=1543243643(创建的时间), st_ctime=1543158976()
#print(os.sep)
#在window使用'\r\n'换行的 在linux使用'\n'进行换行的 在mac里边使用'\r'进行换行的，我们使用'\n'进行换行是因为python内部做了处理
#print(os.linesep) #获取当前系统中的换行方式
#print(os.pathsep)#获取路径的分隔符在windows里边是分号在linux里边是冒号
#os.system('dir')#执行shell命令
#print(os.environ)#获取系统环境变量
#print(os.path.abspath('abc'))
#print(os.path.dirname('D:\pyScripts\onlineStudy\day18\os模块.py'))#获取当前文件所在的文件夹名字
#print(os.path.abspath(__file__))
#print(os.path.join(['path',['path',['path']]]))#文件路径进行拼接