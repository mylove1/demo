# coding:utf-8
import re
import pymongo
MASTERIP = '192.168.0.50'




if __name__ == '__main__':
    conn = pymongo.Connection(MASTERIP, 27017)
    db = conn.xingzheng
    with open("dengjijiguan3.txt", 'r') as f:
        # with open("dengjijiguan4.txt", 'w') as f2:
            for enu, x in enumerate(f.readlines()):
                x = x.strip()
                x = x.split('工商行政管理')[0]
                x = x.split('市场监督管理局')[0]
                x = x.split('市场和质量')[0]
                x = x.split('工商和质量监督管理局')[0]
                x = x.split('经济技术开发区')[0]
                x = x.split('经济开发区')[0]
                x = x.split('市场监督管理所')[0]
                x = x.split('工商质监局')[0]
                x = x.split('工商局')[0]
                x = x.split('工商所')[0]
                x = x.split('分局')[0]
                x = x.split('工商管理和质量技术监督局')[0]
                x = x.split('高新技术开发区')[0]
                x = x.split('市场监管局')[0]
                x = x.split('工商行政管理总局')[0]
                x = x.split('工业园区')[0]
                x = x.split('保税区')[0]
