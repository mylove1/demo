# coding:utf-8
import requests
import re

def posthtml(page):
    url = 'http://wsgs.fjaic.gov.cn/creditpub/search/ent_except_list'
    data = {'captcha': '4',
'condition.pageNo': page,
'condition.insType': '',
'condition.keyword': '',}
    while 1:
        try:
            return requests.post(url, data=data).text
        except:
            continue
for x in range(58, 59):#76367):
    html = posthtml(x)
    print html
    for y in re.findall('href="(http://wsgs\.fjaic\.gov\.cn/creditpub/notice/view.*?)" target="_blank">(.*?)</a>', html):
        print y