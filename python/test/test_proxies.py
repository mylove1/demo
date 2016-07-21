# -*- coding:utf-8 -*-
import requests

url = "http://httpbin.org/ip"
# url = "http://www.baidu.com"
print 'a'

proxies = {
    # 'http': '36.250.69.4:80',
    # 'http': '58.19.222.139:3128',
    # 'http': '101.251.199.66:3128',
    # 'http': '39.87.17.93:81',
    # 'http': '27.151.220.15:8888',
    # 'http': '5.196.94.27:3128',
    # 'http': '158.181.145.219:3128',
    # 'http': '163.125.195.45:9999',
    # 'http': '62.195.69.35:80',
    'http': '46.129.14.37:80'
    }
r = requests.get(url, timeout=10, proxies=proxies)
print r.text
#
# def try_speed(url):
#     try:
#         r = requests.get(url, timeout=10, proxies=proxies)
#         return r.elapsed.total_seconds()
#     except requests.exceptions.ProxyError:
#         return 11
#     except requests.exceptions.ConnectTimeout:
#         return 10

#
#
# try:
#     r = requests.get(url, timeout=10, proxies=proxies)
#     print(r.text)
#     print(r.elapsed.total_seconds())  # return type float
# except requests.exceptions.ProxyError:
#     print('ProxyError')
# except requests.exceptions.ConnectTimeout:
#     print('timeout')
