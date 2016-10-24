# coding:utf-8

import requests

url = "http://gsxt.cqgs.gov.cn/search_getEnt.action?_c1476350804521=_c783441&entId=50021071201506231070054&id=500107008127032&stype=SAIC&type=1"
r = requests.get(url)
a = r.text
print a
print len(r.text)