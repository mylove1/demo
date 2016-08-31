# coding:utf-8
'''
福建省信用信息公示系统
企业详情页面解析
'''
import requests
import re
import time
class HeNanAnalyze():
    def __init__(self, id):
        self.id = id
        self.url = 'http://222.143.24.157/businessPublicity.jspx?id=' + id + '&sourceType=1'
        self.qiyegongshiurl = 'http://222.143.24.157/enterprisePublicity.jspx?id=' + id
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Host': '222.143.24.157',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        }

    def delcss(self, html):
        li = {
            "<a.*?>": "<a>",
            "<li.*?>": "<li>",
            "<tr.*?>": "<tr>",
            "<td.*?>": "<td>",
            "<th.*?>": "<th>",
            "<col.*?>": "<col>",
            "<table.*?>": "<table>",
            "<div.*?>": "<div>",
            "<!--.*?-->": "",
            u"主要人员信息</th></tr>": u"主要人员信息</th><tr>"

        }
        for x in li.keys():
            re_this = re.compile(x)
            html = re_this.sub(li[x], html)
        return html

    def dealwith(self, li, html):
        for x in li:
            html = html.replace(x, '')
        return html

    def gethtml(self, url):
        while 1:
            try:
                return requests.get(url).text
            except:
                continue

    def pair(self, html):
        return re.findall('<th>(.*?)</th><td>(.*?)</td>', html)

    def chapter(self, re_this, html):
        return ''.join(re.findall(re_this, html))

    def table(self, html):
        # print html

        table = []
        '''
        页面中有两种表，这是第二种的解析
        这种表结构：（第一行不让它在html中）
        	<tr><th colspan="4">分支机构信息</th></tr>
            <tr>
              <th>序号</th>
              <th>注册号/统一社会信用代码</th>
              <th>名称</th>
              <th>登记机关</th>
            </tr>

            <tr class="page-item">
                <td class="center">1</td>
                <td>350000100009208</td>
                <td>福建省能源服务有限公司南平分公司</td>
                <td>福建省南平市工商行政管理局</td>
            </tr>

            <tr class="page-item">
                <td class="center">2</td>
                <td>350000100009208</td>
                <td>福建省能源服务有限公司宁德分公司</td>
                <td>福建省宁德市工商行政管理局</td>
            </tr>

            <tr class="page-item">
                <td class="center">3</td>
                <td>350000100009208</td>
                <td>福建省能源服务有限公司龙岩分公司</td>
                <td>福建省龙岩市工商行政管理局</td>
            </tr>

            <tr class="page-item">
                <td class="center">4</td>
                <td>350000100009208</td>
                <td>福建省能源服务有限公司莆田分公司</td>
                <td>福建省莆田市工商行政管理局</td>
            </tr>

            <tr class="page-item">
                <td class="center">5</td>
                <td>350000100009208</td>
                <td>福建省能源服务有限公司福州分公司</td>
                <td>福州市市场监督管理局</td>
            </tr>

            <tr class="page-item">
                <td class="center">6</td>
                <td>350000100009208</td>
                <td>福建省能源服务有限公司漳州分公司</td>
                <td>福建省漳州市工商行政管理局</td>
            </tr>

            <tr class="page-item">
                <td class="center">7</td>
                <td>350000100009208</td>
                <td>福建省能源服务有限公司三明分公司</td>
                <td>福建省三明市工商行政管理局</td>
            </tr>

            <tr class="page-item">
                <td class="center">8</td>
                <td>350000100009208</td>
                <td>福建省能源服务有限公司厦门分公司</td>
                <td>厦门市市场监督管理局</td>
            </tr>

            <tr class="page-item">
                <td class="center">9</td>
                <td>350000100009208</td>
                <td>福建省能源服务有限公司泉州分公司</td>
                <td></td>
            </tr>

        :return:[{}, {}, {}]
        '''
        # 表头
        html_head = ''.join(re.findall('<tr>((?:<th>.*?</th>)+)</tr>', html))
        head_list = re.findall('<th>(.*?)</th>', html_head)
        # 表身
        body_list = re.findall('<tr>((?:<td>.*?</td>)+)</tr>', html)
        for enu, x in enumerate(body_list):
            body_list[enu] = re.findall('<td>(.*?)</td>', x)

        # 获取表格的列数
        lenth = len(head_list)

        for x in body_list:
            this_dict = {}
            for enu in range(lenth):
                key = head_list[enu]
                value = x[enu]
                if key in this_dict.keys():
                    table.append(this_dict)
                    this_dict = {}
                this_dict[key] = value
            if ''.join(this_dict.values()) == '':
                continue
            else:
                table.append(this_dict)

        return table

    def print_dict(self, this_dict):
        for x in this_dict.keys():
            if isinstance(this_dict[x], list):
                print x, '：', self.print_list(this_dict[x])
            elif isinstance(this_dict[x], dict):
                print x, '：', self.print_dict(this_dict[x])
            else:
                print x, '：', this_dict[x]

    def print_list(self, this_list):
        for x in this_list:
            if isinstance(x, list):
                self.print_list(x)
            elif isinstance(x, dict):
                self.print_dict(x)
            else:
                print x

    def baseinfo(self, this_re, html):
        # 获取页面中的基本信息键值对
        baseinfo = {}
        for x in self.pair(self.chapter(this_re, html)):
            # 测试打印
            # print '---------', x[0], x[1]

            baseinfo[x[0]] = x[1]
        return baseinfo

    def tableinfo(self, dic, table_dict, html):
        # 对table_dict进行处理，以键为compinfo的键插入compinfo
        for x in table_dict.keys():
            dic[x] = self.table(self.chapter(table_dict[x], html))
            # print '1'
            # 测试打印
            # self.print_table(compinfo[x])

        return dic

    def annual(self, nianbao_list):
        nianbao = {}
        for this_year_list in nianbao_list:
            this_year = this_year_list[1]
            this_html = self.delcss(self.gethtml(url = 'http://222.143.24.157' + this_year_list[0]))
            this_html = ''.join(this_html.split())
            nianbao[this_year] = {}

            table_dict = {
                u"网站或网店信息": u'网站或网店信息</th></tr>(.*?)</th></tr></table>',
                u"股东及出资信息": u'股东及出资信息(.*?)</th></tr></table>',
                u"对外投资": u'对外投资信息</th></tr>(.*?)</th></tr></table>',
                # u"对外提供保证担保信息": u'对外提供保证担保信息</th></tr>(.*?)</th></tr></table>',
                u"股权变更信息": u'股权变更信息</th></tr>(.*?)</th></tr></table>',
                u"修改记录": u'修改记录</th></tr>(.*?)</th></tr></table>',
            }

            # 加入各种表里的信息
            a = {}
            a = self.tableinfo(a, table_dict, this_html)
            nianbao[this_year] = a
            # 加入企业基本信息

            nianbao[this_year][u"基本信息"] = self.baseinfo(u'企业基本信息</th></tr>(.*?)table', this_html)
            nianbao[this_year][u"企业资产状况信息"] = self.baseinfo(u'企业资产状况信息</th></tr>(.*?)table', this_html)
        return nianbao

    def run(self):
        # 初始化公司信息为字典
        compinfo = {}
        html = self.gethtml(self.url)
        html = ''.join(html.split())
        html = self.delcss(html)

        html = self.dealwith(['<br>', '<br/>'], html)

        # 获取页面中的基本信息键值对
        # for x in self.pair(self.chapter(u'<th>基本信息</th>(.*?)table', html)):
        #     # if '<' in x[0] or '>' in x[0]: continue
        #     print x[0], x[1]
        compinfo[u"基本信息"] = self.baseinfo(u'基本信息</th>(.*?)table', html)
        compinfo[u"清算信息"] = self.baseinfo(u'清算信息</th>(.*?)table', html)

        # 获取页面中的表信息，
        # table_dict字典中键为信息的键，值为获取这部分信息的正则


        # # 二：企业公示信息
        if u"个体工商户公示信息" not in html:
            table_dict = {
                u"高管信息": u'主要人员信息</th>(.*?)</th></table>',  #
                u"股东信息": u'股东信息</th>(.*?)</th></table>',  #
                u"对外投资": u'分支机构信息</th>(.*?)</th></table>',
                u"变更信息": u'变更信息</th>(.*?)</table></div><div>',  #
                u"经营异常": u'经营异常信息</th>(.*?)</table></div></div>',  #
                u"行政处罚": u'行政处罚信息</th>(.*?)</table></div></div>',
                u"动产抵押": u'动产抵押登记信息</th>(.*?)</table></div></div>',
                u"股权出质": u'股权出质登记信息</th>(.*?)</table></div></div>',
                u"严重违法": u'严重违法信息</th>(.*?)</table></div></div>'
            }
            compinfo = self.tableinfo(compinfo, table_dict, html)


            html_qiyegongshi = ''.join(self.gethtml(self.qiyegongshiurl).split())
            nianbao_list = re.findall(u'href="(/QueryYearExamineDetail\.jspx.*?)"target="_blank">(.*?)年度报告', html_qiyegongshi)
            #
            # # 企业年报信息
            compinfo[u"企业年报"] = self.annual(nianbao_list)
        else:
            table_dict = {
                u"高管信息": u'参加经营的家庭成员姓名</th>(.*?)</table></div><div>',  #
                u"变更信息": u'变更信息</th>(.*?)</table></div><div>',  #
                u"经营异常": u'经营异常信息</th>(.*?)</th></table><table>',  #
                u"行政处罚": u'行政处罚信息</th>(.*?)</table></div></div>',
                u"动产抵押": u'动产抵押登记信息</th>(.*?)</table></div></div>',
            }
            compinfo = self.tableinfo(compinfo, table_dict, html)
        return compinfo

        # print compinfo
        # self.print_dict(compinfo)

        # 对结果打印显示
        # j = json.dumps(compinfo, indent=4)
        # print j



        # 对table_dict进行处理，以键为compinfo的键插入compinfo
        # for x in table_dict.keys():
        #     compinfo[x] = self.table(self.chapter(table_dict[x], html))
        #     # 测试打印
        #     self.print_table(compinfo[x])
        # print '\n'.join(compinfo.keys())

        # # 1：主要人员信息：[]
        # zhuyaorenyuan = self.table(self.chapter(u'主要人员信息</th>(.*?)</th></tr></table>', html))
        # self.print_table(zhuyaorenyuan)
        # # 2：分支机构：[]
        # fenzhijigou = self.table(self.chapter(u'分支机构信息(.*?)</th></tr></table>', html))
        # self.print_table(fenzhijigou)
        #
        # # 3：股东信息
        # gudongxinxi = self.table(self.chapter(u'股东信息<br/>(.*?)</th></tr></table>', html))
        # self.print_table(gudongxinxi)
        #
        # # 4：变更信息
        # biangengxinxi = self.table(self.chapter(u'变更信息</th>(.*?)</th></tr></table>', html))
        # self.print_table(biangengxinxi)
    def info(self):
        return self.run()


if __name__ == '__main__':
    # url = 'http://wsgs.fjaic.gov.cn/creditpub/notice/view?uuid=25z1mCH6cgjbR.NOXANO.w.i33STy5xX&tab=01'
    url = 'http://wsgs.fjaic.gov.cn/creditpub/notice/view?uuid=np2zjUZkeytc8wbZIiCjNzgSjSF60hHp&tab=01'
    url = 'http://wsgs.fjaic.gov.cn/creditpub/notice/view?uuid=25z1mCH6cgjbR.NOXANO.w.i33STy5xX&tab=01'
    id = '33D1559F7E785FA4E053050A080AED3E'
    id = '3B4232F6F5B7DF07E053050A080AA31E'
    a = HeNanAnalyze(id)
    print a.info()