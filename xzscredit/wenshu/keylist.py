# coding:utf-8

import requests
import time
import threading

class getcount(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.url = 'http://wenshu.court.gov.cn/List/TreeContent'

    def url_list(self, url, data):
        req = requests.post(url=url, data=data)
        html = req.text[1:-1].replace('\\', '')
        if len(html) < 100:
            print html
        try:
            l = list(eval(html))
            return list(eval(html))
        except:
            return [[{"Value":0},],]

    def url_total(self, url, data):
        l = self.url_list(url, data)
        return l[0]["Value"]

    # def run(self):
    #     print self.url_total(self.url, {"Param": "上传日期:2012-07-01 TO 2016-07-01"})

    def run(self):
        while True:
            data = globallist.pop()
            count = self.url_total(url, data)
            global total
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
        if not format_birth == '2013-06-01':
            birth_secds -= 86400
            globallist.append({"Param":"上传日期:" + time.strftime("%Y-%m-%d",time.localtime(birth_secds)) + " TO " + format_birth})
        else:
            break
    print len(globallist)
    for thread in range(0, 10):
        t = getcount()
        t.start()

    # mm = getcount()
    # mm.start()
