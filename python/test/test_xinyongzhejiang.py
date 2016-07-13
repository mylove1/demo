# coding:utf-8
import requests


def get_html(url, coo):
    payload = coo
    headers = {
        'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Accept':'Accept: text/javascript, application/javascript,\
         application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate',
        'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
        'X-Requested-With':'XMLHttpRequest',
        'Referer':'http://www.zjcredit.gov.cn/info/sincerityList.do?\
        id=E1629F9418A23FE1EE323A9C91C24AAC008665C958FCA09F9D58972B33953836',
        'Connection':'keep-alive'
    }
    cookie = {

    }
    r = requests.post(url, data=payload, headers=headers, cookies = cookie)
    return r.text



url = 'http://www.zjcredit.gov.cn/info/promptsProxy.do?startrecord=481&endrecord=560&perpage=10&totalRecord=1456'
coo = {
    'startrecord':'481',
    'endrecord':'560',
    'perpage':'10',
    'totalRecord':'1456'
}
print get_html(url, coo)
