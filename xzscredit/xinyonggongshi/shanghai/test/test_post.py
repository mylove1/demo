# coding:utf-8
import requests
import re


def posthtml(page):
    url = 'http://www.sgs.gov.cn/notice/search/ent_except_list'
    data = {'captcha': '',
            'condition.pageNo': page,
            'condition.insType': '',
            'condition.keyword': '莹达戈（上海）陶瓷国际贸易有限公司'}
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