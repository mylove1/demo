headers = '''Accept:text/plain, */*; q=0.01
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.8
Connection:keep-alive
Content-Length:173
Content-Type:application/x-www-form-urlencoded; charset=UTF-8
Cookie:Hm_lvt_0076fef7e919d8d7b24383dc8f1c852a=1470374349,1471396634,1471424655,1471431058; Hm_lpvt_0076fef7e919d8d7b24383dc8f1c852a=1471835249
Host:www.creditchina.gov.cn
Origin:http://www.creditchina.gov.cn
Referer:http://www.creditchina.gov.cn/search_all
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
X-Requested-With:XMLHttpRequest
'''
headers = headers.replace('\n', "',\n'")
headers = headers.replace(':', "': '")
headers = ''.join(["'", headers, "'"])
headers = headers.replace("http': '", "http:")
print headers