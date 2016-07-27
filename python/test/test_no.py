# coding=utf-8
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
    'Referer': 'http://wenshu.court.gov.cn/List/ListContent',
    'Connection': 'keep-alive',
}

data = {
    'Param': '上传日期:2016-07-22,案件类型:刑事案件',
    'Index': '1',
    'Page': '5',
    'Order': '法院层级',
    'Direction': 'asc',
}
url = 'http://wenshu.court.gov.cn/List/ListContent'
# '?Param=上传日期:2016-07-22,案件类型:刑事案件&Index=1&Page=5&Order=法院层级&Direction=asc'

r = requests.get(url)
print r.text