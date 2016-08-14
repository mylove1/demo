# coding:utf-8
import requests
import threading
import re
import pymongo

# conn = pymongo.Connection("192.168.100.55", 27017)
# db = conn.zhejiang

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=1901E6FD9C9E3D18F0B4A6CE9EF4FDAB.gsxt46; CNZZDATA1000503299=1781526156-1466650590-null%7C1471067347',
    'Host': 'gsxt.zjaic.gov.cn',
    'Referer': 'http://gsxt.zjaic.gov.cn/appbasicinfo/doViewAppBasicInfo.do?corpid=06BA65EBF0DB1B27CF25D47D4F2FE4422777FAFEDD75046E039A8908B078AD0E&no=7',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

url = "http://gsxt.zjaic.gov.cn/appbasicinfo/doReadAppBasicInfo.do?corpid=06BA65EBF0DB1B27CF25D47D4F2FE4422777FAFEDD75046E039A8908B078AD0E"
data = {
    "qryParam": "",
    "pagination.currentPage": "1",
    "pagination.pageSize": "10",
}

r = requests.get(url, headers=headers)
print r.text



# text = r.text
# li = re.findall('''{"catRegNo":"(.*?)","corpid":"(.*?)","catRemark":".*?","catNo":"(.*?)","canOutReaCodeName":".*?","catState":".*?","catEntName":"(.*?)","catOrgName''', text)
# for x in li:
#     pagedict = {}
#     pagedict["catRegNo"] = x[0]
#     pagedict["corpid"] = x[1]
#     pagedict["catNo"] = x[2]
#     pagedict["catEntName"] = x[3]
#     db.yichanglist.insert(pagedict)
