# coding:utf-8
import re
import pybloom
table = []
a = '<tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>a</td><td>b</td><td>c</td><td>d</td></tr><tr><td>e</td><td>f</td><td>g</td><td>h</td></tr>'
table_total = re.findall('<tr>((?:<td>.*?</td>)+)</tr>', a)

print '\n'.join(table_total)
for enu, x in enumerate(table_total):
    table_total[enu] = re.findall('<td>(.*?)</td>', x)
print table_total
lenth = len(table_total[0])
print lenth
for x in table_total[1:]:
    this_dict = {}
    for enu in range(lenth):
        this_dict[table_total[0][enu]] = x[enu]
    table.append(this_dict)
print table
print isinstance(table, list)

m = u'杭州'
print '222'
f = pybloom.BloomFilter(capacity=1000000,error_rate=0.001)
f.add('http://wsgs.fjaic.gov.cn/creditpub/notice/view?uuid=hb6h.VOvgTbBQf_jvwV84EvP26gi08JU&tab=01')
print 'http://wsgs.fjaic.gov.cn/creditpub/notice/view?uuid=hb6h.VOvgTbBQf_jvwV84EvP26gi08JU&tab=01' in f