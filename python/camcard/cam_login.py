# coding:utf-8
import requests
from lxml import etree

login_url = "https://api.intsig.net/user/login2?user=13213840126&password=0b857a0d2718d517&client=Android-m2&client_id=78e5LED244KdyRD92DgJf96N&client_app=CamCard_AD_EA_2@7%2E0%2E0%2E20160707&type=mobile"
login_headers = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1; m2 Build/LMY47D)CamCard_AD_EA_2@7.0.0.20160707',
    'Host': 'api.intsig.net',
    'Connection': 'Keep-Alive',
}


tree = etree.HTML(a)
print tree.xpath('//uid/text()')

