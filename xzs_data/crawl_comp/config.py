#coding:utf-8
# 环球贸易网
import re
MASTERIP = "192.168.0.50"
LISTENPORT = 31111
use_proxy = False
bianma = 'gbk'
kwlist = ['http://www.herostart.com/',]

relist = [
    # [
    #     ["tel", re.compile(u">电话：(.*?)</li>")],
    #     ["phone", re.compile(u'>手机：(.*?)</li>')],
    #     ["name", re.compile(u'公司名称：</td><td>(.*?)</td></tr>')],
    #     ["di", re.compile(u'所在地：</td><td><Ahref=.*?黄页">(.*?)</A>')],
    #     ["person", re.compile(u'<li>联系人：(.*?)</li>')],
    #     ["chuanzhen", re.compile(u'>传真：(.*?)</li>')],
    #     ["email", re.compile(u'>邮件：(.*?)</li>')],
    # ],
    [],
    []

]

# 连接中有如下字符表明这是企业的详情页面
xiangqing = ["gongsi",
             "sq",
             "sell",
             ]
wuyong = [
          "buy",
          "expo",
          "info"]

def t_html(html):
    html = ''.join(html.split())
    html = html.replace("&nbsp;", '')
    return html