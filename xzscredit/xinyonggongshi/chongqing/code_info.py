# coding:utf-8
import requests
import json
import pymongo
import threading


class getent(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            print len(comp_list)
            try:
                key = comp_list.pop(0)
            except:
                break
            url = 'http://gsxt.cqgs.gov.cn/search_getEnt.action?entId=%s&id=%s&stype=SAIC&type=1' % (key[0], key[1])
            text = get_html(url)[6:]
            if text == 'null':
                print url
                print key[2]
                break
            #     continue
            # jsontext = json.loads(text)
            # try:
            #     db.getent.insert(jsontext)
            # except:
            #     print url
            #     print text
            #     print key
            #     break


def get_html(url):
    while 1:

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
                'Referer': 'http://gsxt.cqgs.gov.cn/',
            }
            r = requests.get(url, headers=headers)
            r.encoding = "utf-8"
            return r.text
        except:
            pass


if __name__ == '__main__':
    conn = pymongo.Connection('192.168.100.55', 27017)
    db = conn.chongqing
    comp_list = []
    for x in db.namelist.find():
        comp_list.append([x["pripid"], x["regcode"], x["name"]])
    print len(comp_list)
    for x in xrange(2):
        a = getent()
        a.start()


