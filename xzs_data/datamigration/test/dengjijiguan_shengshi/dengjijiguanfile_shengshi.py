# coding:utf-8
import re
# import pymongo
# import sys
#
# try:
#     sys.setdefaultencoding("utf-8")
# except:
#     reload(sys)
#     sys.setdefaultencoding("utf-8")
# MASTERIP = '192.168.0.50'
# conn = pymongo.Connection(MASTERIP, 27017)
# db = conn.xingzheng
if __name__ == '__main__':
    rea = re.compile('(^.*?)市.*?')
    with open("dengjijiguan3.txt", 'r') as f:
        for enu, x in enumerate(f.readlines()):
            print x
            sheng = rea.findall(x)
            if sheng:
                print sheng[0]
            print '\n', '------------------------'
            # db.dengjijiguan.insert({"name": x.strip(), "sheng": "不知道", "shi": "也不知道"})
            if enu == 100:break

