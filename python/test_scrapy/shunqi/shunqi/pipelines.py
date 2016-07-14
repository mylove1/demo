# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
from shunqi.settings import DbConfig


class ShunqiPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db=DbConfig['db'],
                                    host=DbConfig['host'], charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """INSERT IGNORE INTO shunco (name, sheng, shi, shunqiurl)
                VALUES (%s, %s, %s, %s)""",
                (
                    item['name'],
                    item['sheng'],
                    item['shi'],
                    item['url'],
                )
            )
            self.conn.commit()
        except MySQLdb.Error, e:
            print 'Error %d %s' % (e.args[0], e.args[1])

        return item