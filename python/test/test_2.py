# -*- coding:utf-8 -*-
# 河南省信用异常企业正则匹配
import re

re_a = re.compile("""<ul>
        <li class="tb-a1"><a href="(.*?)" target=_blank>(.*?)</a>&nbsp;</li>
        <li class="tb-a2">(.*?)&nbsp;</li>
        <li class="tb-a3">(.*?)</li>
    </ul>""")
txt = ("""<div class="se-yichang">
    <ul>
        <li class="input-3"><input style="color:#000000;border-radius:5px;" name="gjz" id="gjz" type="text"
                                   onmouseover=this.focus();this.select();
                                   value="企业名称/注册号/统一社会信用代码" onclick="if(value=='企业名称/注册号/统一社会信用代码') {value='';}"
                                   onBlur="if(!value){value='企业名称/注册号/统一社会信用代码';}"/></li>
        <li class="se-su"><a href="#" onclick="showCaptcha();"><img src="images/se-su-a.png"
                                                                                 onMouseOver="this.src='images/se-su-a.png'"
                                                                                 onMouseOut="this.src='images/se-su-b.png'"/></a>
        </li>
    </ul>
</div>
</form>
<div style="height:600px;">
<div class="tb-a">
    <ul>
        <li class="tb-a1">企业名称</li>
        <li class="tb-a2">注册号/统一社会信用代码</li>
        <li class="tb-a3">被列入经营异常名录日期</li>
    </ul>
</div>

<div class="tb-b">
    <ul>
        <li class="tb-a1"><a href="/businessPublicity.jspx?id=3570046AA7EA1AA6E053050A080A734E&sourceType=1" target=_blank> 南阳市卧龙区顺丰农业服务专业合作社</a>&nbsp;</li>
        <li class="tb-a2">411303NA000262X &nbsp;</li>
        <li class="tb-a3">2016年6月17日</li>
    </ul>
</div>
<div class="tb-c">
    <ul>
        <li class="tb-a1"><a href="/businessPublicity.jspx?id=3570046AA7E91AA6E053050A080A734E&sourceType=1" target=_blank> 南阳市卧龙区强民农业服务专业合作社</a>&nbsp;</li>
        <li class="tb-a2">411303NA000259X &nbsp;</li>
        <li class="tb-a3">2016年6月17日</li>
    </ul>
</div>
<div class="tb-b">
    <ul>
        <li class="tb-a1"><a href="/businessPublicity.jspx?id=&sourceType=1" target=_blank> </a>&nbsp;</li>
        <li class="tb-a2"> &nbsp;</li>
        <li class="tb-a3">2016年6月17日</li>
    </ul>
</div>
<div class="tb-c">
    <ul>
        <li class="tb-a1"><a href="/businessPublicity.jspx?id=&sourceType=1" target=_blank> </a>&nbsp;</li>
        <li class="tb-a2"> &nbsp;</li>
        <li class="tb-a3">2016年6月17日</li>
    </ul>
</div>
<div class="tb-b">
    <ul>
        <li class="tb-a1"><a href="/businessPublicity.jspx?id=3575ACE9413D8CACE053050A080A7A02&sourceType=1" target=_blank> 郑州昕蕾文化传播有限公司</a>&nbsp;</li>
        <li class="tb-a2">410103000162077 &nbsp;</li>
        <li class="tb-a3">2016年6月17日</li>
    </ul>
</div>
<div class="tb-c">
    <ul>
        <li class="tb-a1"><a href="/businessPublicity.jspx?id=3575ACE9413D8CACE053050A080A7A02&sourceType=1" target=_blank> 郑州昕蕾文化传播有限公司</a>&nbsp;</li>
        <li class="tb-a2">410103000162077 &nbsp;</li>
        <li class="tb-a3">2016年6月17日</li>
    </ul>
</div>
<div class="tb-b">
    <ul>
        <li class="tb-a1"><a href="/businessPublicity.jspx?id=3575A255744F863DE053050A080A33D9&sourceType=1" target=_blank> 郑州蓉锦宽巷子企业管理有限公司</a>&nbsp;</li>
        <li class="tb-a2">410103000086027 &nbsp;</li>
        <li class="tb-a3">2016年6月17日</li>
    </ul>
</div>
<div class="tb-c">
    <ul>
        <li class="tb-a1"><a href="/businessPublicity.jspx?id=3575A255744F863DE053050A080A33D9&sourceType=1" target=_blank> 郑州蓉锦宽巷子企业管理有限公司</a>&nbsp;</li>
        <li class="tb-a2">410103000086027 &nbsp;</li>
        <li class="tb-a3">2016年6月17日</li>
    </ul>
</div>
<div class="tb-b">
    <ul>
        <li class="tb-a1"><a href="/businessPublicity.jspx?id=3575977E81857F4FE053050A080AE7B4&sourceType=1" target=_blank> 郑州紫贝壳广告策划有限公司</a>&nbsp;</li>
        <li class="tb-a2">410103000059296 &nbsp;</li>
        <li class="tb-a3">2016年6月17日</li>
    </ul>
</div>
<div class="tb-c">
    <ul>
        <li class="tb-a1"><a href="/businessPublicity.jspx?id=35758CCA7BA6795AE053050A080A3EA4&sourceType=1" target=_blank> 河南美亚国际航空运输有限公司</a>&nbsp;</li>
        <li class="tb-a2">914101037942651651 &nbsp;</li>
        <li class="tb-a3">2016年6月17日</li>
    </ul>
</div>
        <div >
            <table>
                <tr>
                </tr>
            </table>
        </div>

<form action="/exceptionInfoSelect.jspx" method="post" id="exceptionSubmit">
    <input type="hidden" name="pageNo" id="pageNo"/>
    <input type="hidden" name="gjz" id="gjz2" value=""/>


<div class="fenye" id="pages" style="width:1100px">
    <!--分页-->
                  <ul>
                  <li><a href="#" onclick="_gotoPage('6');">上一页</a></li>
                   <li><a  href="#"  onclick="_gotoPage(0+1);" >1</a></li>
                   <li><a  href="#"  onclick="_gotoPage(1+1);" >2</a></li>
                   <li><a  href="#"  onclick="_gotoPage(2+1);" >3</a></li>
                   <li><a  href="#"  onclick="_gotoPage(3+1);" >4</a></li>
                   <li><a  href="#"  onclick="_gotoPage(4+1);" >5</a></li>
                   <li><a  href="#"  onclick="_gotoPage(5+1);" >6</a></li>
                   <li><a  href="#"  onclick="_gotoPage(6+1);"  class="fenye-bj" >7</a></li>
                   <li><a  href="#"  onclick="_gotoPage(7+1);" >8</a></li>
                   <li><a  href="#"  onclick="_gotoPage(8+1);" >9</a></li>
                   <li><a  href="#"  onclick="_gotoPage(9+1);" >10</a></li>
                  <li><a href="#"  onclick="_gotoPage('8');">下一页</a></li>
                  <li style="padding-left:10px;color:#666666; font-size:14px;">共计：301178条,&nbsp;跳转到第&nbsp;<input id="jumpPageid"  type="text" style="width:25px;height:13px"/>&nbsp;页&nbsp;<a href="#" onclick="jumpPage('301178');">确定</a></li>
                  </ul>
            </div>
    </form>

</div>
 <div class="banqun">
            版权所有：河南省工商行政管理局 <a target="_blank" style="color:red;text-decoration:underline;font-size:14px; " href="http://gsxt.haaic.gov.cn/phone.jspx">业务(技术)支持电话</a><br/>
            地址：郑州市花园路127号&nbsp;&nbsp;邮政编码：450008&nbsp;&nbsp;<span style="color:red">建议使用IE8及以上版本浏览器</span></div>
</div>
</div>


""")
#"""<div class="tb-b"><ul><li class="tb-a1"><a href="(.*?)" target=_blank>(.*?)</a>(.*?)</li><li class="tb-a2">(.*?)</li><li class="tb-a3">(.*?)</li></ul></div>"""
for i in re_a.findall(txt):
    if ' ' in i:
        continue
    else:
        print ''.join(i)
        print i[1]
