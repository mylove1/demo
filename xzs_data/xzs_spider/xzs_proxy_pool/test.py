# coding:utf-8
import requests
import urllib2
import json

def requests_time():
    url = "http://www.baidu.com"

    r = requests.get(url=url, proxies={"http": ip})
    print r.status_code
    print len(r.text)
    print r.elapsed.total_seconds()


# def urllib_time():
#     url = "http://www.baidu.com"
#     ip = '119.6.136.122:83'
#     r = urllib2.urlopen(url=url)


if __name__ == '__main__':
    ip = '119.6.136.122:83'
    requests_time()
    # codelist = []
    # codelist.append({"1": "yi"})
    # codelist.append({"2": "er"})
    # j = json.dumps(codelist)
    # print j
