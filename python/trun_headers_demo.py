# coding:utf-8

headers = '''
Host:www.jsgsj.gov.cn:58888
Origin:http://www.jsgsj.gov.cn:58888
Referer:http://www.jsgsj.gov.cn:58888/ecipplatform/inner_ci/ci_queryCorpInfor_gsRelease.jsp
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
X-Requested-With:XMLHttpRequest
'''
headers = headers.replace('\n', "',\n'")
headers = headers.replace(':', "': '")
headers = ''.join(["'", headers, "'"])
headers = headers.replace("http': '", "http:")
print headers