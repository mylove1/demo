# coding:utf-8
import requests
import random
import config


url = 'http://www.tianyancha.com/company/80424269.json'
headers = {
    'Host': 'www.tianyancha.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Tyc-From': 'normal',
    'CheckError': 'check',
    'Referer': 'http://www.tianyancha.com/company/80424269',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'TYCID': 'ae1724aaf1c8467ea98857751ca5b365',
    'tnet': '115.193.34.157',
    'Hm_lvt_e92c8d65d92d534b0fc290df538b4758': '1470226465',
    'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758': '1470233531',
    '_pk_ref.1.e431': '%5B%22%22%2C%22%22%2C1470233531%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dfvk2-mIvt_V6J5ua_xZm7DZ3Kmimxq11gNx368bfboNBpipA5cYuwSssE7HnJIOF%26wd%3D%26eqid%3Dc280475a0008790900000004576dee5d%22%5D',
    '_pk_id.1.e431': 'f4c1214caa44b719.1466822242.4.1470233531.1470233531.',
    '_pk_ses.1.e431': '*',
    'token': '533b33aee3654fe29740b5aeda21b887',
    '_utm': '3103b6438c704a35b62f844ae62eb09b',
}
r = requests.get(url, headers=headers)
print r.text