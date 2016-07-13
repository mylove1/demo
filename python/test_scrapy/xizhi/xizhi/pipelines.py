# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import MySQLdb.cursors
from xizhi.settings import DbConfig


class XizhiPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db=DbConfig['db'],
                                    host=DbConfig['host'], charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

        # 清空表
        # self.cursor.execute('truncate table weather;')
        # self.conn.commit()

    def process_item(self, item, spider):
        try:
            print "charu1"
            self.cursor.execute(
                """INSERT IGNORE INTO company (name, tyshxy, zc, zzjg, type, status, faren, zhuceziben, jingyingriqi, yingyeqixian, fazhaoriqi, guanwang, dengjijiguan, dizhi, fanwei)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    item['name'],
                    item['tyshxy'],
                    item['zc'],
                    item['zzjg'],
                    item['type'],
                    item['status'],
                    item['faren'],
                    item['zhuceziben'],
                    item['jingyingriqi'],
                    item['yingyeqixian'],
                    item['fazhaoriqi'],
                    item['guanwang'],
                    item['dengjijiguan'],
                    item['dizhi'],
                    item['fanwei'],
                )
            )
            self.conn.commit()
        except MySQLdb.Error, e:
            print 'Error %d %s' % (e.args[0], e.args[1])

        return item