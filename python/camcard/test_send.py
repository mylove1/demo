# coding:utf-8
from lxml import etree
import requests

url = 'http://srh.intsig.net/CCAppService/enterprise/advanceSearch?keyword=hua%27bei&domain=&start=0&token=ad7af17319b90a9ff62cc2823bf9e1d2&from=searchBox&device_id=867575026347925&client_app=cc_android'
headers = {
    'User-Agent': 'User-Agent:Dalvik/2.1.0(Linux;U;Android5.1;m2Build/LMY47D)CamCard/7.0.0.20160707',
    'Host': 'srh.intsig.net',
    'Connection': 'Keep-Alive',
}

r = requests.get(url, headers=headers)
print r.headers
print r.cookies
print r.text
print r.request
print r.reason