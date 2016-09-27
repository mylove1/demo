# coding:utf-8

headers = '''
Accept:image/webp,image/*,*/*;q=0.8
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8
Connection:keep-alive
Cookie:BIGipServerpool_gsp=3456018624.24841.0000; JSESSIONID=79QRXy0Lb1xwJvxdnr3LJJWyNXwvZLxnJRPkPnrDX1FcH5nRpQ1m!775123446
Host:www.jsgsj.gov.cn:58888
Referer:http://www.jsgsj.gov.cn:58888/province/
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
'''
headers = headers.replace('\n', "',\n'")
headers = headers.replace(':', "': '")
headers = ''.join(["'", headers, "'"])
headers = headers.replace("http': '", "http:")
print headers