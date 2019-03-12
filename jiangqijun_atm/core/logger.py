#!user/bin/env python
# -*- coding:utf-8 -*-
#__author__:jiangqijun
#__date__:2018/12/22

import logging, os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
sys.path.append(os.path.join(BASE_DIR, 'conf'))
from setting import LOG_LEVEL, LOG_TYPES

transaction_logg_path = os.path.join(os.path.join(BASE_DIR, 'log'), 'transactions.log')
access_logg_path = os.path.join(os.path.join(BASE_DIR, 'log'), 'access.log')

tansaction_logger = logging.getLogger('transaction')
tansaction_fh = logging.FileHandler(transaction_logg_path)
tansaction_fomater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s -line:-%(lineno)d')


def get_logger(logname):
    logg_path = os.path.join(os.path.join(BASE_DIR, 'log'), LOG_TYPES.get(logname))
    logger = logging.getLogger(logname)
    logger.setLevel(LOG_LEVEL)
    fh = logging.FileHandler(logg_path, encoding='utf-8')
    formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s -line:-%(lineno)d')
    fh.setFormatter(formater)
    logger.addHandler(fh)
    return logger

names = list(LOG_TYPES.keys())
t_logger = get_logger(names[0])
a_logger = get_logger(names[1])
t_logger.info('我是一条记录')