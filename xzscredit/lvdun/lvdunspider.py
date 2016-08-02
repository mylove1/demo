# -*- coding: utf-8 -*-
import requests
import re
import random
import MySQLdb
import threading
import sys
import time
import setting


reload(sys)
sys.setdefaultencoding('utf-8')


# def get_company_list(start, stop):
#     comp_list = []
#     conn = MySQLdb.connect(host='192.168.0.100', user='root', passwd='dingyu', db='dingyu', port=3306, charset="utf8")
#     cursor = conn.cursor()
#     cursor.execute("select name from company_zong where id between %s and %s  ;" % (start, stop))
#     aa = cursor.fetchall()
#     for x in aa:
#         comp_list.append(x[0])
#     return comp_list


class chinaz(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.header = headers

    def get_html(self, key):

        while 1:
            this_headers = {
                'User-Agent': random.choice(headers),
                'Referer': 'http://www.11315.com/',
                'Connection': 'keep-alive',
            }
            # [use proxy]
            try:
                proxy = requests.get('http://192.168.0.100:8384/ip').text
                r = requests.post(key, headers=this_headers, proxies={'http': proxy}, timeout=5)
                print r.status_code
                html = r.text
                if r.status_code != 200:
                    continue
                else:
                    if len(html) < 2000:
                        continue

                break
            except:
                continue
                # print proxy, 'is bad'

        html = html.split()
        html = ''.join(html)
        return html

    def get_list(self, key):
        urllist = ['http://', str('%08d' % key), '.11315.com/']
        url = ''.join(urllist)
        html = self.get_html(url)
        if '您想浏览的网页找不到'in html:
            return ''
        rea = re.compile('com"target="_blank"title="(.*?)">.*?</a>')
        try:
            try:
                name = rea.findall(html)[1]
            except:
                reb = re.compile('class="h1_icp">(.*?)<span>')
                name = reb.findall(html)[0]
        except:
            name = ''
        return name

    def to_db(self, name):
        try:
            cursor.execute("insert into t_lvdun(t_lvdun_name)values('%s');" % name)
            conn.commit()
        except MySQLdb.Error, e:
            print 'Error %d %s' % (e.args[0], e.args[1])


    def run(self):
        while True:
            try:
                key = keylist.pop(0)
            except:
                break
            name = self.get_list(key)
            if name != '':
                print '-----------------------------', key, name
                self.to_db(name)
            else:
                print '----------------------------x', key


if __name__ == '__main__':
    start = 1
    end = 10000
    keylist = [x for x in xrange(start, end)]

    conn = MySQLdb.connect(host='192.168.0.100', user='root', passwd='dingyu', db='dingyu', port=3306, charset="utf8")
    cursor = conn.cursor()

    headers = setting.agents

    for x in range(20):
        thread = chinaz()
        thread.start()



