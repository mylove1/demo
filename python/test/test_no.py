# coding:utf-8
import urllib
import requests
import threading
#
# url = 'http://www.chatm.com/chatm/goBrandDetail?zch=B52ISmgHfME=&category=1'
#
#
class ceshi(threading.Thread):
    def __init__(self):
        self.url = 'http://www.chatm.com/chatm/goBrandDetail?zch=B52ISmgHfME=&category=1'
        threading.Thread.__init__(self)

    def structure_url(self, company):
        stru_comp = urllib.quote(company).replace('%', '%25')
        return 'http://sbcx.saic.gov.cn:9080/tmois/wszhcx_getLikeCondition.xhtml?appCnName=' + stru_comp + '&intCls=&paiType=0'


    def run(self):
        for x in ['就死放假我']:
            r = requests.get(self.structure_url(x))
            print r.text
            print r.url
            print r.status_code

if __name__ == '__main__':
    for x in range(1):
        a = ceshi()
        a.start()
