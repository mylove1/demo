# coding:utf-8
import requests
import threading
import re
import time
import json

class Xizhi(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def gethtml(self, url):
        while 1:
            try:
                r = requests.get(url)
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
        requests.post('http://' + MASTERIP + ':12445/postinfo', data=mess)
        print '--------------------------------------->>>'

    def ttry(self, li, ind, defa):
        try:
            return li[ind]
        except:
            return defa

    def baseinfo(self, html):
        html = ''.join(html.split())
        base = {}
        # 所在地区
        re_father = re.compile(
            u"""<divclass="crumbs">.*?首页.*?>全国</a>.*?<ahref="http://company.xizhi.com/.*?>(.*?)</a>.*?<ahref="http://company.xizhi.com/.*?>(.*?)</a>.*?</span>(.*?)</div><divclass="containerclearfix">""")
        father = re_father.findall(html)[0]
        base["sheng"] = self.ttry(father, 0, '')
        base["shi"] = self.ttry(father, 1, '')

        # 获取企业名称
        try:
            base["name"] = father[2]
        except:
            re_name = re.compile(u"<title>(.*?)-悉知</title>")
            name = re_name.findall(html)[0]
            base["name"] = self.ttry(name, 0, '')

        re_list = [
            # 统一社会信用代码
            ["xinyongid", u"""class="lab">统一社会信用代码：</span></td><tdwidth="270px"><spanclass="">(.*?)</span>""", ''],
            ["zhucehao", u"""class="lab">注册号：</span></td><tdwidth="230px"><spanclass="">(.*?)</span>""", ''],
            ["zuzhijigouid", u"""class="line1">组织机构代码：</td><tdclass="line2"colspan="3">(.*?)</td>""", ''],
            ["type", u"""class="line1">公司类型：</td><tdclass="line2">(.*?)</td>""", ''],
            ["status", u"""class="line3">经营状态：</td><tdclass="line4">(.*?)</td>""", '存续'],
            ["faren", u"""class="line1">法定代表人：</td><tdclass="line2">(.*?)</td>""", ''],
            ["jingyingriqi", u"""class="line3">经营日期：</td><tdclass="line4">(.*?)</td>""", ''],
            ["zhuceziben", u"""class="line1">注册资本：</td><tdclass="line2">(.*?)</td>""", ''],
            ["yingyeqixian", u"""class="line3">营业期限：</td><tdclass="line4">(.*?)</td></tr>""", ''],
            ["fazhaoriqi", u"""class="line1">发照日期：</td><tdclass="line2">(.*?)</td>""", ''],
            ["wangzhi", u"""class="line3">网<spanclass="letter-space"></span>址：</td><tdclass="line4">(.*?)</td>""", ''],
            ["dengjijiguan", u"""class="line1">登记机关：</td><tdclass="line2"colspan="3">(.*?)</td>""", ''],
            ["qiyedizhi", u"""class="line1">企业地址：</td><tdclass="line2"colspan="3">(.*?)</td>""", ''],
            ["fanwei", u"""class="line1">经营范围：</td><tdclass="line2"colspan="3">(.*?)</td>""", ''],
        ]
        for xy in re_list:
            re_xy = re.compile(xy[1])
            base[xy[0]] = self.ttry(re_xy.findall(html), 0, xy[2])

        re_list_list = [
            ["gudong",
             u"""<h3><span></span>股东信息</h3>(.*?)<h3><span></span>主要成员</h3>""",
             u"""(?:<tr><td><a.*?>(.*?)</a></td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>)|(?:<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>)""",
             ["gudongname", "gudongtype", "renjiaochuzi", "shijiaochuzi"],
             ''
             ],
            ["member",
             u"""<h3><span></span>主要成员</h3>(.*?)<h3><span></span>分支机构</h3>""",
             u"""<li><spanclass="lab">(.*?)：</span><spanclass="lab-in">(.*?)</span></li>""",
             ["position", "name"],
             ''
             ],
        ]
        for xy in re_list_list:
            base[xy[0]] = []
            this_html = re.findall(xy[1], html)[0]
            for xx in re.findall(xy[2], this_html):
                this_info = {}
                for enu, yy in enumerate(xy[3]):
                    if xx[0]:
                        this_info[yy] = self.ttry(xx, enu, xy[4])
                    else:
                        suo = len(xx) - len(xy[3])
                        this_info[yy] = self.ttry(xx, suo + enu, xy[4])
                base[xy[0]].append(this_info)

        base["fenzhi"] = []
        this_html = re.findall(u"""<h3><span></span>分支机构</h3>(.*?)<divid="details-loading">loading</div>""",
                               html)
        for x in re.findall(u"""<ahref="http://company.xizhi.com/GS.*?blank">(.*?)</a></span>""", ''.join(this_html)):
            base["fenzhi"].append(x)
        return base



    def haveurl(self, url):
        mess = {"url": url}
        html = self.gethtml(url)
        mess["baseinfo"] = self.baseinfo(html)

        # 获取标签
        re_tag = re.compile('class="nav-count">(.*?)</span></a>')
        try:
            taglist = re_tag.findall(html)
        except:
            taglist = [0, 0, 0, 0]

        # # taglist[0] 风险信息数目
        mess["risk"] = int(taglist[0])
        # if int(taglist[0]):
        #     pass
        # # taglist[1] 知识产权数目
        mess["rights"] = int(taglist[1])
        # if int(taglist[1]):
        #     pass
        # # taglist[2] 对外投资数目
        mess["invest"] = int(taglist[2])
        # if int(taglist[2]):
        #     pass
        # # taglist[3] 企业年报数目
        mess["report"] = int(taglist[3])
        # if int(taglist[3]):
        #     pass
        mess["name"] = mess["baseinfo"]["name"]
        print mess
        print str(mess)
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
            kw = "http://company.xizhi.com/GS5707b23f1f98cc257c8b4892/"
            # kw = "平顶山市科远"
            try:
                print kw
            except:
                pass
            if kw == 'xxx': time.sleep(10)
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