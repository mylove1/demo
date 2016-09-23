# coding:utf-8

import requests
url = "http://www.jsgsj.gov.cn:58888/province/rand_img.jsp?type=7&temp=Fri%20Sep%2023%202016%2008:34:36%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)"

for x in range(0,1000):
    while 1:
        print x
        try:
            r = requests.get(url)
            with open(r"C:\Users\cooper\Desktop\opp\jiangsu\%s.jpg"%x, 'wb') as f:
                f.write(r.content)
            break
        except:
            continue
