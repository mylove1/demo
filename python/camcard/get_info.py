# coding: utf-8
import requests
import time

name_list = [
'%e4%b8%8a%e6%b5%b7+%e5%b7%a5%e5%95%86',
'%e4%b8%8a%e6%b5%b7+%e5%a4%a7',

]

headers = {
    'User-Agent': 'User-Agent:Dalvik/2.1.0(Linux;U;Android5.1;m2Build/LMY47D)CamCard/7.0.0.20160707',
    'Host': 'srh.intsig.net',
    'Connection': 'Keep-Alive',
    'Connection': 'keep-alive',
    'X-Requested-With': 'com.intsig.BizCarReader',
}
code = ''
token = 'EDC0D8D87FDB4A275h9707t6'
def get(type, id, token, headers, xhx, callbacktype):
    url = 'http://srh.intsig.net/CCAppService/enterprise/\
        %s?id=%s&token=%s&type=&from=camcard&code=%s&tip=%s&\
        platform=WX&client_app=web&start=0&_=%s&\
        callback=%s' % (type, id, token, code, tip, callbacktype)
    r
def advanceSearch(keyword, token, headers):
    url = 'http://srh.intsig.net/CCAppService/enterprise/advanceSearch?\
        keyword=%s&domain=&start=0&token=%s&from=searchBox\
        &device_id=867575026347925&client_app=cc_android' % (keyword, token)
    r = requests.get(url, headers=headers)
    print r.text
    print "sleep"
    time.sleep(2)


def getsummary(id, code, tip, headers):
    url = 'http://srh.intsig.net/CCAppService/enterprise/getSummary?id=%s&from=camcard&code=%s&tip=%s&platform=WX&client_app=web&_=1469002534576&callback=jsonp2' % (id, code, tip)
    headers = headers
    r = requests.get(url, headers=headers)
    print r.text
    print "sleep"
    time.sleep(2)


def getmulticompany(idlist, code, tip, headers):
    idlist = '%'.join(idlist)
    url = 'http://srh.intsig.net/CCAppService/enterprise/getMultiCompany?idlist=%s&from=camcard&code=%s&tip=%s&platform=WX&client_app=web&_=1469003784970&callback=jsonp4' % (idlist, code, tip)
    headers = headers
    r = requests.get(url, headers=headers)
    print r.text
    print "sleep"
    time.sleep(2)


def getdetail(id, code, tip, headers):
    url = 'http://srh.intsig.net/CCAppService/enterprise/getDetail?id=%s&from=camcard&code=%s&tip=%s&platform=WX&client_app=web&_=1469003784970&callback=jsonp4' % (id, code, tip)
    r = requests.get(url, headers=headers)
    print r.text
    print "sleep"
    time.sleep(2)


def getreportdetail(id, token, code, tip, headers):
    url = 'http://srh.intsig.net/CCAppService/enterprise/getReportDetail?id=%s&year=2015&token=%s&from=camcard&code=%s&tip=%s&platform=WX&client_app=web&_=1469006790532&callback=jsonp6' % (id, token, code, tip)
    r = requests.get(url, headers=headers)
    print r.text

# 商标详情：
def gettrademarklist(id, token, code, tip, headers):
    url = 'http://srh.intsig.net/CCAppService/enterprise/getTrademarkList?id=%s&token=%s&type=&from=camcard&code=%s&tip=%s&platform=WX&client_app=web&start=0&_=1469008251235&callback=jsonp4' % (id, token, code, tip)
    r = requests.get(url, headers=headers)
    print r.text


def getdomainlist(id, token, code, tip, headers):
    url = 'http://srh.intsig.net/CCAppService/enterprise/getDomainList?id=%s&token=%s&type=&from=camcard&code=%s&tip=%s&platform=WX&client_app=web&start=0&_=1469007858347&callback=jsonp5' % (id, token, code, tip)
    r = requests.get(url, headers=headers)
    print r.text

# 专利详情
def getpatents(id, token, code, tip, headers):
    url = 'http://srh.intsig.net/CCAppService/enterprise/getPatents?id=%s&token=%s&type=&from=camcard&code=%s&tip=%s&platform=WX&client_app=web&start=0&_=1469009276918&callback=jsonp5' % (id, token, code, tip)
    r = requests.get(url, headers=headers)
    print r.text

# 软件著作权

if __name__ == '__main__':

    token = 'f237df4008429fdc3c1a8943eed351e6'
    com_id = '37335a7f-8f2a-4b1d-a3cf-a88b4cc7c045'
    com_idlist = ['dbecd873-985f-4cdf-a10c-896f94ada75f',
                  '2C78293706-aed6-4067-8b45-bf34f2213ad0',
                  '2C2af348d3-a7c5-46fa-8622-2237a93d834b']
    code = '746c6bb4842f096d448afeb3ae30ee7a1448d78df0b9d82e9fbb082f0e78efc1d2c75b482854c6bced19879f61b0ae60'
    tip = code
    # advanceSearch(name_list[1],token,headers=headers)
    # getsummary(com_id, code, tip, headers)
    # getmulticompany(com_idlist, code, tip, headers)
    # getdetail(com_id, code, tip, headers)
    # getreportdetail(com_id, token, code, tip, headers)
    # gettrademarklist(com_id, token, code, tip, headers)
    # getdomainlist(com_id, token, code, tip, headers)
    getpatents(com_id, token, code, tip, headers)