# coding:utf-8
import random
import requests

l = [chr(x) for x in range(97, 123)]


def get_passwd(l):
    a = random.sample(l, 8)
    return ''.join(a)


tel = '13213840126'
data =


def send_msg(num, data):

    http_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'X-Requested-With': "XMLHttpRequest",
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age = 0'
    }
    s = requests.Session()
    print 'b'
    s.get('http://sso1.nlc.cn/ReadPortal/rdRegisterF.jsp', headers=http_headers)
    print 'c'
    # s.post('http://sso1.nlc.cn/ReadPortal/onblurbackup.action', headers=http_headers, data={'onblurbackup': data[num][3]['loginaccountt']})
    s.post(login_url, data=data[num][3], headers=http_headers)
    print 'ok'



if __name__ == '__main__':
    print 'a'
    send_msg(0, tel, data)
