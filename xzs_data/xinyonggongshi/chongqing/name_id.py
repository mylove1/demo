#!/usr/bin/env python
# coding:utf-8

'''

'''

import re
import requests
from chongqing_validatecode import chongqing_vali


def html_id_list(text):
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


def name_idlist(name):
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
        code = chongqing_vali(r.content, "chongqing.mo", show=False)
        data = {"key": name, "code": code}
        r = s.post(url='http://gsxt.cqgs.gov.cn/search.action', data=data)
        # print r.text
        if u"验证码不正确" in r.text:
            continue
        # print r.status_code
        return html_id_list(r.text)

if __name__ == '__main__':
    name = u"中国移动"
    print name_idlist(name)
