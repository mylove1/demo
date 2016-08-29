headers = '''
captcha:
condition.pageNo:7
condition.insType:
session.token:d22a8c09-d52a-47cc-9ee6-ce73b8a20048
condition.keyword:
'''
headers = headers.replace('\n', "',\n'")
headers = headers.replace(':', "': '")
headers = ''.join(["'", headers, "'"])
headers = headers.replace("http': '", "http:")
print headers