# coding:utf-8
import requests
import re


def posthtml(page):
    url = 'http://www.sgs.gov.cn/notice/search/ent_info_list'
    data = {'searchType': '1',
            'captcha': '-1',
            'condition.insType': '',
            'condition.keyword': u'上海宝冶集团有限公司',
            'session.token': '8465d190-891a-44c4-9ece-1d9a1ff43ea4'}
    while 1:
        try:
            return requests.post(url, data=data).text
        except:
            continue

for x in range(1, 2):
    html = posthtml(x)
    print html
    for y in re.findall('href="(https://www\.sgs\.gov\.cn/notice/notice/view.*?)" target="_blank">(.*?)</a>', html):
        print y
