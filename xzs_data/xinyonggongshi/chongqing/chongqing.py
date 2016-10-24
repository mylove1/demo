#coding:utf-8
from __init__ import Analyze
import json
from pprint import pprint
import re
import requests
from chongqing_validatecode import chongqing_vali


class ChongQingAnalyze(Analyze):
    def __init__(self, name=None, entid=None, regid=None, type=None, model=None):
        self.model = model
        self.gongshang_info = ""
        self.typelist = [1, 16, 7, 2, 17, 18, 19, 20,
                         21, 22, 3, 4, 5, 6, 8, 9, 10,
                         11, 12, 13, 14, 15]
        # self.typelist = self.typelist.extend([x for x in range(1, 20)])
        self.info = self.data()
        if entid and regid:
            self.name = name
            self.entid = entid
            self.regid = regid
        else:
            self.name = name
            l = self.name_idlist(self.name)[0]
            self.entid = l["entid"]
            self.regid = l["id"]
        self.headers = {
            "Referer": "http://gsxt.cqgs.gov.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }

        self.type = type if type else self.get_type()

    def get_html(self, link):
        r = requests.get(url=link, headers=self.headers)
        return r.text

    def get_dict(self, link=None, text=None):
        while 1:
            if link:
                text = self.get_html(link)
            try:
                if text[:11] == '{"code":-1}':
                    return {}
                return json.loads(text[6:])
            except:
                print text
                continue

    def get_type(self):
        for x in self.typelist:
            this_link = "http://gsxt.cqgs.gov.cn/search_getEnt.action?entId=%s&stype=SAIC&type=%s" % (self.entid, x)
            text = self.get_html(this_link)
            if len(text) > 10:
                self.gongshang_info = self.get_dict(text=text)
                return x
        print u"找不出这种类型的企业", self.entid, self.regid

    def html_id_list(self, text):
        """
        对查询页面进行解析
        :param text:
        :return: list，包含企业名称，社会信用代码以及重庆特有的regid的列表
        """
        rea = re.compile("""class='name'target="_self"data-id="(.*?)"data-type="\d{4}"data-entId="(.*?)">(.*?)</a>""")
        text = ''.join(text.split())
        l = []
        for jilu in rea.findall(text):
            l.append({"name": jilu[2],
                      "entid": jilu[1],
                      "id": jilu[0]
                      })
        return l

    def name_idlist(self, name):
        """"
        对传入的企业名称进行查询，返回一个列表，包含企业名称，信用代码，regid
        返回的结果可能为空，也可能有几个
        :param name:
        :return:
        """
        while 1:
            url = 'http://gsxt.cqgs.gov.cn/sc.action?width=130&height=40&fs=23'
            s = requests.Session()
            r = s.get(url)
            code = chongqing_vali(r.content, self.model, show=False)
            data = {"key": name, "code": code}
            r = s.post(url='http://gsxt.cqgs.gov.cn/search.action', data=data)
            # print r.text
            if u"验证码不正确" in r.text:
                continue
            # print r.status_code
            return self.html_id_list(r.text)

    def get_gongshang_info(self):
        # 工商公示信息
        if not self.gongshang_info:
            gongshang_url = "http://gsxt.cqgs.gov.cn/search_getEnt.action?entId=%s&stype=SAIC&type=%s" % (self.entid, self.type)
            self.gongshang_info = self.get_dict(gongshang_url)
        return self.gongshang_info

    def get_nianbao_info(self):
        nianbao_info = []
        report_year_list = [2015, 2014, 2013]
        for year in report_year_list:
            this_url = "http://gsxt.cqgs.gov.cn/search_getYearReportDetail.action?id=%s&type=%s&year=%s" %(self.regid, self.type, year)
            text = self.get_html(this_url)
            if len(text) > 20:
                report = json.loads(text)
                if report == {}:
                    continue
                report["year"] = year
                nianbao_info.append(report)
        return nianbao_info

    def get_gudongchuzi_info(self):
        this_url = ("http://gsxt.cqgs.gov.cn/search_getDaily.action?"
                    "id=%s&jtype=invsub") % (self.regid)
        gudongchuzi_info = self.get_dict(this_url)
        return gudongchuzi_info

    def get_guquanbiangeng_info(self):
        this_url = ("http://gsxt.cqgs.gov.cn/search_getDaily.action?"
                   "id=%s&jtype=transinfo") % (self.regid)
        guquanbiangeng_info = self.get_dict(this_url)
        return guquanbiangeng_info

    def get_xingzhengxuke_info(self):
        this_url = ("http://gsxt.cqgs.gov.cn/search_getDaily.action?"
                    "id=%s&jtype=licinfo") % (self.regid)
        xingzhengxuke_info = self.get_dict(this_url)
        return xingzhengxuke_info

    def get_zhishichanquanchuzhi_info(self):
        this_url = ("http://gsxt.cqgs.gov.cn/search_getDaily.action?"
                    "id=%s&jtype=pleinfo") % (self.regid)
        zhishichanquanchuzhi_info = self.get_dict(this_url)
        return zhishichanquanchuzhi_info

    def get_xingzhengchufa_info(self):
        this_url = ("http://gsxt.cqgs.gov.cn/search_getDaily.action?"
                    "id=%s&jtype=peninfo") % (self.regid)
        xingzhengchufa_info = self.get_dict(this_url)
        return xingzhengchufa_info

    def get_gongshi_info(self):
        if self.gongshang_info:
            gongshi_info = self.gongshang_info
        else:
            gongshi_info = self.get_gongshang_info()
        gongshi_info["nianbaolist"] = self.get_nianbao_info()
        gongshi_info["gudongchuzi"] = self.get_gudongchuzi_info()
        gongshi_info["guquanbiangeng"] = self.get_guquanbiangeng_info()
        gongshi_info["xingzhengxuke"] = self.get_xingzhengxuke_info()
        gongshi_info["zhishichanquanchuzhi"] = self.get_zhishichanquanchuzhi_info()
        gongshi_info["xingzhengchufa"] = self.get_xingzhengchufa_info()
        return gongshi_info

if __name__ == '__main__':
    # entid = "5002281201412040817780"
    # regid = "500228NA907174X"
    # a = ChongQingAnalyze(entid=entid, regid=regid)
    # print a.type

    name = u"中国移动通迅花岩营业厅"
    a = ChongQingAnalyze(name=name)
    print a.entid
    print a.regid
    print a.type

