# coding:utf-8
import requests
import re





def gethtml(url):
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'company.xizhi.com',
        'Referer': 'http://company.xizhi.com/GS570826931f98cc273d8b495b/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    }
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
    return html

def ttry(li, ind, defa):
    try:
        return li[ind]
    except:
        return defa


def baseinfo(html):
    html = ''.join(html.split())
    base = {}
    # 所在地区
    re_father = re.compile(u"""<divclass="crumbs">.*?首页.*?>全国</a>.*?<ahref="http://company.xizhi.com/.*?>(.*?)</a>.*?<ahref="http://company.xizhi.com/.*?>(.*?)</a>.*?</span>(.*?)</div><divclass="containerclearfix">""")
    father = re_father.findall(html)[0]
    base["sheng"] = ttry(father, 0, '')
    base["shi"] = ttry(father, 1, '')

    # 获取企业名称
    re_name = re.compile(u"<title>(.*?)-悉知</title>")
    name = re_name.findall(html)
    base["name"] = ttry(name, 0, '')

    # 统一社会信用代码
    # re_xinyongid = re.compile(u"""class="lab">统一社会信用代码：</span></td><tdwidth="270px"><spanclass="">(.*?)</span>""")
    # xinyongid = re_xinyongid.findall(html)
    # base["xinyongid"] = ttry(xinyongid, 0, '')

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
        base[xy[0]] = ttry(re_xy.findall(html), 0, xy[2])

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

            print xx
            this_info = {}
            for enu, yy in enumerate(xy[3]):
                if xx[0]:
                    this_info[yy] = ttry(xx, enu, xy[4])
                else:
                    suo = len(xx) - len(xy[3])
                    this_info[yy] = ttry(xx, suo + enu, xy[4])
            base[xy[0]].append(this_info)

    base["fenzhi"] = []
    this_html = re.findall(u"""<h3><span></span>分支机构</h3>(.*?)<divid="details-loading">loading</div>""",
                           html)
    for x in re.findall(u"""<ahref="http://company.xizhi.com/GS.*?blank">(.*?)</a></span>""", ''.join(this_html)):
        base["fenzhi"].append(x)



    print '名称', base["name"]
    print '省份', base["sheng"]
    print '市', base["shi"]
    print '统一社会信用代码', base["xinyongid"]
    print '注册号', base["zhucehao"]
    print '组织机构代码', base["zuzhijigouid"]
    print '公司类型', base["type"]
    print '经营状态', base["status"]
    print '法人', base["faren"]
    print '经营日期', base["jingyingriqi"]
    print '注册资本', base["zhuceziben"]
    print '营业期限', base["yingyeqixian"]
    print '发照日期', base["fazhaoriqi"]
    print '网址', base["wangzhi"]
    print '登记机关', base["dengjijiguan"]
    print '企业地址', base["qiyedizhi"]
    print '经营范围', base["fanwei"]
    for x in base["gudong"]:
        print '股东名称', x["gudongname"]
        print '股东类型', x["gudongtype"]
        print '认缴出资', x["renjiaochuzi"]
        print '实际出资', x["shijiaochuzi"]
    for x in base["member"]:
        print x["position"]
        print x["name"]
    for x in base["fenzhi"]:
        print x


    return base


def haveurl(url):
    mess = {"url": url}
    html = gethtml(url)
    mess["baseinfo"] = baseinfo(html)

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
    print taglist
    return mess

if __name__ == '__main__':
    # 科远，基本，风险
    # url = 'http://company.xizhi.com/GS5707e9c31f98cc98108b46f9/'
    # 铁道，基本，风险
    # url = 'http://company.xizhi.com/GS57082d041f98cc224e8b46cd/'
    # 阿里，风险，对外投资，年报
    url = 'http://company.xizhi.com/GS570826931f98cc273d8b495b/'
    # zhege you 统一社会信用代码
    url = 'http://company.xizhi.com/GS5762b58d1f98cc6a0d8b45f0/'
    # 有组织机构代码
    url = 'http://company.xizhi.com/GS5707da061f98cc82678b4936/'
    url = 'http://company.xizhi.com/GS5707b23f1f98cc257c8b4892/'
    # url = 'http://company.xizhi.com/GS5707d0301f98cc544f8b48d8/'
    print haveurl(url)