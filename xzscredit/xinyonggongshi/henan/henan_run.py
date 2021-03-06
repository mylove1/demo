# coding:utf-8

import requests
import os
import re
import pybloom
import pymongo
import infopage
import threading


def posthtml(page):
    url = 'http://222.143.24.157/exceptionInfoSelect.jspx'
    data = {"pageNo": page}
    while 1:
        try:
            return requests.post(url, data=data).text
        except:
            continue

def openbloomfile(BLOOMFILENAME):
    if BLOOMFILENAME in os.listdir('./'):
        with open(BLOOMFILENAME, 'rb') as bf:
            return pybloom.BloomFilter.fromfile(bf)
    else:
        return pybloom.BloomFilter(capacity=1000000,error_rate=0.001)

def savebloomtofile(f, BLOOMFILENAME):
    with open(BLOOMFILENAME, 'wb') as bf:
        f.tofile(bf)

def getinfotomongo(url, db):
    a = infopage.HeNanAnalyze(url)
    db.compinfo.insert(a.info())

if __name__ == '__main__':
    TOTAL = 0
    conn = pymongo.Connection("192.168.0.50", 27017)
    db = conn.henan
    BLOOMFILENAME = "fujianyichang.oom"
    f = openbloomfile(BLOOMFILENAME)

    for page in range(1, 5000):
        threadlist = []
        print page
        if TOTAL > 20:break
        for x in re.findall('href="/businessPublicity\.jspx\?id=(.*?)&sourceType=1"', posthtml(page)):
            if x in f:
                 print x
                 TOTAL += 1
                 print 'TOTAL：',TOTAL
                 break
            else:
                 f.add(x)
                 threadlist.append(threading.Thread(target=getinfotomongo,args=(x, db)))
        for thread in threadlist:
            thread.start()
        for thread in threadlist:
            thread.join()
    savebloomtofile(f, BLOOMFILENAME)
    print 'all have be down'
