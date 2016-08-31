# coding:utf-8
import requests
import re

def posthtml(page):
    url = 'http://www.sgs.gov.cn/notice/search/ent_except_list'
    data = {'captcha': '-1',
'condition.pageNo': '1',
'condition.insType': '',
'condition.keyword': '莹达戈',}
    while 1:
        try:
            return requests.post(url, data=data).text
        except:
            continue
for x in range(1, 2):#76367):
    html = posthtml(x)
    print html
    for y in re.findall('href="(http://wsgs\.fjaic\.gov\.cn/creditpub/notice/view.*?)" target="_blank">(.*?)</a>', html):
        print y