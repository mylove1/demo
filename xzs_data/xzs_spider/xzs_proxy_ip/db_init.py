# coding:utf-8

import sqlite3
import config
import pymongo
sql1 = '''
DROP TABLE IF EXISTS `alive`;'''
sql2 = '''
CREATE TABLE `alive` (
  `t_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `t_ip` CHAR(21) NOT NULL DEFAULT NULL
);
'''
conn = sqlite3.connect(config.DB_FILE)
cursor = conn.cursor()
cursor.execute(sql1)
cursor.execute(sql2)
connp = pymongo.Connection('192.168.0.50', 27017)
db = connp.ip
for x in db.useful.find():
    print x["ip"]
    if len(x["ip"]) > 21:
        print x["ip"]
        continue
    cursor.execute('insert into alive (t_ip) values ("%(ip)s");'% x)
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()
