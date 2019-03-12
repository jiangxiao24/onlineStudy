#!user/bin/env python
# -*- coding:utf-8 -*-
#__author__:jiangqijun
#__date__:2018/12/22

import os,sys
from conf.setting import ACCOUNTS
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os_windows = sys.platform
if os_windows == 'win32':
    goal_path = os.path.join(os.path.join(BASE_DIR, 'db'), 'accounts')


def create_account(name, password, init_banlance, real_banlance, status):
    names = os.listdir(goal_path)
    # 判断文档是否在存在不存在则创建
    if name not in names:
        goal = os.path.join(goal_path, name)
        with open(goal, 'a+', encoding='utf-8') as f:
            info = {'name': name, 'password': password, 'init_banlance': init_banlance, 'real_banlance': real_banlance, 'status': status}
            f.write(json.dumps(info))

def show_info(name):
    goal = os.path.join(goal_path, name)
    with open(goal, 'r', encoding='utf-8') as f:
        info = json.loads(f.readline())
        print(info)
        return info

def login(fuc):
    def actul_action():
        flag = True
        while flag:
            username = input("请输入用户名:")
            password = input("请输入密码：")
            names = os.listdir(goal_path)
            if username not in names:
                print("帐号不存在")
            else:
                with open(os.path.join(goal_path, username), 'r+', encoding='utf-8') as f:
                    record = json.loads(f.readline())
                    u = record.get('name')
                    p = record.get('password')
                    if username == u and password == p:
                        fuc()
                        flag = False
    return actul_action

@login
def shopp():
    print("欢迎来到购物页面")

@login
def account_info():
    print("欢迎查看个人信息")

#create_account('jiangqijun', '123456', 15000, 15000, True)