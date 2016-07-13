# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
from cooper.settings import DBCOOFIG


class CooperPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=DBCOOFIG['user'], passwd=DBCOOFIG['passwd'], db=DBCOOFIG['db'],
                                    host=DBCOOFIG['host'], charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

        # 清空表
        # self.cursor.execute('truncate table weather;')
        # self.conn.commit()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """INSERT IGNORE INTO hnqyxyurl (link, numb)
                VALUES (%s, %s)""",
                (
                    item['link'],
                    item['numb']
                )
            )
            self.conn.commit()
        except MySQLdb.Error, e:
            print 'Error %d %s' % (e.args[0], e.args[1])
        return item

'''
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in unicode(item['description']).lower():
                raise DropItem("Contains forbidden word: %s" % word)
        else:
            return item
'''
'''
class W3SchoolPipeline(object):
    def __init__(self):
        self.file = codecs.open('w3school_data_utf8.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        # print line
        self.file.write(line.decode("unicode_escape"))
        return item
'''