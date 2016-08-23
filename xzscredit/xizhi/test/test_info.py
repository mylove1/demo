# coding:utf-8
import requests
import re





def gethtml(url):
    headers = {
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
    return html


def baseinfo(html):
    base = {}

    return base


def haveurl(url):
    mess = {"url": url}
    html = gethtml(url)
    mess["baseinfo"] = baseinfo(html)
    re_tag = re.compile('class="nav-count">(.*?)</span></a>')
    try:
        taglist = re_tag.findall(html)
    except:
        taglist = [0, 0, 0, 0]

    # taglist[0] 风险信息数目
    if int(taglist[0]):
        pass
    # taglist[1] 知识产权数目
    if int(taglist[1]):
        pass
    # taglist[2] 对外投资数目
    if int(taglist[2]):
        pass
    # taglist[3] 企业年报数目
    if int(taglist[3]):
        pass
    print taglist
    print html
    return mess

if __name__ == '__main__':
    # 科远，基本，风险
    # url = 'http://company.xizhi.com/GS5707e9c31f98cc98108b46f9/'
    # 铁道，基本，风险
    # url = 'http://company.xizhi.com/GS57082d041f98cc224e8b46cd/'
    # 阿里，风险，对外投资，年报
    url = 'http://company.xizhi.com/GS570826931f98cc273d8b495b/'
    print haveurl(url)