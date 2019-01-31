#!user/bin/env python
# -*- coding:utf-8 -*-
#__author__:jiangqijun
#__date__:2019/1/30

goods_list = [["1.", "iphone6s", "5800"], ["2.", "mac book", "5900"], ["3.", "coffee", "32"],
              ["4.", "python book", "80"],["5.", "bicycle", "1500"]]
salary = int(input("你的工资是:"))
addGoods = '''
>>>:
%s'''%salary
print(addGoods)
for i in range(len(goods_list)):
    print(goods_list[i][0]+" "+goods_list[i][1]+" "+goods_list[i][2])
flag = True
remain = salary
while(flag):
    choosed_no = 0
    print(">>>:")
    choosed_no_temp = input()
    if choosed_no_temp.isdigit():
        choosed_no = int(choosed_no_temp)
        if choosed_no>5:
            print("请输入正确的选项")
            break
    else:
        print("欢迎下次光临!")
        break
    temp = int(goods_list[choosed_no-1][2])
    if (remain-temp) >= 0:
        remain = remain-temp
        msg = """已加入%s到你的购物车，当前余额：%s
        """%(goods_list[choosed_no-1][1], remain)
        print(msg)
    else:
        msg = """余额不足，%s
        """ % (remain-temp)
        print(msg)
        flag = False