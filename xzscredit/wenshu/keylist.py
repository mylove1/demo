# coding:utf-8

import requests
import time
import threading

class getcount(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def url_list(self, url, data):
        req = requests.post(url=url, data=data)
        html = req.text[1:-1].replace('\\', '')
        if len(html) < 100:
            print html
        return list(eval(html))

    def url_total(self, url, data):
        l = self.url_list(url, data)
        return l[0]["Value"]

    def run(self):
        while True:
            data = globallist.pop()
            count = self.url_total(url, data)
            total += int(count)
            print total
            print data["Param"], count


if __name__ == '__main__':
    globallist = []
    global total
    total = 0
    url = 'http://wenshu.court.gov.cn/List/TreeContent'
    birth_secds = 1469319414
    data={"Param": ""}
    for x in range(10000):
        tup_birth = time.localtime(birth_secds)
        format_birth = time.strftime("%Y-%m-%d",tup_birth)
        if not format_birth == '2015-10-01':
            birth_secds -= 86400
            globallist.append({"Param":"上传日期:" + format_birth})
        else:
            break
    print len(globallist)
    for thread in range(0, 10):
        t = getcount()
        t.start()

