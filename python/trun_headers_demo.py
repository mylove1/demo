# coding:utf-8

headers = '''
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8
Connection:keep-alive
Cookie:test=20111112; JSESSIONID=0000lUG4aFlYI7eTvRC5MPCn792:-1; AD_VALUE=4537010d
Host:222.143.24.157
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
'''
headers = headers.replace('\n', "',\n'")
headers = headers.replace(':', "': '")
headers = ''.join(["'", headers, "'"])
headers = headers.replace("http': '", "http:")
print headers