# coding:utf-8
import re
aa = '''  <tr><td>CN101010400</td><td>shunyi</td><td>顺义</td><td>北京</td><td>北京</td></tr>
        <tr><td>CN101010500</td><td>huairou</td><td>怀柔</td><td>北京</td><td>北京</td></tr>
        <tr><td>CN101010600</td><td>tongzhou</td><td>通州</td><td>北京</td><td>北京</td></tr>
        <tr><td>CN101010700</td><td>changping</td><td>昌平</td><td>北京</td><td>北京</td></tr>
        <tr><td>CN101010800</td><td>yanqing</td><td>延庆</td><td>北京</td><td>北京</td></tr>
        <tr><td>CN101010900</td><td>fengtai</td><td>丰台</td><td>北京</td><td>北京</td></tr>
        <tr><td>CN101011000</td><td>shijingshan</td><td>石景山</td><td>北京</td><td>北京</td></tr>
        <tr><td>CN101011100</td><td>daxing</td><td>大兴</td><td>北京</td><td>北京</td></tr>
        <tr><td>CN101011200</td><td>fangshan</td><td>房山</td><td>北京</td><td>北京</td></tr>
        <tr><td>CN101011300</td><td>miyun</td><td>密云</td><td>北京</td><td>北京</td></tr>
        <tr><td>CN101011400</td><td>mentougou</td><td>门头沟</td><td>北京</td><td>北京</td></tr>
        <tr><td>CN101011500</td><td>pinggu</td><td>平谷</td><td>北京</td><td>北京</td></tr>
        <tr><td>CN101020100</td><td>shanghai</td><td>上海</td><td>上海</td><td>上海</td></tr>
        <tr><td>CN101020200</td><td>minhang</td><td>闵行</td><td>上海</td><td>上海</td></tr>
        <tr><td>CN101020300</td><td>baoshan</td><td>宝山</td><td>上海</td><td>上海</td></tr>
        <tr><td>CN101020500</td><td>jiading</td><td>嘉定</td><td>上海</td><td>上海</td></tr>
        <tr><td>CN101020600</td><td>nanhui</td><td>浦东南汇</td><td>上海</td><td>上海</td></tr>
        <tr><td>CN101020700</td><td>jinshan</td><td>金山</td><td>上海</td><td>上海</td></tr>
        <tr><td>CN101020800</td><td>qingpu</td><td>青浦</td><td>上海</td><td>上海</td></tr>
        <tr><td>CN101020900</td><td>songjiang</td><td>松江</td><td>上海</td><td>上海</td></tr>
        <tr><td>CN101021000</td><td>fengxian</td><td>奉贤</td><td>上海</td><td>上海</td></tr>
        <tr><td>CN101021100</td><td>chongming</td><td>崇明</td><td>上海</td><td>上海</td></tr>
        <tr><td>CN101021200</td><td>xujiahui</td><td>徐家汇</td><td>上海</td><td>上海</td></tr>
        <tr><td>CN101021300</td><td>pudong</td><td>浦东</td><td>上海</td><td>上海</td></tr>
        <tr><td>CN101030100</td><td>tianjin</td><td>天津</td><td>天津</td><td>天津</td></tr>
        <tr><td>CN101030200</td><td>wuqing</td><td>武清</td><td>天津</td><td>天津</td></tr>
        <tr><td>CN101030300</td><td>baodi</td><td>宝坻</td><td>天津</td><td>天津</td></tr>
        <tr><td>CN101030400</td><td>dongli</td><td>东丽</td><td>天津</td><td>天津</td></tr>
'''

aaa = aa.replace('\n', '')
print aaa
