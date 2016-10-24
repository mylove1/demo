#!/usr/bin/env python
# coding:utf-8

import requests

url = 'http://222.143.24.157/queryListData.jspx'

data = {
	"searchType": '1',
	'entName': u'平顶山市科技',
	'currentPageIndex': '1'
}

r = requests.get(url=url, data=data)
print r.text
print r.status_code
print r.headers