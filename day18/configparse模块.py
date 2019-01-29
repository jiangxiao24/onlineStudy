#__author__:jiangqijun
#__date__:2018/11/29
import configparser
#配置文件用来保存基本路径，经常变更的数据
#一、这里创建了三个大模块，DEFAULT,bitbucket.org,topsecret.server.com

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'ServerAliveInterval':'45',
    'Compression':'yes',
    'CompressionLevel':'9'
}

config['bitbucket.org'] = []
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '66666'
topsecret['ForwardX11'] = 'no'
config['DEFAULT']['ForwardX11'] = 'yes'


with open('example.ini','w') as configfile:
    config.write(configfile)

#二、读取配置文件
config.read('example.ini')#['example.ini']
print(config.sections())#读取出除了defaults外的区域 ['bitbucket.org', 'topsecret.server.com']
print(config.defaults())#读取出所有的默认项
for key in config['bitbucket.org']: #打印出除了bitbucket.org之外还有default里边的
    print(key)
config['DEFAULT']['Compression']#yes

#三、删除
config.remove_section('topsecret.server.com')#删除掉这个区域

#四、修改时做一个覆盖而不是修改
config.set('topsecret.server.com','Host Port','888')

with open('','w') as configfile:
    config.write(configfile)