# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#from twisted.enterprise import adbapi
#from hashlib import md5
import MySQLdb
import MySQLdb.cursors
from hnqyxy.settings import DbConfig


class HnqyxyPipeline(object):
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
                """INSERT IGNORE INTO t_hnxy (t_hnxy_name, t_hnxy_url, t_hnxy_numb)
                VALUES (%s, %s, %s)""",
                (
                    item['name'],
                    item['url'],
                    item['numb']
                )
            )
            self.conn.commit()
        except MySQLdb.Error, e:
            print 'Error %d %s' % (e.args[0], e.args[1])

        return item


'''
class HnqyxyPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    # pipeline默认调用
    def process_item(self, item, spider):
        print '1'
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        print 5
        d.addErrback(self._handle_error, item, spider)
        print 6
        d.addBoth(lambda _: item)
        print 7
        return d

    # 将每行更新或写入数据库中
    def _do_upinsert(self, conn, item, spider):
        print '2'
        linkmd5id = self._get_linkmd5id(item)
        # print linkmd5id
        conn.execute("""
                select 1 from hnqyxyurl where linkmd5id = %s
        """, (linkmd5id,))
        ret = conn.fetchone()

        if ret:
            conn.execute("""
                update hnqyxyurl set link = %s, numb = %s where linkmd5id = %s
            """, (item['link'], item['numb'], linkmd5id))
            # print """
            #    update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
            # """, (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id)
        else:
            conn.execute("""
                insert into hnqyxyurl(linkmd5id, link, numb)
                values(%s, %s, %s)
            """, (linkmd5id, item['link'], item['numb']))
            # print """
            #    insert into cnblogsinfo(linkmd5id, title, description, link, listUrl, updated)
            #    values(%s, %s, %s, %s, %s, %s)
            # """, (linkmd5id, item['title'], item['desc'], item['link'], item['listUrl'], now)

    # 获取url的md5编码
    def _get_linkmd5id(self, item):
        print '3'
        # url进行md5处理，为避免重复采集设计
        return md5(item['link']).hexdigest()

    # 异常处理
    def _handle_error(self, failue, item, spider):
        print '4'
        log.err(failure)
'''