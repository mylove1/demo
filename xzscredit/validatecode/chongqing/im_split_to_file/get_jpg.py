# coding:utf-8

import requests
url = "http://gsxt.cqgs.gov.cn/sc.action?width=130&height=40&fs=23&t=1474620448546"
for x in range(0,400):
    while 1:
        print x
        try:
            r = requests.get(url)
            with open(r"C:\Users\cooper\Desktop\opp\chongqing\a\%s.jpg"%x, 'wb') as f:
                f.write(r.content)
            break
        except:
            continue
