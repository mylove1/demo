# coding:utf-8
import MySQLdb
import pymongo

# moconn = pymongo.Connection("192.168.0.50", 27017)
# db = moconn.test
# db.lindmysql.insert({"name": u"加油", "info": u"这条记录前加了油"})
# db.lindmysql.insert({"name": "没加油", "info": u"这条记录前没加油"})


myconn = MySQLdb.connect(host='192.168.0.50',
                       user='root',
                       passwd='dingyu',
                       db='test',
                       port=3306,
                       charset="utf8")


mycur = myconn.cursor()
aa = mycur.execute('insert into linkmongo(name,info)values(%s,%s)',(u"加油", u"这条记录前加了油"))
aa = mycur.execute('insert into linkmongo(name,info)values(%s,%s)',("没加油", "这条记录前没有加油"))
myconn.commit()
mycur.close()
myconn.close()

