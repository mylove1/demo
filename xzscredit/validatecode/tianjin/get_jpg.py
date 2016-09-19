# coding:utf-8

import requests
url = "http://tjcredit.gov.cn/verifycode?date=1474194064298"

for x in range(100):
    r = requests.get(url)
    with open("C:\Users\cooper\Desktop\opp%s.jpg"%x, 'wb') as f:
        f.write(r.content)
print r.status_code