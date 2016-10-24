import requests
r = requests.get(url="http://www.baidu.com", proxies=None)
r.encoding="utf-8"
print r.text