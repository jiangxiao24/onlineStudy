#__author__:jiangqijun
#__date__:2018/10/12

import sys,time
import json

# f = open('test1', 'w')
# f.write("hello")

# f = open('test2.txt', 'w',encoding='utf-8')
# print(f.readline())
# print(f.readline())
# print(f.read(5))
# print(f.read(5))

# content = f.readlines()
# print(content)
#
# for i in range(len(content)):
#     if i == 5:
#         print(content[i].strip('\n')+'like it')
#     else:
#         print(content[i].strip('\n'))
#
# for i in range(len(content)):
#     str = content[i].strip('\n')
#     if i == 5:
#         str = ''.join([str,'likeit'])  #取代+
#     print(str)
#
#
# for i in range(1,10):
#     print(i)

# str = "sha dsfs dkfjadskfkdsf hdfksdf"
# print(str.split(" "))
# for i in f:
#     print(i.strip())
#
# print(f.tell()) #光标所在的位置
# print(f.read(4))#一个英文占用一个字符，中文则认为一个字符是三个字符
# print(f.tell())
#
#
# f.seek(offset=1)
# print(f.read(2))
# f.write("hello world")
# f.truncate(3)
# f.write("222")
# f.close()

# for i in range(30):
#     sys.stdout.write('*')
#     sys.stdout.flush() #将缓存的数据写到磁盘
#     time.sleep(2)
#
# for i in range(30):
#     print('*',end='', flush=True)

# f = open('test2.txt','r+', encoding='utf-8')#可以先读取到上边的内容再进行写入,写入的时候在最后边写，并不会覆盖原本存在的内容
# print(f.readline())
# f.write('333')
# print(f.readline())
# f.close()

# f = open('test2.txt','w+',encoding='utf-8')#写光标一直在最后一个位置，所以每次写的时候都会清空，写完后光标还在最后一个位置需要调整光标位置才能读取到内容
# print(f.readline())
# f.write("hello")
# print(f.readline())
# f.seek(0)
# print(f.readline())

# f = open('test2.txt','a+',encoding='utf-8')#写光标一直在最后一个位置，每次写的时候不会清空，写完后光标还在最后一个位置需要调整光标
# f.write('666')
# print(f.readline())
# f.seek(0)
# print(f.readline())

# f1 = open('test1','r',encoding='utf-8')
# f2 = open('test2.txt','a',encoding='utf-8')
# number = 0
# for line in f1:
#     number = number+1
#     if number==6:
#         line = ''.join([line.strip(),'666\n'])
#         print(line)
#     f2.write(line)
# f1.close()
# f2.close()
# with open('test1','r', encoding='utf-8') as f:
#     f.readline()
#     print(f.readline())
#
# with open('test1', 'r', encoding='utf-8') as f1 ,open('test2.txt', 'w', encoding='utf-8') as f2:
#     pass

#python中的字典转换为json
#d = {"1":"test1","2":"test2"}
d = '232'
with open("json_txt","w+", encoding='utf-8') as f:
    f.write(json.dumps(d))
    f.write('\n'+json.dumps(d))
    f.seek(0)
    print(f.readline())

#json中的对象转换为python中的字

with open("json_txt", "r+", encoding='utf-8') as f:
     print(f.readline())
     d2 = json.loads(f.readline())
     #print(d2["1"])




