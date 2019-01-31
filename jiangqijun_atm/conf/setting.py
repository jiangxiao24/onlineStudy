#!user/bin/env python
# -*- coding:utf-8 -*-
#__author__:jiangqijun
#__date__:2018/12/22


import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))

DATABASE = {
    'engine': 'mysql',
    'name': 'accounts',
    'path': '%s/db' %BASE_DIR
}

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log'
}

TRANSACTION_TYPE = {
    'repay': {'action': 'plus', 'interest': 0},
    'withdraw': {'action': 'minus', 'interest': 0.05},
    'transfer': {'action': 'minus', 'interest': 0.05},
    'consume': {'action': 'minus', 'interest': 0}
}
ACCOUNTS = {
    'jiangqijun': '123456',
    'xiaoming': '000000',
    'xiaohua': '654321'
}