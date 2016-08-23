# coding:utf-8
import re
import requests

url = 'http://www.xizhi.com/search?wd=%E5%B9%B3%E9%A1%B6%E5%B1%B1%E5%B8%82%E7%A7%91%E8%BF%9C'
r = requests.get(url)
r.encoding = 'utf-8'
html = ''.join(r.text.split())
# 匹配搜索后列表页的企业名与连接
rea = re.compile('(http://company\.xizhi\.com/GS.*?/)')
namelist = rea.findall(r.text)
namelist = list(set(namelist))

for x in namelist:
    print x