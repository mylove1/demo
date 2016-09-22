# coding:utf-8

import requests
url = "http://gsxt.ngsh.gov.cn/ECPS/verificationCode.jsp?_=1474534287596"

for x in range(100, 200):
    r = requests.get(url)
    with open(r"C:\Users\cooper\Desktop\opp\ningxia\%s.jpg"%x, 'wb') as f:
        f.write(r.content)
print r.status_code