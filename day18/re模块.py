#__author__:jiangqijun
#__date__:2018/12/1
import  re

#一、元字符
# .(通配符)能够匹配除了\n 即换行符之外的所有字符
res1 = re.findall('w..l','hello w\nld')
print(res1) #输出结果为空

#^表示起始位置开始匹配
res2 = re.findall('^h...o', 'hdjffhellojkj')
print(res2)#无法匹配到

#$表示在结尾位置匹配
res3 = re.findall('w...d','hello world')
print(res3)

#*表示重复匹配，零个或者多个
res4 = re.findall('w.*','hello world')
print(res4)
res5 = re.findall('ab*','fjsfhjsdaklk')
print(res5)#匹配大结果是a
res6 = re.findall('a*','bcdef')
print(res6)#['', '', '', '', '', '']这里由于没有匹配到所以就全部是空

# + 表示一个或者多个
res7 = re.findall('a+b','aaaaabdfjkdajjbabkk')
print(res7) #['aaaaab', 'ab']

# ？表示零个或者一个
res8 = re.findall('a?b','aaaaabdfjkdajjbabkk')
print(res8) #['ab', 'b', 'ab']

#{x}表示匹配x次
#{m,n}表示匹配m-n次,但是如果都满足的时候就选最多的匹配(贪婪匹配)
res9 = re.findall('a{2}b','aaaaabdfjkdaabjjbabkk')
print(res9) #['aab', 'aab']
res10 = re.findall('a{1,5}b','aaaaabdfjkdaabjjbabkk')
print(res10)#['aaaaab', 'aab', 'ab']

#总结：*等价于{0,无穷次}， +等价于{1,无穷次}，?等价于{0,1},{1,}等价于{1,无穷次}

#[] 字符集 里边的逗号表示或匹配
res11 = re.findall('a[b,c]d','abd')
print(res11) #['abd']
res11 = re.findall('a[b,c]d','acd')
print(res11)#['acd']
res11 = re.findall('a[b ,c]d','abd')
print(res11)#['abd']后边的空格被过滤掉了
res11 = re.findall('a[b,c, ]d','a d')
print(res11)#['a d']这里可以匹配到空格

#[]字符集里边 \ - ^ 元字符功能取消掉

# - 在[]内表示一个范围内
res12 = re.findall('[a-z,1-9,A-Z]','dsfas3242893UJKJ')
print(res12) #['d', 's', 'f', 'a', 's', '3', '2', '4', '2', '8', '9', '3', 'U', 'J', 'K', 'J']

# ^在[]内表示取非的意思
res13 = re.findall('[^7]','uij87erk')
print(res13)#['u', 'i', 'j', '8', 'e', 'r', 'k']除了7之外的所有的字符
res14 = re.findall('[^7,8]','jkj827273kj')
print(res14)#['j', 'k', 'j', '2', '2', '3', 'k', 'j']除了7,8之外的所有的字符
res15 = re.findall('[^ab]','shsjabkjakb')
print(res15)#['s', 'h', 's', 'j', 'k', 'j', 'k']除了a,b这类字符外的所有的字符

# \
#1、能够将含有特殊意义的元字符取消特殊意义 \.取消了.的所有字符的含义
#2、能够将不含特殊意义的元字符加上特殊含义
######
# \d 匹配所有的数字 等价于[0-9]
# \D匹配所有的非数字 等价于[^0-9]
# \s匹配任何空白字符 等价于[\t\n\r\f\v]
# \S匹配任何空白字符 等价于[^\t\n\r\f\v]
# \w匹配任何字母数字 等价于[0-9a-zA-Z]
# \W匹配任何非字母数字 等价于[^0-9a-zA-Z]
# \b匹配一个特殊边界 eg：$ # , . 空格等

res16 = re.findall('\d','890-hjhksdf')
print(res16)#['8', '9', '0']
res17 = re.findall('\D','890-hjhksdf')
print(res17)#['-', 'h', 'j', 'h', 'k', 's', 'd', 'f']
res18 = re.findall('\s','890-h  jhksdf')
print(res18)#[' ', ' ']
res19 = re.findall('\S','890-h jhksdf')
print(res19)#['8', '9', '0', '-', 'h', 'j', 'h', 'k', 's', 'd', 'f']
res20 = re.findall('\w','890-hjhksdf#$')
print(res20)#['8', '9', '0', 'h', 'j', 'h', 'k', 's', 'd', 'f']
res21 = re.findall('\W','890-hjhksdf@#')
print(res21)#['-', '@', '#']
res22 = re.findall(r'h\b','890-h$jhksdf')#这里要加原生r是因为\b在python解释器里边是一个特殊字符
print(res22)#['h']

#re.search只返回一个匹配到的值
ret1 =  re.search('ab','dsfsadabflsdkabaa')
print(ret1)
print(ret1.group())

# \加上元字符取消特殊功能 比如 \.表示. \+表示+ \\表示\
ret2 = re.search('a\.','fkdsa.kl')
print(ret2.group()) #a.
ret3 = re.search('a\+b','a+b')
print(ret3.group())#a+b

# \\
ret4 = re.search('\\\\j','sdf\jfdsfs')#这里传入四个\是因为，代码传给python解释器的时候需要一个\\表示一个\，而正则里边也需要\\表示一个\，所以这个在python解释器里边是\\然后再变成正则的\
print(ret4.group())#\j
ret5 = re.search(r'\\j','dfsf\jk')
print(ret5.group())#\j

#()表示分组
ret6 = re.search('(ab)(cd)*','abjk')
print(ret6.group())#ab

#这里的(?P<id>)是固定的用法，用作起名字，这里的还是做为一个整体来匹配，只是匹配后的结果值可以用名称来取值
ret7 = re.search('(?P<id>\d{3})/(?P<name>\w{5})','sdfs880/ksdjfksd')
print(ret7)
print(ret7.group())
print(ret7.group('id'))
print(ret7.group('name'))

#二、正则表达式的方法
#1、re.findall() 返回所有的内容保存到列表中
res21 = re.findall('ab','ahkshkfabjkjab')
print(res21)#['ab', 'ab']
#2、re.search  返回第一个匹配到第一个对象object，通过group返回获取返回值
res22 = re.search('ab','ahkshkfabjkjab')
print(res22.group())#ab
#3、re.match只在字符串的开始位置进行匹配，返回的是一个对象object，通过group返回获取返回值
res23 = re.match('ah','ahkshkfahjkjab')#ah
print(res23.group())
#4、re.split()按照前边的元字符进行匹配分割，先按照a进行分割后，再将得到的字符按照b进行分割，a前边没有字符所以会得到一个空格，直接返回列表
res24 = re.split('[a,h]','asjajiohako')
print(res24)#['', 'sj', 'jio', '', 'ko']
#5、re.sub()按照正则式进行替换，返回替换后的值
res25 = re.sub('w...d','jiangqijun','hello world')
print(res25)#hello jiangqijun
#6、re.compile()将正则式编译为模型，然后每次直接调用
model = re.compile('\.com')
print(model.findall('www.zaful.com'))#['.com']
