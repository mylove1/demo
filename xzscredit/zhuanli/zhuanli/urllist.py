# -*- coding: utf-8 -*-

import MySQLdb
import MySQLdb.cursors
# from zhuanli.settings import DbConfig
#
# conn = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db=DbConfig['db'],
#                             host=DbConfig['host'], charset='utf8', use_unicode=True)
# cursor = conn.cursor()
urllist = []
conn = MySQLdb.connect(host='192.168.0.100', user='root', passwd='dingyu', db='dingyu', port=3306, charset="utf8")
cursor = conn.cursor()
a = 1
b = 1000000
cursor.execute("select name from company_zong where id between %s and %s  ;" % (a, b))
aa = cursor.fetchall()
for x in aa:
    urllist.append('http://cpquery.sipo.gov.cn//txnQueryOrdinaryPatents.do?select-key%3Ashenqingh=&select-key%3Azhuanlimc=&select-key%3Ashenqingrxm=' + x[0] +'&select-key%3Azhuanlilx=&select-key%3Ashenqingr_from=&select-key%3Ashenqingr_to=&attribute-node:record_start-row=1&attribute-node:record_page-row=100&')


