# coding=utf-8
import requests
import re
# import MySQLdb
import time
from PIL import Image
import pytesseract

# image = Image.open('0366.jpg')
# vcode = pytesseract.image_to_string(image)
index = 2000
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
    'Referer': 'http://wenshu.court.gov.cn/List/ListContent',
    'Connection': 'keep-alive',
}

DbConfig = {
 # db config
 'user': 'root',
 'passwd': 'dingyu',
 'db': 'dingyu',
 'host': '192.168.0.102',
}

proxies = {

    }
if __name__ == '__main__':
    # conn = MySQLdb.connect(user=DbConfig['user'],
    #                        passwd=DbConfig['passwd'],
    #                        db=DbConfig['db'],
    #                        host=DbConfig['host'],
    #                        charset='utf8',
    #                        use_unicode=True
    #                        )
    # cursor = conn.cursor()

    url = 'http://wenshu.court.gov.cn/List/ListContent'
    data = {
        'Param': '上传日期:2016-07-22,案件类型:刑事案件',
        'Index': '1',
        'Page': '5',
        'Order': '法院层级',
        'Direction': 'asc',
    }

    for ind in xrange(1, index):
        print "start sleep"
        # time.sleep(1)
        print "sleep stop"
        print ind
        # data['Index'] = str(ind)
        # try:
        # r = requests.post(url, headers=headers, data=data)
        r = requests.post('http://wenshu.court.gov.cn/List/TreeContent', data={"Param": ""})
        text = r.text

        if (len(text)) < 100:
            print text
            # if (len(text)) == 8:
            #     image = requests.get('http://wenshu.court.gov.cn/User/ValidateCode/8259').content
            #     with open('jpg.jpg', 'wb') as imag:
            #         imag.write(image)
            #     image = Image.open('jpg.jpg')
            #     code = pytesseract.image_to_string(image)
            #     print code
            #     codedata = {'ValidateCode': code}
            #     a = requests.post('http://wenshu.court.gov.cn/Content/CheckVisitCode', headers=headers, data=codedata)
            #     print 'ok'
        print '-----------------------------'


