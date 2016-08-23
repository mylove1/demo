# coding:utf-8
import requests
import threading
import re
import json

class Xizhi(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': '_GCWGuid=7E250C80-BF9A-083C-5C3C-2656AA2B020E; gr_user_id=64a24efc-0103-4082-b1a6-f849a62dbf40; _auth=rcKhA4FVjJjEE5jIKttZmczp43e5Op04QRgj8eA5ramd%2FLT7wGTlOc7GA4EP3xJFyunLWyTsb%2BI9%2FYaBDT6xNt6RneSnYg1Ci%2B5Z%2F3NCjI%2FyjcwizqzQS29HFlnzsM9g; Hm_lvt_bf959def12cb728de8b9fca745e166a7=1470190130,1471404445,1471410433,1471933088; Hm_lpvt_bf959def12cb728de8b9fca745e166a7=1471933408; AJSTAT_ok_pages=7; AJSTAT_ok_times=15; a7123_pages=6; a7123_times=12',
            'Host': 'company.xizhi.com',
            'Referer': 'http://company.xizhi.com/GS570826931f98cc273d8b495b/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            }

    def gethtml(self, url, headers={}):
        while 1:
            try:
                r = requests.get(url, headers=headers)
            except:
                print '_'
                pass
            r.encoding = 'utf-8'
            html = r.text
            if u"悉知" not in html:
                print 'error page'
                continue
            break
        self.posturl(html)
        return html

    def posturl(self, html):
        rea = re.compile('(http://company\.xizhi\.com/GS.*?/)')
        namelist = rea.findall(html)
        namelist = list(set(namelist))
        print namelist
        self.put_url({"comp": str(namelist)})

    def put_url(self, mess):
        requests.post('http://' + MASTERIP + ':12445/post/compurl', data=mess)
        print '--------------------------------------->>>'


    def put_mess(self, mess):
        requests.post('http://' + MASTERIP + ':12445/post/', data=mess)
        print '--------------------------------------->>>'



    def haveurl(self, url):
        mess = {"url": url}
        html = self.gethtml(url)
        self.put_mess({"comp": str(mess)})




    def get_kw(self):
        r = requests.get('http://' + MASTERIP +':12445/comp')
        return r.text

    def resolve(self, dic):
        if dic:
            for j in dic:
                self.put_mess(j)
        else:
            print 'o'

    def run(self):
        while 1:
            # 加 try
            # kw = self.get_kw()
            kw = "平顶山市科远"
            try:
                print kw
            except:
                pass
            if kw == 'xxx': break
            if kw[:4] == 'http':
                self.haveurl(kw)
            else:
                self.gethtml('http://www.xizhi.com/search?wd=' + kw)
            break


if __name__ == '__main__':
    MASTERIP = '192.168.0.50'
    for thread in range(1):
        a = Xizhi()
        a.start()