# coding:utf-8
import requests
url = "http://gsxt.zjaic.gov.cn/search/doGetAppSearchResult.do"
data ={
    "clickType": "1",
    "verifyCode": "13",
    "name": "%E6%9D%AD%E5%B7%9E%E9%93%B6%E8%A1%8C%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8"
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '121',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSESSIONID=09CEE65140BF193591113BB6E51AC6FB.gsxt46; CNZZDATA1000503299=1781526156-1466650590-null%7C1471418465',
    'Host': 'gsxt.zjaic.gov.cn',
    'Origin': 'http://gsxt.zjaic.gov.cn',
    'Referer': 'http://gsxt.zjaic.gov.cn/search/doEnGeneralQueryPage.do',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

}
r = requests.post(url, headers=headers, data=data)

print r.text
print r.status_code