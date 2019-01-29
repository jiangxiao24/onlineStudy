#__author__:jiangqijun
#__date__:2018/10/20

import json
import chardet
import sys


parent_layers = []
current_layer= []

with open('address_file', 'r+',encoding='unicode-escape') as f:
    json.loads(f.readline())
    # str1.encode('utf8').decode()
    # str1 = f.readline()
    # str1.encode('unicode-escape')
    # json.loads(str1.encode('unicode-escape'))
    # str2 = str1.encode('utf8').decode('GBK')

    #json.loads(str1)
   # d = json.loads(f.readlines())
   #print(json.loads(u(f.readline())))
   #print((''.join(f.readlines())))
   #current_layer = json.loads(''.join(f.readlines()), encoding='utf8')
   # print(type(current_layer))
# print(current_layer)
    # while(True):
    #     pass
