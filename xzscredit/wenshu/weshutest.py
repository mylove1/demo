# coding:utf-8
import requests



data = {
    'Param': u"全文检索:" + "华为技术有限公司",
    'Index': 1,
    'Page': '20',
    'Order': '裁判日期',
    'Direction': 'asc',
}

this_headers = {
    'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    'Referer': 'http://wenshu.court.gov.cn/List/ListContent',
    'Connection': 'keep-alive',
}

proxy = requests.get('http://192.168.0.20:8384/ip').text
r = requests.post('http://wenshu.court.gov.cn/List/ListContent', headers=this_headers, data=data, proxies={'http': proxy}, timeout=7)
