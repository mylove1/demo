# coding:utf-8

headers = '''
Accept:*/*
Accept-Encoding:gzip, deflate, sdch, br
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:no-cache
Connection:keep-alive
Cookie:JSESSIONID=60D42694D98B4CB1A22D22F1FE7DFA97; BIGipServerotn=368050698.64545.0000; _jc_save_fromStation=%u5B89%u9633%2CAYF; _jc_save_toStation=%u5E7F%u5DDE%2CGZQ; _jc_save_fromDate=2016-10-03; _jc_save_wfdc_flag=dc
Host:kyfw.12306.cn
If-Modified-Since:0
Referer:https://kyfw.12306.cn/otn/lcxxcx/init
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
X-Requested-With:XMLHttpRequest
'''
headers = headers.replace('\n', "',\n'")
headers = headers.replace(':', "': '")
headers = ''.join(["'", headers, "'"])
headers = headers.replace("http': '", "http:")
print headers