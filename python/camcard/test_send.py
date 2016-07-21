# coding:utf-8
from lxml import etree
import requests
# [getSummary]
url = 'http://srh.intsig.net/CCAppService/enterprise/getSummary?id=d761545f-3977-4d1c-845b-3bc71ec6b70a&token=86e3339b189cbdad8ea2be7e16b2a0f2&from=camcard&code=55626bb4842f096d448afeb3ae30ee7a3f41f84cfa4da82e80ab1fbbc6f7a0fd9302c896c5e456d29a41ec0a67248923&tip=746c6bb4842f096d448afeb3ae30ee562f41f84cfa4da82e80ab1fbbc6f7a0fd9302c896c5e456d29a41ec0a67248923&platform=WX&client_app=web&_=1468982989065&callback=jsonp2'
url = 'http://srh.intsig.net/CCAppService/enterprise/advanceSearch?keyword=杭州银行&domain=&start=0&token=EDC0D8D87FDB4A275h9707t6&from=searchBox&device_id=&client_app=cc_android'
# url = 'http://srh.intsig.net/CCAppService/enterprise/getReportList?id=d761545f-3977-4d1c-845b-3bc71ec6b70a&token=919ddd4bf51bda8f64bf799e2de1b7f0&from=camcard&code=746c6bb4842f096d448afeb3ae30ee7a91849d17805cc9b4ba099133d6ed7f30ab2e523e43e7c1399d989301f01dbaa2&tip=746c6bb4842f096d448afeb3ae30ee7a3f41f84cfa4da82e80ab1fbbc6f7a0fd9302c896c5e456d29a41ec0a67248923&platform=WX&client_app=web&start=0&_=1468982996560&callback=jsonp5'
# # url = 'http://srh.intsig.net/CCAppService/enterprise/getReportList?id=47752c63-7f7a-49b6-ab7d-a5fccae5fa86&token=919ddd4bf51bda8f64bf799e2de1b7f0&from=camcard&code=746c6bb4842f096d448afeb3ae30ee7a91849d17805cc9b4ba099133d6ed7f30ab2e523e43e7c1399d989301f01dbaa2&tip=746c6bb4842f096d448afeb3ae30ee7a91849d17805cc9b4ba099133d6ed7f30ab2e523e43e7c1399d989301f01dbaa2&platform=WX&client_app=web&start=0&_=1468985276642&callback=jsonp4'
# url = 'http://srh.intsig.net/CCAppService/enterprise/getTenderCount?name=%E6%9D%AD%E5%B7%9E%E9%A6%99%E6%B1%9F%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&from=camcard&code=746c6bb4842f096d448afeb3ae30ee7a91849d17805cc9b4ba099133d6ed7f30ab2e523e43e7c1399d989301f01dbaa2&tip=746c6bb4842f096d448afeb3ae30ee7a91849d17805cc9b4ba099133d6ed7f30ab2e523e43e7c1399d989301f01dbaa2&platform=WX&client_app=web&_=1468985272945&callback=jsonp3'
# url = 'http://srh.intsig.net/CCAppService/enterprise/getSummary?id=0d447143-9fc8-4cf8-a126-acb461962193&token=86eeae9b189cbdad8ea2be7e16b2a0f2&from=camcard&code=746c6bb4842f096d448afeb3ae30ee7a062b6b0215ef587eb1cce706cbc9020526684ac094cac1d309cdae2b4e19baa0&tip=746c6bb4842f096d448afeb3ae30ee7a062b6b0215ef587eb1cce706cbc9020526684ac094cac1d309cdae2b4e19baa0&platform=WX&client_app=web&callback=jsonp2'
# url = 'http://srh.intsig.net/CCAppService/enterprise/getSummary?id=769e33f9-f0c7-4a32-a48f-b6e1da935309&from=camcard&code=746c6bb4842f096d448afeb3ae30ee7aefa3af07a846d340a981f4145cf61da45ab479b118f34d38df76ae68f9b62338&tip=746c6bb4842f096d448afeb3ae30ee7aefa3af07a846d340a981f4145cf61da45ab479b118f34d38df76ae68f9b62338&platform=WX&client_app=web&_=1468990661147&callback=jsonp2'
url = 'http://srh.intsig.net/CCAppService/enterprise/getSummary?id=d1509c0c-e5cf-42f6-bcaf-24d5ef3efecc&token=737bd2297ac29873c37966f2092dc1c4&from=camcard&code=746c6bb4842f096d448afeb3ae30ee7a7815223b437ae023ec6712a22b639752623306fe2ac8c9f4f661f81fc25963ef&tip=746c6bb4842f096d448afeb3ae30ee7a7815223b437ae023ec6712a22b639752623306fe2ac8c9f4f661f81fc25963ef&platform=WX&client_app=web&_=1469002534576&callback=jsonp2'






proxies = {
    'http': '62.195.69.35:80',
    }
headers = {
    'User-Agent': 'User-Agent:Dalvik/2.1.0(Linux;U;Android5.1;m2Build/LMY47D)CamCard/7.0.0.20160707',
    'Host': 'srh.intsig.net',
    'Connection': 'Keep-Alive',
    'Connection': 'keep-alive',
    'X-Requested-With': 'com.intsig.BizCarReader',
}

# r = requests.get(url, headers=headers)
# print r.headers
# print r.cookies
# print r.text
# print r.request
# print r.reason
# print r.status_code
for x in range(1):
    r = requests.get(url, headers=headers)
    print r.text