# coding:utf-8

import requests
import re
data = {"id": "500223600285334",
        "type": "9999",
        "entid": "50022301008257",
        "name": u"中国移动通迅花岩营业厅"}
r = requests.post("http://gsxt.cqgs.gov.cn/search_ent", data=data)
print r.text