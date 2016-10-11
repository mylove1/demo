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


# 更新记录
# sql_update = 'update dengjijiguan set t_sheng = "江苏省",t_shi = "南京市" where t_jiguan_name like "%南京%" and t_sheng is null;'
# cursor.execute(sql_update)

# 返回数据库中没有特定省市的记录
sql_no_info = 'select t_jiguan_name from dengjijiguan where t_jiguan_name like "%江苏%" and t_sheng is null;'
cursor.execute(sql_no_info)
for x in cursor.fetchall():
    print x[0]

# 返回数据库中没有省市的记录
# num = 0
# sql_no_info = 'select t_jiguan_name from dengjijiguan where t_shi is null;'
# cursor.execute(sql_no_info)
# for x in cursor.fetchall():
#     num += 1
#     print x[0]
# print num

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