#__author__:jiangqijun
#__date__:2018/9/4

data1 = {"湖南省":[{"长沙市":["岳麓区","芙蓉区","开福区"]},{"永州市":["祁阳县","东安县","宁远县"]}],
        "广东省":[{"深圳市":["南山区","福田区","罗湖区"]},{"广州市":["天河区","白云区","黄浦区"]}],
        "北京市":[{"北京市":["朝阳区","海淀区","房山区"]}]}

data2 = {"1":{"湖南省":[{"长沙市":["岳麓区","芙蓉区","开福区"]},{"永州市":["祁阳县","东安县","宁远县"]}]},
         "2":{"广东省":[{"深圳市":["南山区","福田区","罗湖区"]},{"广州市":["天河区","白云区","黄浦区"]}]},
         "3":{"北京市":[{"北京市":["朝阳区","海淀区","房山区"]}]}}

choose_provice_num = ""
choose_city_num = ""
choose_county_num = ""
provice = ""
city = ""
county = ""
provice_flag = True
city_flag = True
county_flag = True
data = {1:["湖南省",[{1:["长沙市",{1:"岳麓区",2:"芙蓉区",3:"开福区"}]},{2:["永州市",{1:"祁阳县",2:"东安县",3:"宁远县"}]}]],
         2:["广东省",[{1:["深圳市",{1:"南山区",2:"福田区",3:"罗湖区"}]},{2:["广州市",{1:"天河区",2:"白云区",3:"黄浦区"}]}]],
         3:["北京市",[{1:["北京市",{1:"朝阳区",2:"海淀区",3:"房山区"}]}]]
         }
provice_msg = "1.%s\n2.%s\n3.%s\n"%(data[1][0], data[2][0], data[3][0])
while(provice_flag):
    print(provice_msg)
    choose_provice_num = input("请选择省级数字编号,如需退出请输入quit：")
    if choose_provice_num == "quit":
        break
    else:
        provice = data[int(choose_provice_num)][0]
        city_flag = True
        while(city_flag):
            for i in range(len(data)):
                if i == int(choose_provice_num) - 1:
                    for j in range(len(data[i + 1][1])):
                        city_msg = "%s.%s" % (str(j + 1), data[i + 1][1][j][j + 1][0])
                        print(city_msg)
                    choose_city_num = input("请选择市级数字编号,如需退出请输入quit，返回上一级输入back：")
                    if choose_city_num == "quit":
                        provice_flag = False
                        city_flag = False
                        break
                    elif choose_city_num == "back":
                        city_flag = False
                        break
                    else:
                        city = data[int(choose_provice_num)][1][int(choose_city_num) - 1][int(choose_city_num)][0]
                        for k in range(len(data[int(choose_provice_num)][1][int(choose_city_num) - 1][int(choose_city_num)][1])):
                            county_msg = "%s.%s" % (str(k + 1), data[int(choose_provice_num)][1][int(choose_city_num) - 1][int(choose_city_num)][1][k + 1])
                            print(county_msg)
                        county_flag = True
                        while(county_flag):
                            choose_county_num = input("请选择县级数字编号,如需退出请输入quit，返回上一级输入back：")
                            if choose_county_num == "quit":
                                provice_flag = False
                                city_flag = False
                                county_flag = False
                                break
                            elif choose_county_num == "back":
                                county_flag = False
                                break
                            else:
                                county = data[int(choose_provice_num)][1][int(choose_city_num) - 1][int(choose_city_num)][1][int(choose_county_num)]
                                choose_msg = "你选择的省市县为：%s,%s,%s" % (provice, city, county)
                                print(choose_msg)
                                city_flag = False
                                break