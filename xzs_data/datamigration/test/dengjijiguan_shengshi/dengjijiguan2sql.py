# coding:utf-8
import re
import pymongo
import sqlite3


# MASTERIP = '192.168.0.50'
# conn = pymongo.Connection(MASTERIP, 27017)
# db = conn.xingzheng

conn = sqlite3.Connection("dengjijiguan.db")
cursor = conn.cursor()

cr_sql = '''
CREATE TABLE `dengjijiguan` (
  t_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  t_jiguan_name VARCHAR(100) NOT NULL DEFAULT NULL,
  t_sheng VARCHAR(10) DEFAULT NULL,
  t_shi VARCHAR(10) DEFAULT NULL
);
'''

# cursor.execute(cr_sql)


# 返回数据库中没有省市的记录
sql_no_info = 'select t_jiguan_name from dengjijiguan where t_jiguan_name like "%南京%";'
cursor.execute(sql_no_info)
for x in cursor.fetchall():
    print x[0]

# 把文件中的导入数据库
# with open("dengjijiguan2.txt", 'r') as f:
#     for x in f.readlines():
#         x = x.split()[0]
#         if len(x) < 10:
#             continue
#         sql = "insert into dengjijiguan (t_jiguan_name) values ('%s');" % x
#         print sql
#         cursor.execute(sql)

cursor.close()
conn.commit()
conn.close()