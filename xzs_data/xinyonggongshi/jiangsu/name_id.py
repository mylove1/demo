#!/usr/bin/env python
# coding:utf-8

'''

'''

import re
import requests
from jiangsu_validatecode import jiangsu_vali


def html_id_list(text):
    """
    对查询页面进行解析
    :param text:
    :return: list，包含企业名称
    """
    rea = re.compile("""gsRelease\.jsp','(.*?)','(.*?)','(.*?)','.*?','.*?','ecippla.*?>(.*?)<""")
    text = ''.join(text.split())
    l = []
    for jilu in rea.findall(text):
        l.append({"name": jilu[3],  # 企业名称
                  "jsid": jilu[1],    # 内部ID
                  "org": jilu[0],   # 内部ID
                  "seqid": jilu[2]  # 内部ID
                  })
    return l


def name_idlist(name):
    """"
    江苏在搜索的时候验证码随便输入几个字母就可以了，不需要识别
    对传入的企业名称进行查询，返回一个列表，包含企业名称，信用代码，regid
    返回的结果可能为空，也可能有几个
    :param name:
    :return:
    """
    while 1:
        # url = ('http://www.jsgsj.gov.cn:58888/province/rand_img.jsp?'
        #        'type=7&temp=Wed%20Oct%2019%202016%2010:31:03%20GMT+0800%20'
        #         '(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)')
        # s = requests.Session()
        # r = s.get(url)
        # code = jiangsu_vali(r.content, show=True, model_file=False)
        code = 'sdfff'
        data = {"name": name,
                "verifyCode": code,
                }
        r = requests.post(url='http://www.jsgsj.gov.cn:58888/province/infoQueryServlet.json?queryCinfo=true', data=data)
        print r.text
        # if u"验证码不正确" in r.text:
        #     continue
        # print r.status_code
        return html_id_list(r.text)

if __name__ == '__main__':
    name = u"江苏新东南电缆有限公司"
    print name_idlist(name)
