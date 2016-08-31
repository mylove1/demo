# coding:utf-8
import requests
url = 'http://222.143.24.157/QueryYearExamineDetail.jspx?id=ff808081543caa8d01544b7d7547216b'
r = requests.get(url)
print r.text