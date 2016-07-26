# -*- coding:utf-8 -*-
import requests

url = "http://httpbin.org/ip"
url = 'http://wenshu.court.gov.cn/List/ListContent'
# url = "http://www.baidu.com"
print 'a'
data = {
    'Param': '上传日期:2016-07-22,案件类型:刑事案件',
    'Index': '1',
    'Page': '5',
    'Order': '法院层级',
    'Direction': 'asc',
}
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
    'http': '120.52.73.30:80',
    'http': '204.29.120.89:120'
}
r = requests.post(url, timeout=3, data=data, proxies=proxies)
print len(r.text)
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
