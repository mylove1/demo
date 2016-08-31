# coding:utf-8
import requests
import re

def posthtml(page):
    url = 'https://s.nacao.org.cn/servlet/valication'
    data = {
               'firststrfind': "jgmc='%e5%b9%b3%e9%a1%b6%e5%b1%b1%e5%b8%82%e7%a7%91%e8%bf%9c%e7%bd%91%e7%bb%9c%e6%8a%80%e6%9c%af%e6%9c%89%e9%99%90%e5%85%ac%e5%8f%b8'",
           'strfind': "jgmc='%e5%b9%b3%e9%a1%b6%e5%b1%b1%e5%b8%82%e7%a7%91%e8%bf%9c%e7%bd%91%e7%bb%9c%e6%8a%80%e6%9c%af%e6%9c%89%e9%99%90%e5%85%ac%e5%8f%b8'",
    'key': '%E5%B9%B3%E9%A1%B6%E5%B1%B1%E5%B8%82%E7%A7%91%E8%BF%9C%E7%BD%91%E7%BB%9C%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8',
           'kind': '2',
                   'tit1': '%E5%B9%B3%E9%A1%B6%E5%B1%B1%E5%B8%82%E7%A7%91%E8%BF%9C%E7%BD%91%E7%BB%9C%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8',
                           'selecttags': '%E5%85%A8%E5%9B%BD',
                                         'xzqhName': 'alll',
                                                     'button': '',
                                                               'jgdm': 'false',
                                                                       'jgmc': 'true',
        'jgdz': 'false',
        "Cookie": "cn_1d16f4376ad67oc14c23_dplus=%7B%22distinct_id%22%3A%20%22155b4f60197393-06939690c1bdd-414a0229-1fa400-155b4f6019c740%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201467625277%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201467625277%7D; cn_1259810332_dplus=%7B%22distinct_id%22%3A%20%22156591cadd24b1-02b34ebc143fad-414a0229-1fa400-156591cadd36e2%22%2C%22%24_sessionid%22%3A%201%2C%22%24_sessionTime%22%3A%201472008648%2C%22initial_view_time%22%3A%20%221470371381%22%2C%22initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com.hk%2F%22%2C%22initial_referrer_domain%22%3A%20%22www.google.com.hk%22%2C%22%24recent_outside_referrer%22%3A%20%22www.google.com.hk%22%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201472008648%7D; Hm_lvt_a17f93a4ef326580ad360f8b1419c389=1470373867,1472008440,1472008446,1472008622; __utma=108799005.1144303923.1466054733.1470373867.1472008440.5; __utmz=108799005.1472008440.5.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); JSESSIONID=306C184581F154FE88158519D79059E4; banggoo.nuva.cookie=3|V8Tbq|V8TZm",
                                                                                       'zch': 'false',
                                                                                              'strJgmc': '',
                                                                                                         '': '',
                                                                                                             'secondSelectFlag': '',
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '1033',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'cn_1d16f4376ad67oc14c23_dplus=%7B%22distinct_id%22%3A%20%22155b4f60197393-06939690c1bdd-414a0229-1fa400-155b4f6019c740%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201467625277%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201467625277%7D; cn_1259810332_dplus=%7B%22distinct_id%22%3A%20%22156591cadd24b1-02b34ebc143fad-414a0229-1fa400-156591cadd36e2%22%2C%22%24_sessionid%22%3A%201%2C%22%24_sessionTime%22%3A%201472008648%2C%22initial_view_time%22%3A%20%221470371381%22%2C%22initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com.hk%2F%22%2C%22initial_referrer_domain%22%3A%20%22www.google.com.hk%22%2C%22%24recent_outside_referrer%22%3A%20%22www.google.com.hk%22%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201472008648%7D; Hm_lvt_a17f93a4ef326580ad360f8b1419c389=1470373867,1472008440,1472008446,1472008622; __utma=108799005.1144303923.1466054733.1470373867.1472008440.5; __utmz=108799005.1472008440.5.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); JSESSIONID=306C184581F154FE88158519D79059E4; banggoo.nuva.cookie=3|V8Tbq|V8TZm',
        'Host': 's.nacao.org.cn',
        'Origin': 'https://s.nacao.org.cn',
        'Referer': 'https://s.nacao.org.cn/specialResult.html?x=7jITUT47YZXinqcMx6xgsEL2Gfs=&k=xhgT/9Ns6hkNseTK8CDc0Lg=&s=601hD8so4Z/f6dKCq/z7rip4h0snfEId4nyHsWdPI5M2j8btJaMJFdajh6zbpFSWRsVC4NXFx+FsRpvgL90RdYk=&y=RxPFbWMI9HYSZ1R3hwcNTEaiYq6RCtaGoI1D62l1poxj7o+J7xcVF0ZydNOJl2ZWPZzjyfDq1tIyUA==',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',

    }
    while 1:
        try:
            return requests.post(url, data=data, headers=headers)
        except:
            continue
for x in range(1, 2):#76367):
    r = posthtml(x)
    print r.status_code
    print r.text
    # for y in re.findall('href="(http://wsgs\.fjaic\.gov\.cn/creditpub/notice/view.*?)" target="_blank">(.*?)</a>', html):
    #     print y