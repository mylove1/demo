# coding : utf-8
import re
print 'l'
a = '''陕西省丹凤县人民法院民 事 裁 定 书（2016）陕1022民初313号原告陈某某，女，汉族，农民。被告王某某，男，汉族，农民。委托代理人许广禄，丹凤县竹林关法律服务所法律工作者。案由：离婚纠纷本院在审理原告陈某某诉被告王某某离婚纠纷一案中，原告陈某某因自行与被告王某某和好为由，向本院提出撤诉申请。本院认为，原告陈某某申请撤诉符合法律规定，依照《中华人民共和国民事诉讼法》第一百四十五条一款、第一百五十四条一款（五）项之规定，裁定如下：准许原告陈某某撤回起诉。案件受理费100元，由原告陈某某负担。代理审判员　　龚永红二〇一六年七月二十一日书　记　员　　魏　沙'''
print 'llllll'
r_yuangao = re.compile(u'2(.*?)6')
r_beigao = ''
l_yuangao = r_yuangao.findall(a)
print l_yuangao[0]