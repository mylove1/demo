# coding:utf-8

import requests
url = "http://qyxy.baic.gov.cn/CheckCodeCaptcha?currentTimeMillis=1474626756666&num=7585"

for x in range(597, 800):
    r = requests.get(url)
    with open(r"C:\Users\cooper\Desktop\opp\beijing\a\%s.jpg"%x, 'wb') as f:
        f.write(r.content)
print r.status_code