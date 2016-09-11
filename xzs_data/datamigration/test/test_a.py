# coding:utf-8
import re
a = "灵石县市场和质量监督管理局"
a = re.findall('(.*?)管理局(.*?)', a)
print a

print a
b = [1, 2]
m, n = b
print m
print n
