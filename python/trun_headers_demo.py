# coding:utf-8

headers = '''
Accept:image/webp,image/*,*/*;q=0.8
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8
Connection:keep-alive
Cookie:JSESSIONID=D64EA66A81DC1C0C6EDADBBC1289D447; ROBOTCOOKIEID=23f9b3400417aeaa5b8f2caf5952794dcd27ab8d; SECSESSIONID=93d925b9d2436a0ef5a6382fad6915b8; CNZZDATA1000300906=314635445-1474529997-http%253A%252F%252F211.141.74.198%253A8081%252F%7C1474700656
Host:211.141.74.198:8081
Referer:http://211.141.74.198:8081/aiccips/
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
'''
headers = headers.replace('\n', "',\n'")
headers = headers.replace(':', "': '")
headers = ''.join(["'", headers, "'"])
headers = headers.replace("http': '", "http:")
print headers