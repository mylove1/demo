# coding:utf-8
import requests
import threading
import re
import time
import urlparse

class YouBoy(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.relist = [
        ["name", re.compile(u'style="width:30%;">公司名称：</th><tdstyle="width:70%;">(.*?)</td></tr>')],
        ["zhucehao", re.compile(u'class="bgcolor"><th>注册号：</th><td>(.*?)</td></tr>')],
        ["dizhi", re.compile(u'<th>住所：</th><td>(.*?)</td></tr>')],
        ["faren", re.compile(u'class="bgcolor"><th>法定代表人：</th><td>(.*?)</td></tr>')],
        ["zhuceziben", re.compile(u'<tr><th>注册资本：</th><td>(.*?)</td></tr>')],
        ["type", re.compile(u'<tr><th>公司类型：</th><td>(.*?)</td></tr>')],
        ["status", re.compile(u'class="bgcolor"><th>企业状态：</th><td>(.*?)</td></tr>')],
        ["yingyeqixianzi", re.compile(u'<tr><th>营业期限自：</th><td>(.*?)</td></tr>')],
        ["yingyeqixianzhi", re.compile(u'class="bgcolor"><th>营业期限至：</th><td>(.*?)</td></tr>')],
        ["chengliriqi", re.compile(u'<tr><th>成立日期：</th><td>(.*?)</td></tr>')],
        ["dengjijiguan", re.compile(u'class="bgcolor"><th>登记机关：</th><td>(.*?)</td></tr>')],
        ["jigoudaima", re.compile(u'<tr><th>组织机构代码：</th><td>(.*?)</td></tr>')],
        ["status", re.compile(u'class="bgcolor"><th>企业状态：</th><td>(.*?)</td></tr>')],
        ["status", re.compile(u'class="bgcolor"><th>企业状态：</th><td>(.*?)</td></tr>')],
        ["status", re.compile(u'class="bgcolor"><th>企业状态：</th><td>(.*?)</td></tr>')],
        ]

    def gethtml(self, url):
        while 1:
            try:
                proxy = proxypool.pop(0)
            except:
                proxypool.extend(requests.get("http://" + MASTERIP +":8384/ip/100").text.split())
                continue
            try:
                r = requests.get(url, proxy=proxy)
            except:
                print '_'
                pass
            html = r.text
            break
        self.posturl(html, url)
        if "details" in url:
            self.postjpg(html)
        return 'ok'

    def posturl(self, html, url):
        rea = re.compile('href="(/details/.*?)"')
        namelist = rea.findall(html)
        namelist = list(set(namelist))
        for x in range(len(namelist)):
            namelist[x] = urlparse.urljoin(url, namelist[x])
            print namelist[x]
        self.put_url({"comp": str(namelist)})

        rea = re.compile('href="(http://.*?36bj\.com.*?)"')
        namelist = rea.findall(html)
        namelist = list(set(namelist))
        for x in namelist:
            print x
        self.put_url({"comp": str(namelist)})

    def postjpg(self, html):
        info = {}
        html = ''.join(html.split())

        for x in self.relist:
            try:
                info[x[0]] = x[1].findall(html)[0]
            except:
                info[x[0]] = ''
        for x in info.keys():
            print info[x]
        # rea = re.compile('(http://pic.meizitu.com/.*?jpg)')
        # namelist = rea.findall(html)
        # namelist = list(set(namelist))
        if info["name"] != '':
            self.put_jpg({"comp": str(info)})

    def put_url(self, mess):
        requests.post('http://' + MASTERIP + ':31112/post/url', data=mess)
        print '------------>>>'


    def put_jpg(self, mess):
        requests.post('http://' + MASTERIP + ':31112/post/jpg', data=mess)
        print '------------------------>>>'

    def get_kw(self):
        return requests.get('http://' + MASTERIP + ':31112/comp').text


    def run(self):
        while 1:
            try:
                # 加 try
                kw = self.get_kw()
                if kw == '0':
                    print 'no kw'
                    time.sleep(5)
                    continue
                try:
                    print kw
                except:
                    pass

                self.gethtml(kw)

            except:
                pass



if __name__ == '__main__':
    proxypool = []
    MASTERIP = '192.168.0.50'
    for thread in range(1):
        a = YouBoy()
        a.start()
