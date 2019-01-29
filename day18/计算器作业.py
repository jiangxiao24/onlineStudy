#__author__:jiangqijun
#__date__:2018/12/5
import re
from decimal import *

def operate(op, x1, x2):
    if op == "*":
        res = x1 * x2
    elif op == "/":
        res = x1 / x2
    elif op == "+":
        res = x1 + x2
    elif op == "-":
        res = x1 - x2
    elif op == "*-":
        temp = x1*x2
        res = '-{0}'.format(temp)
    elif op == "/-":
        res = -(x1/x2)
    elif op == '+-':
        res = x1 - x2
    elif op == '--':
        res = x1 + x2
    return res


def match_op(s):
    while (re.search('[\d,\.,\-]+[*,/,+,\d,\-,\s,\.]+[\d,\.]+', s)!=None):
        res0 = re.search('[\d,\.,\-]+[*,/,+,\d,\-,\s,\.]+[\d,\.]+', s).group()
        while (re.search('[\d,\.]+[*,/][\-]?[\d,\.]+',res0)!=None):
            res1 = re.search('[\d,\.]+[*,/][\-]?[\d,\.]+',res0).group()
            op = re.findall('[\d,\.]+([*,/,\-]+)[\d,\.]+', res1)[0]
            x1 = float(re.findall('^([\d,\.]+)', res1)[0])
            x2 = float(re.search('([\d,\.]+)$', res1)[0])
            res1temp = operate(op, x1, x2)
            res0 = res0.replace(res1, str(res1temp))
        while (re.search('[\d,\.,\-]+[+,\-][\-]?[\d,\.]+', res0)!=None):
            res2 = re.search('[\d,\.,\-]+[+,\-][\-]?[\d,\.]+', res0).group()
            #如果是负数与加减运算结合则需要单独处理
            if re.search('^-[\d,\.]+[+,\-]+[\d,\.]+',res2)!=None:
                res3 = re.search('^-[\d,\.]+[+,\-]+[\d,\.]+',res2).group()
                optemp = re.findall('[\d,\.]+([+\-]+)[\d,\.]+', res3)[0]
                x1 = float(re.findall('^-([\d,\.]+)', res3)[0])
                x2 = float(re.search('([\d,\.]+)$', res3).group())
                if optemp == "+-":
                    temp = x1+x2
                    res3temp = '-{0}'.format(temp)
                elif optemp == "+":
                    res3temp = x2-x1
                elif optemp == "--":
                    res3temp = x2-x1
                elif optemp == "-":
                    temp = x1 + x2
                    res3temp = '-{0}'.format(temp)
            else:
                res3 = re.search('[\d,\.]+[+,\-]+[\d,\.]+', res2).group()
                op = re.findall('[\d,\.]+([+,\-]+)[\d,\.]+', res3)[0]
                x1 = float(re.findall('^([\d,\.]+)', res3)[0])
                x2 = float(re.search('([\d,\.]+)$', res3)[0])
                res3temp = operate(op, x1, x2)
            res0 = res0.replace(res3, str(res3temp))
        s = s.replace(re.search('[\d,\.,\-]+[*,/,+,\d,\-,\s,\.]+[\d,\.]+', s).group(),res0)
        if re.search('[^+,*,/]+',s).group()==s:
            break
    return s


#用于外层的括号匹配
def match_brackets(s):
    while (re.search('\(([^\(\)]+)\)',s)!=None):
        res0 = re.findall('\(([^\(\)]+)\)', s)
        for ss in res0:
            if re.search('[^+,*,/]+',ss).group() == ss:
                s = s.replace('('+ss+')', ss)
            res1 = match_op(ss)
            s = s.replace(ss, str(res1))
    return match_op(s)

s = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3+52)/(16-3*2))'
print(match_brackets('1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3+52)/(16-3*2))'))