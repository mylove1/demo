headers = '''
Accept:*/*
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8
Connection:keep-alive
Cookie:_GCWGuid=7E250C80-BF9A-083C-5C3C-2656AA2B020E; gr_user_id=64a24efc-0103-4082-b1a6-f849a62dbf40; _auth=rcKhA4FVjJjEE5jIKttZmczp43e5Op04QRgj8eA5ramd%2FLT7wGTlOc7GA4EP3xJFyunLWyTsb%2BI9%2FYaBDT6xNt6RneSnYg1Ci%2B5Z%2F3NCjI%2FyjcwizqzQS29HFlnzsM9g; Hm_lvt_bf959def12cb728de8b9fca745e166a7=1470190130,1471404445,1471410433,1471933088; Hm_lpvt_bf959def12cb728de8b9fca745e166a7=1471933408; AJSTAT_ok_pages=7; AJSTAT_ok_times=15; a7123_pages=6; a7123_times=12
Host:company.xizhi.com
Referer:http://company.xizhi.com/GS570826931f98cc273d8b495b/
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
X-Requested-With:XMLHttpRequest
'''
headers = headers.replace('\n', "',\n'")
headers = headers.replace(':', "': '")
headers = ''.join(["'", headers, "'"])
headers = headers.replace("http': '", "http:")
print headers