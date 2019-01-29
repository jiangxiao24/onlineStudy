#__author__:jiangqijun
#__date__:2018/10/14

# data = {1:["湖南省",[{1:["长沙市",{1:"岳麓区",2:"芙蓉区",3:"开福区"}]},{2:["永州市",{1:"祁阳县",2:"东安县",3:"宁远县"}]}]],
#          2:["广东省",[{1:["深圳市",{1:"南山区",2:"福田区",3:"罗湖区"}]},{2:["广州市",{1:"天河区",2:"白云区",3:"黄浦区"}]}]],
#          3:["北京市",[{1:["北京市",{1:"朝阳区",2:"海淀区",3:"房山区"}]}]]
#          }
data = {
    "湖南省":{
    "长沙市":{
        "岳麓区":"岳麓山",
        "芙蓉区":"湖南卫视",
        "开福区":"玛兰坡"
    },
    "永州市":{
        "祁阳县":"祁阳一中",
        "东安县":"东安一中",
        "宁远县":"宁远一中"
    }
},
    "广东省":{
        "深圳市":{
            "南山区":"深圳大学",
            "福田区":"深圳图书馆"
        },
        "广州市":{
            "天河区":"华农",
            "白云区":"白云山"
        }
    }
}
'''
parent_layers = []
current_layer = data

while(True):
    for key in current_layer:
        print(key)
    choice = input("请选择：>>>").strip()
    if(len(choice)==0):continue
    if choice in current_layer:
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b':
        if parent_layers:
            current_layer = parent_layers.pop()
    else:
        print("无此项")
        break;
'''
