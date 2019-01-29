#__author__:jiangqijun
#__date__:2018/11/27

import logging

#根据不同的级别只打印出warning error citical
# logging.debug('logging debug')
# logging.info('logging info')
# logging.warning('logging warning')
# logging.error('logging error')
# logging.critical('logging critical')

#四个类
#1、logger = logging.getLogger('loggname')获取一个logger类
#2、fh = logging.FileHandler('log.txt')获取保存文件.
#3、formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s -line:-%(lineno)d')设置格式
#4、fh.setFormatter(formater)引用格式
#5、logger.addHandler(fh)添加到输出文件
logger = logging.getLogger('loggname')
logger.setLevel('DEBUG')
fh = logging.FileHandler('log.txt')
ch = logging.StreamHandler()
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s -line:-%(lineno)d')
fh.setFormatter(formater)
ch.setFormatter(formater)
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('logging debug')
logger.info('logging info')
logger.warning('logging warning')
logger.error('logging error')
logger.critical('logging critical')

