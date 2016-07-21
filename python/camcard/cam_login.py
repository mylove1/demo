# coding:utf-8
import urllib2
import requests
from lxml import etree
headers = {
    'Cookie': 'JSESSID=6ddpqk4iepi7s23co1hs43p832',
    'Cookie': '_ga=GA1.2.2021239531.1467996251',
}

import Cookie
import datetime
import random

expiration = datetime.datetime.now() + datetime.timedelta(days=30)
cookie = Cookie.SimpleCookie()
cookie["session"] = random.randint(1,1000000000)
cookie["session"]["domain"] = ".baidu.com"
cookie["session"]["path"] = "/"
cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")



# import urllib2
# import cookielib
# policy = cookielib.DefaultCookiePolicy(
#     rfc2965=True, strict_ns_domain=cookielib.DefaultCookiePolicy.DomainStrict,
#     blocked_domains=["ads.net", ".ads.net"])
# cookie = cookielib.CookieJar(policy)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open('http://httpbin.org/headers')
# print response.read()













# login_url = "http://info.camcard.com/?device_id=867575026347925&code=666c6bb4842f096d448afeb3ae30ee7aa62ec37aa05a79dfb9eb635a508ef0bae4383bb7f2df54b0bfcef9260e9d21a5&from=searchList&keyword=%E4%BC%98%E5%8C%96&id=da86aaf6-61d3-4715-8184-9d2a52c09f27"
# opener = urllib2.build_opener()
# opener.addheaders.append(('Cookie','_ga=GA1.2.2021239531.1467996251','JSESSID=6ddpqk4iepi7s23co1hs43p832'))
# opener.addheaders.append(('Cookie','_cpl=zh-cn'))
# opener.addheaders.append(('Cookie','gr_user_id=d9a5bc2c-990b-4abe-a34d-95b5c2ad2d8f'))
# opener.addheaders.append(('Cookie','_cpcl=577fd85cc8c14'))
# opener.addheaders.append(('Cookie','Hm_lvt_3e5d98c3ed0582b0b85a3561dceafded=1467996251'))
# opener.addheaders.append(('Cookie','gr_session_id_a3a7339123406a03=30777f82-ee22-4f98-ba75-41a55fb2b76b'))
# f = opener.open('http://httpbin.org/headers')
# f = urllib2.urlopen(login_url, headers=headers)
# f = requests.get('http://httpbin.org/headers',headers=headers)
# print f.text




# login_url = "https://api.intsig.net/user/login2?user=13213840126&password=0b857a0d2718d517&client=Android-m2&client_id=78e5LED244KdyRD92DgJf96N&client_app=CamCard_AD_EA_2@7%2E0%2E0%2E20160707&type=mobile"
# login_headers = {
#     'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1; m2 Build/LMY47D)CamCard_AD_EA_2@7.0.0.20160707',
#     'Host': 'api.intsig.net',
#     'Connection': 'Keep-Alive',
# }
