# coding:utf-8
import requests

url = 'http://api.tianyancha.com/services/v3/t/details/wapCompany/667936445'
headers = {
    "version": "Android 1.2.16",
    "Authorization": "J/Su/BjwjmDbcbZzc5WxMqKebNl3cbokpAEycENUyL21fZqX322xVg==",
    "X-Auth-Token": "",
    "User-Agent": "Dalvik/1.6.0 (Linux; U; Android 4.2.2; Droid4X-WIN Build/JDQ39E)",
    "Host": "api.tianyancha.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
}
r = requests.get(url, headers)
print r.text


# GET /services/v3/t/details/wapCompany/667936445 HTTP/1.1
# Authorization: J/Su/BjwjmDbcbZzc5WxMqKebNl3cbokpAEycENUyL21fZqX322xVg==
# version: Android 1.2.16
# X-Auth-Token:
# User-Agent: Dalvik/1.6.0 (Linux; U; Android 4.2.2; Droid4X-WIN Build/JDQ39E)
# Host: api.tianyancha.com
# Connection: Keep-Alive
# Accept-Encoding: gzip