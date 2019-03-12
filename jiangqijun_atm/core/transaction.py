#!user/bin/env python
# -*- coding:utf-8 -*-
#__author__:jiangqijun
#__date__:2018/12/22
import os, sys, json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'conf'))
from setting import TRANSACTION_TYPE
from logger import t_logger, a_logger

os_windows = sys.platform
if os_windows == 'win32':
    goal_path = os.path.join(os.path.join(BASE_DIR, 'db'), 'accounts')


def with_draw(name, count):
    """取现方法"""
    action = TRANSACTION_TYPE.get('withdraw').get('action')
    interest = float(TRANSACTION_TYPE.get('withdraw').get('interest'))
    with open(os.path.join(goal_path, name), 'r+', encoding='utf-8') as f:
        record = json.loads(f.readline())
        before_count = record.get('real_banlance')
        if action is 'plus':
            temp_banlance = int(before_count) + count*(1+interest)
        elif action is 'minus':
            temp_banlance = int(before_count) - count * (1 + interest)
        if temp_banlance >= 0:
            record['real_banlance'] = temp_banlance
            record_before = json.dumps(record)
            t_logger.info('{0}账户取款{1},手续费为{2},可用额度为:{3}'.format(name, count, interest, temp_banlance))
        else:
            print("你的账户余额不足,请确认后再操作！！！")

    with open(os.path.join(goal_path, name), 'w+', encoding='utf-8') as f:
        f.write(record_before)


def repay(name, count):
    """还款方法"""
    action = TRANSACTION_TYPE.get('repay').get('action')
    interest = float(TRANSACTION_TYPE.get('repay').get('interest'))
    with open(os.path.join(goal_path, name), 'r+', encoding='utf-8') as f:
        record = json.loads(f.readline())
        before_count = record.get('real_banlance')
        if action is 'plus':
            temp_banlance = int(before_count) + count * (1 + interest)
        elif action is 'minus':
            temp_banlance = int(before_count) - count * (1 + interest)
        record['real_banlance'] = temp_banlance
        record = json.dumps(record)
        t_logger.info('{0}账户还款{1},可用额度为:{2}'.format(name, count, temp_banlance))
    with open(os.path.join(goal_path, name), 'w+', encoding='utf-8') as f:
        f.write(record)


def transfer(name1, name2, count):
    """转账方法"""
    action = TRANSACTION_TYPE.get('transfer').get('action')
    interest = TRANSACTION_TYPE.get('transfer').get('interest')
    print(os.path.join(goal_path, name1))
    print(os.path.join(goal_path, name2))
    with open(os.path.join(goal_path, name1), 'r+', encoding='utf-8') as f1,\
            open(os.path.join(goal_path, name2), 'r+', encoding='utf-8') as f2:
        record1 = json.loads(f1.readline())
        record2 = json.loads(f2.readline())
        before_count1 = record1.get('real_banlance')
        before_count2 = record2.get('real_banlance')
        if action is 'plus':
            temp_banlance1 = int(before_count1) + count
            temp_banlance2 = int(before_count2) - count * (1 + interest)
        elif action is 'minus':
            temp_banlance1 = int(before_count1) - count * (1 + interest)
            t_logger.info('{0}转出{1}'.format(name1, count))
            temp_banlance2 = int(before_count1) + count
            t_logger.info('{0}收到{1}'.format(name2, count))
        if temp_banlance1 >= 0:
            record1['real_banlance'] = temp_banlance1
            record2['real_banlance'] = temp_banlance2
            record1 = json.dumps(record1)
            record2 = json.dumps(record2)
        else:
            print("账户余额不足以转出！！！")
    with open(os.path.join(goal_path, name1), 'w+', encoding='utf-8') as f1, \
            open(os.path.join(goal_path, name2), 'w+', encoding='utf-8') as f2:
        f1.write(record1)
        f2.write(record2)


def consume(name, count):
    """消费方法"""
    action = TRANSACTION_TYPE.get('consume').get('action')
    interest = float(TRANSACTION_TYPE.get('repay').get('interest'))
    with open(os.path.join(goal_path, name), 'r+', encoding='utf-8') as f:
        record = json.loads(f.readline())
        before_count = record.get('real_banlance')
        if action is 'plus':
            temp_banlance = int(before_count) + count * (1 + interest)
        elif action is 'minus':
            temp_banlance = int(before_count) - count * (1 + interest)
        if temp_banlance >= 0:
            record['real_banlance'] = temp_banlance
            record = json.dumps(record)
            t_logger.info('{0}账户消费{1}'.format(name, count))
        else:
            print("余额不足消费！！！")
    with open(os.path.join(goal_path, name), 'w+', encoding='utf-8') as f:
        f.write(record)


#with_draw('jiangqijun', 1000)
#transfer('jiangqijun', 'xiaoming', 200)
repay('xiaoming', 800)
consume('xiaoming', 200)