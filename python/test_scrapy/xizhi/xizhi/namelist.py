# coding:utf-8
import MySQLdb
from xizhi.settings import DbConfig

def getList():
    conn = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db=DbConfig['db'],
                                host=DbConfig['host'], charset='utf8', use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('select name from shunco where id < 50;')
    nametuple = cursor.fetchall()
    namelist = ['http://www.xizhi.com/search?wd='+x[0] for x in nametuple]
    return namelist




namelist = getList()

print '----------'.join(namelist)
