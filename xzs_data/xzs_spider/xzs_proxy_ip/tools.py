# coding:utf-8
"""
写了几个在这个项目中能用到的工具
"""
import requests

from config import TEST_URL
from config import CHECK_LENTH

def ip_test(ip):
    '''
    :param ip:是形如 192.168.0.1:8000 这种格式的文本
    :return: True or False
    '''
    url = TEST_URL
    try:
        r = requests.get(url, proxies={"http": ip}, timeout=7)
        if len(r.text) == CHECK_LENTH:
            return True
        else:
            return False
    except:
        return False




if __name__ == '__main__':
    ip = requests.get('http://192.168.0.50:8384/ip').text
    while 1:
        if ip_test(ip):
            print 'ok'
        else:
            print 'no'
