# coding:utf-8

headers = '''
Accept:*/*
Accept-Encoding:gzip, deflate, sdch, br
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:no-cache
Connection:keep-alive
Cookie:JSESSIONID=0A01D73198D3C40D7FBFD15802460C6E56DDBC5BD5; __NRF=0BDC5FA0E3AAD37AE95B25BE765D3C15; BIGipServerotn=836174090.38945.0000; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5317%u4EAC%2CBJP; _jc_save_fromDate=2016-09-08; _jc_save_wfdc_flag=dc
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