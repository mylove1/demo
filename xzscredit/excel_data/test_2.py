# coding:utf-8

import xml.dom.minidom

dom = xml.dom.minidom.parse(u"F:\\企业目录（整理好）\\[青海.xls")
root = dom.documentElement
print root.nodeName
print