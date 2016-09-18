# coding:utf-8
import requests
import re

def posthtml(page):
    url = 'http://tjcredit.gov.cn/platform/saic/search.ftl'
    data = {'Host': 'qyxy.baic.gov.cn',
'Origin': 'http://qyxy.baic.gov.cn',
'Referer': 'http://qyxy.baic.gov.cn/gjjbj/gjjQueryCreditAction!getBjQyList.dhtml',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            }
    headers = {}
    while 1:
        try:
            return requests.post(url, data=data)
        except:
            continue
for x in range(1, 2):#76367):

    r = posthtml(x)
    r.encoding("utf-8")
    print r.text
    print r.url

    # for y in re.findall('href="(http://wsgs\.fjaic\.gov\.cn/creditpub/notice/view.*?)" target="_blank">(.*?)</a>', html):
    #     print y