# coding:utf-8
import requests

def posthtml(page):
    url = 'http://wsgs.fjaic.gov.cn/creditpub/search/ent_except_list'
    data = {'captcha': '',
            'condition.pageNo': page,
            'condition.insType': '',
            'condition.keyword': ''}
    while 1:
        try:
            return requests.post(url, data=data).text
        except:
            continue
for x in range()