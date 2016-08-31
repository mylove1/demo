# coding:utf-8
import re

class CreditChinaInfo():
    def __init__(self, html):
        self.html = ''.join(self.delcss(html).split())

    def delcss(self, html):
        li = {
            "<ul.*?>": "<ul>"
            # "<a.*?>": "<a>",
            # "<li.*?>": "<li>",
            # "<tr.*?>": "<tr>",
            # "<td.*?>": "<td>",
            # "<th.*?>": "<th>",
            # "<col.*?>": "<col>",
            # "<table.*?>": "<table>",
            # "<div.*?>": "<div>",
            # "<!--.*?-->": "",

        }
        for x in li.keys():
            re_this = re.compile(x)
            html = re_this.sub(li[x], html)
        return html


    def chapter(self, re_this, html):
        return ''.join(re.findall(re_this, html))


    def baseinfo(self, html):
        thisinfo = {}
        for x in re.findall("<ul>(.*?)</ul>", html):
            for y in re.findall("<strong>(.*?)</strong>(.*?)</li>", x):
                thisinfo[y[0][:-1]] = y[1]
                # print y[0][:-1], y[1]
        return thisinfo


    def tableinfo(self, html):
        thisinfo = []

        for x in re.findall("<ul>(.*?)</ul>", html):
            thisdict = {}
            for y in re.findall("<strong>(.*?)</strong>(.*?)</li>", x):
                thisdict[y[0][:-1]] = y[1]
            thisinfo.append(thisdict)
        return thisinfo

    def info(self):
        compinfo = {}
        jilulist = self.html.split(">></small>")
        t = [u"基础信息", u"优良记录", u"不良记录", u"失信记录"]
        try:
            compinfo[t[0]] = self.baseinfo(jilulist[1])
        except:
            pass

        for x in range(1,4):
            try:
                compinfo[t[x]] = self.tableinfo(jilulist[x+1])
            except:
                pass
        return compinfo



if __name__ == '__main__':
    html = """

    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <meta name="keywords" content="信用中国,creditchina,个人信用,企业信用,信用动态,信用记录,信用搜索,政策法规,信用服务,信用知识,信用评价,联合惩戒,黑名单,失信黑名单,双公式,公式处罚"/>
    <meta name="description" content="“信用中国”网站由国家发展改革委、人民银行指导，国家信息中心主办，百度公司提供独家技术支持，是政府褒扬诚信、
    惩戒失信的权威门户网站。信用,信用中国,信用动态,信用记录,信用搜索,政策法规,信用服务,信用知识,信用评价,联合惩戒,失信黑名单,双公式处罚,行政处罚,
    行政许可,异常名录"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>

    <!--百度站长验证代码-->
    <meta name="baidu-site-verification" content="4avuzk40L6"/>
    <!--百度站长验证代码-->

    <!--百度自动推送-->
    <script>
        (function () {
            var bp = document.createElement('script');
            var curProtocol = window.location.protocol.split(':')[0];
            if (curProtocol === 'https') {
                bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
            }
            else {
                bp.src = 'http://push.zhanzhang.baidu.com/push.js';
            }
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(bp, s);
        })();
    </script>
    <!--百度自动推送-->

    <!--百度统计验证代码-->
    <script>
        var _hmt = _hmt || [];
        (function () {
            var hm = document.createElement("script");
            hm.src = "//hm.baidu.com/hm.js?0076fef7e919d8d7b24383dc8f1c852a";
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(hm, s);
        })();
    </script>
    <!--百度统计验证代码-->

    <link rel="stylesheet" href="http://static.creditchina.gov.cn/css/index.css">
    <link rel="stylesheet" href="http://static.creditchina.gov.cn/css/meta.css">
        <title>信用信息共享搜索 | 信用中国</title>
    </head>
    <body>
    <div class="wrapper">
    <div class="mod-header">
            <p class="mod-header-top">
                <span class="top-link top-link-b"><a href="/about">关于我们</a></span>
                <span class="top-link top-link-a  "><a href="/announcement">网站声明</a></span>
             </p>
             <div class="mod-header-mid">
        	        <span class="logo"><a href="/home"><img src="/img/logo.png"></a></span>
    	    </div>
        	<div class="mod-header-nav">
                <div class="container">
                    <a href="/home"  class="nav-item "><span>首页</span></a>
                    <a href="/channel_news/1"   class="nav-item "><span>信用动态</span></a>
                    <a href="/channel_news/2"  class="nav-item "><span>政策法规</span></a>
                    <a href="/goDisciplinary"  class="nav-item "><span>联合惩戒</span></a>
                    <a href="/channel_news/0" class="nav-item "><span>信用服务</span></a>
                    <!--
                    <a href="/channel_news/7"  class="nav-item "><span>信用研究</span></a>
                    <a href="/channel_news/8"  class="nav-item "><span>信用知识</span></a>
                    -->
                    <a href="/channel_news/17"  class="nav-item "><span>信用百科</span></a>
                    <a href="/channel_news/19"  class="nav-item "><span>V信用</span></a>
                    <a href="/toNavigation"  class="nav-item "><span>信用导航</span></a>
                    <!--
                    <a href="/channel_news/14"  class="nav-item ">互动话题</a>
                    <a href="/search" class="nav-item-last nav-item-last-active "><span class="nav-item-icon"></span><span class="last-text">信用信息共享</span></a>
                    -->
                </div>
            </div>
    </div>
    <div class="mod-page mod-page-creditsearch clearfix">
        <div class="container">
            <ol class="breadcrumb">
                <li><i class="index-bread"></i><a href="/home" class="gray">首页</a></li>
                <li><a href="/search_all#selectType=0&page=1">信用信息共享</a></li>
                <li><a class="active" href="javascript:reload()">信用详情</a></li>
            </ol>
            <header class="page-channel-header">
                <h1>安徽大昌矿业集团有限公司</h1>
            </header>
            <ul class="creditsearch-tags clearfix">
                <li class="disabled">
                    <a href="#csdetail1">基础信息</a>
                </li>
                <li class="disabled">
                    <a href="#csdetail2">优良记录</a>
                </li>
                <li >
                    <a href="#csdetail3">不良记录（1）</a>
                </li>
                <li >
                    <a href="#csdetail4">失信记录（8）</a>
                </li>
                <li class="creditsearch-tags-time">
                    <span>【查询时间：2016年08月31日 08时58分】</span>
                </li>
            </ul>
            <div class="creditsearch-tagsinfos">
                <header>
                    <h1 class="clearfix" id="csdetail1">
                        基础信息
                        <small>收起>></small>
                    </h1>
                </header>
                <div class="creditsearch-tagsinfo">
                    <img src="/img/watermark.png" class="creditsearch-tagsinfo-img">
                    <!-- 企业的基本信息,个人没有该信息 -->
                    <ul class="creditsearch-tagsinfo-ul">
                        <li class="oneline"><strong>企业名称：</strong>安徽大昌矿业集团有限公司</li>
                        <li class="oneline"><strong>法人：</strong></li>
                        <li class="oneline"><strong>工商注册号：</strong>341522000001910</li>
                        <li class="oneline"><strong>注册资金：</strong>21080.000000
                            万(元)                    </li>
                        <li class="oneline"><strong>住所：</strong>安徽省六安市霍邱经济开发区</li>
                        <li class="oneline"><strong>成立日期：</strong>2004-07-13</li>
                        <li class="oneline"><strong>营业期限：</strong>
                        2004-07-13 至 无固定期限
                        </li>
                        <li class="oneline"><strong>经营范围：</strong>霍邱吴集铁矿（南段）采矿、选矿、销售;极贫铁矿采选和销售（必须具备其他有关法定条件许可的，在取得许可证后方可从事铁矿开采）。</li>
                        <li class="oneline"><strong>审核日期：</strong>2015-04-20</li>
                        <!-- 企业的基本信息,个人没有该信息 -->
                    </ul>
                </div>

                <header>
                    <h1 class="clearfix" id="csdetail2">
                        优良记录
                        <small>展开>></small>
                    </h1>
                </header>
                <div class="creditsearch-tagsinfo hidden">
                    <p class="text-info">平台未收录该企业的优良记录。</p>
                </div>

                <header>
                    <h1 class="clearfix" id="csdetail3">
                        不良记录
                        <small>收起>></small>
                    </h1>
                </header>
                <div class="creditsearch-tagsinfo">
                            <img src="/img/watermark.png" class="creditsearch-tagsinfo-img">
                            <ul class="creditsearch-tagsinfo-ul">
                                    <li class="oneline">
                                        <strong>所在地区：</strong>
                                            安徽
                                    </li>
                                    <li class="oneline">
                                        <strong>检查机关：</strong>
                                            安徽省六安市地方税务局稽查局
                                    </li>
                                    <li class="oneline">
                                        <strong>纳税人名称：</strong>
                                            安徽大昌矿业集团有限公司
                                    </li>
                                    <li class="oneline">
                                        <strong>纳税人识别码：</strong>
                                            342423764768183
                                    </li>
                                    <li class="oneline">
                                        <strong>组织机构代码：</strong>
                                            764768183
                                    </li>
                                    <li class="oneline">
                                        <strong>注册地址：</strong>
                                            安徽省霍邱县经济技术开发区
                                    </li>
                                    <li class="oneline">
                                        <strong>法定代表人或者负责人姓名：</strong>
                                            吉少清
                                    </li>
                                    <li class="oneline">
                                        <strong>法定代表人或者负责人性别：</strong>
                                            男
                                    </li>
                                    <li class="oneline">
                                        <strong>法定代表人或者负责人证件名称：</strong>
                                            身份证
                                    </li>
                                    <li class="oneline">
                                        <strong>负有直接责任的财务负责人姓名：</strong>
                                            赵化礼
                                    </li>
                                    <li class="oneline">
                                        <strong>负有直接责任的财务负责人性别：</strong>
                                            男
                                    </li>
                                    <li class="oneline">
                                        <strong>负有直接责任的财务负责人证件名称：</strong>
                                            身份证
                                    </li>
                                    <li class="oneline">
                                        <strong>负有直接责任的中介机构信息：</strong>
                                                暂无
                                    </li>
                                    <li class="oneline">
                                        <strong>案件性质：</strong>
                                            偷税
                                    </li>
                                    <li class="oneline">
                                        <strong>主要违法事实：</strong>
                                            经安徽省六安市地方税务局稽查局检查，发现其在2003年07月01日至2013年03月31日期间，主要存在以下问题：采取偷税手段，不缴或者少缴应纳税款4744.36万元。
                                    </li>
                                    <li class="oneline">
                                        <strong>相关法律依据及处理处罚情况：</strong>
                                            依照《中华人民共和国税收征收管理法》等相关法律法规的有关规定，对其处以追缴税款4744.36万元的行政处理、处以罚款2725.83万元的行政处罚。
                                    </li>
                                    <li class="oneline">
                                        <strong>发布级别：</strong>
                                            总局及以下
                                    </li>
                            </ul>
                </div>

                <header>
                    <h1 class="clearfix" id="csdetail4">
                        失信记录
                        <small>收起>></small>
                    </h1>
                </header>
                <div class="creditsearch-tagsinfo " id="dishonestyImg">
                        <img src="/img/watermark.png" class="creditsearch-tagsinfo-img">
                        <ul class="creditsearch-tagsinfo-ul clearfix">
                                <li class="oneline">
                                    <strong>案号：</strong>
                                        (2015)霍法执字第00568号
                                </li>
                                <li class="oneline">
                                    <strong>省份：</strong>
                                        安徽
                                </li>
                                <li class="oneline">
                                    <strong>执行法院：</strong>
                                        霍邱县人民法院
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人具体情形：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>被执行人的履行情况：</strong>
                                        全部未履行
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人行为具体情形：</strong>
                                        其他有履行能力而拒不履行生效法律文书确定义务
                                </li>
                                <li class="oneline">
                                    <strong>法定代表人或者负责人姓名：</strong>
                                        吉少清
                                </li>
                                <li class="oneline">
                                    <strong>立案时间：</strong>
                                        20150716
                                </li>
                                <li class="oneline">
                                    <strong>做出执行依据单位：</strong>
                                        霍邱县劳动人事争议仲裁委员会
                                </li>
                                <li class="oneline">
                                    <strong>生效法律文书确定的义务：</strong>
                                        被申请人安徽大昌矿业集团有限公司向申请人郑道安支付人民币115217元
                                </li>
                                <li class="oneline">
                                    <strong>发布时间：</strong>
                                        2016年08月10日
                                </li>
                                <li class="oneline">
                                    <strong>执行依据文号：</strong>
                                        （2014）霍劳人仲裁字292号仲裁调解书
                                </li>
                                <li class="oneline">
                                    <strong>作出执行依据单位：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>已履行：</strong>
                                            暂无
                                </li>
                                <li class="oneline">
                                    <strong>未履行：</strong>
                                            暂无
                                </li>
                        </ul>
                        <img src="/img/watermark.png" class="creditsearch-tagsinfo-img">
                        <ul class="creditsearch-tagsinfo-ul clearfix">
                                <li class="oneline">
                                    <strong>案号：</strong>
                                        (2015)霍法执字第00514号
                                </li>
                                <li class="oneline">
                                    <strong>省份：</strong>
                                        安徽
                                </li>
                                <li class="oneline">
                                    <strong>执行法院：</strong>
                                        霍邱县人民法院
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人具体情形：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>被执行人的履行情况：</strong>
                                        全部未履行
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人行为具体情形：</strong>
                                        其他有履行能力而拒不履行生效法律文书确定义务
                                </li>
                                <li class="oneline">
                                    <strong>法定代表人或者负责人姓名：</strong>
                                        吉少清
                                </li>
                                <li class="oneline">
                                    <strong>立案时间：</strong>
                                        20150630
                                </li>
                                <li class="oneline">
                                    <strong>做出执行依据单位：</strong>
                                        六安市中级人民法院
                                </li>
                                <li class="oneline">
                                    <strong>生效法律文书确定的义务：</strong>
                                        一、维持安徽省霍邱县人民法院（2014）霍民一初字第01051号民事判决第一、二、五、七、八项，即：一、被告安徽大昌矿业集团有限公司支付原告王能力医疗费18456.19元，住院伙食补助费784元，住院期间的护理费4901元，计24141.20元。二、被告安徽大昌矿业集团有限公司一次性支付原告王能力交通费、住宿费10000元。五、被告安徽大昌矿业集团有限公司一次性支付原告王能力二倍工资110000元。七、被告安徽大昌矿业集团有限公司于本判决生效之日起三十日内为原告王能力参加社会保险，并补缴费用，期间从2004年4月起，其中属于个人应补缴的部分由王能力自行承担。八、驳回原告王能力其他诉讼请求。二、撤销安徽省霍邱县人民法院（2014）霍民一初字第01051号民事判决第三、四、六项，即：三、被告安徽大昌矿业集团有限公司一次性支付原告王能力停工留薪期工资75701元。四、被告安徽大昌矿业集团有限公司一次性支付原告王能力伤残补助金157710.41元。六、被告安徽大昌矿业集团有限公司按月支付原告伤残津贴2603.55元，直至原告办理退休手续时止。三、安徽大昌矿业集团有限公司一次性支付王能力停工留薪期工资120000元。四、安徽大昌矿业集团有限公司一次性支付王能力伤残补助金300000元。五、安徽大昌矿业集团有限公司按月支付王能力伤残津贴8500元，直至王能力办理退休手续时止。上述赔偿款应于本判决书送达之日起七日内履行完毕
                                </li>
                                <li class="oneline">
                                    <strong>发布时间：</strong>
                                        2015年11月10日
                                </li>
                                <li class="oneline">
                                    <strong>执行依据文号：</strong>
                                        （2014）六民一终字第00758号民事判决书
                                </li>
                                <li class="oneline">
                                    <strong>作出执行依据单位：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>已履行：</strong>
                                            暂无
                                </li>
                                <li class="oneline">
                                    <strong>未履行：</strong>
                                            暂无
                                </li>
                        </ul>
                        <img src="/img/watermark.png" class="creditsearch-tagsinfo-img">
                        <ul class="creditsearch-tagsinfo-ul clearfix">
                                <li class="oneline">
                                    <strong>案号：</strong>
                                        (2015)霍法执字第00530号
                                </li>
                                <li class="oneline">
                                    <strong>省份：</strong>
                                        安徽
                                </li>
                                <li class="oneline">
                                    <strong>执行法院：</strong>
                                        霍邱县人民法院
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人具体情形：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>被执行人的履行情况：</strong>
                                        全部未履行
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人行为具体情形：</strong>
                                        其他有履行能力而拒不履行生效法律文书确定义务
                                </li>
                                <li class="oneline">
                                    <strong>法定代表人或者负责人姓名：</strong>
                                        吉少清
                                </li>
                                <li class="oneline">
                                    <strong>立案时间：</strong>
                                        20150706
                                </li>
                                <li class="oneline">
                                    <strong>做出执行依据单位：</strong>
                                        安徽省霍邱县人民法院
                                </li>
                                <li class="oneline">
                                    <strong>生效法律文书确定的义务：</strong>
                                        一、原告安徽大昌矿业集团有限公司一次性支付被告郑道平全部赔偿费用合计人民币36万元，郑道平再无其他赔偿要求。支付方式转账支付，协议签订后先支付10万元，2015年2月18日之前付10万元，剩余16万元在2015年6月之前付清。户名郑道平，开户行工商银行霍邱县经济开发区支行，账号6212261314002138810。二、双方劳动关系从本协议签订之日起解除，以后双方再无任何纠纷。三、今后郑道平不得再堵闹、妨碍安徽大昌矿业集团有限公司正常办公和生产经营，也不得以任何理由申请劳动仲裁或者起诉安徽大昌矿业集团有限公司，否则安徽大昌矿业集团有限公司有权单方解除本协议，之前郑道平已收（借）款项全部返还给安徽大昌矿业集团有限公司，因此产生的费用、损失等全部由郑道平承担。五、本协议一式三份，安徽大昌矿业集团有限公司2份，郑道平1份，双方签字后生效
                                </li>
                                <li class="oneline">
                                    <strong>发布时间：</strong>
                                        2015年11月10日
                                </li>
                                <li class="oneline">
                                    <strong>执行依据文号：</strong>
                                        （2014）霍民一初字第02297号民事调解书
                                </li>
                                <li class="oneline">
                                    <strong>作出执行依据单位：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>已履行：</strong>
                                            暂无
                                </li>
                                <li class="oneline">
                                    <strong>未履行：</strong>
                                            暂无
                                </li>
                        </ul>
                        <img src="/img/watermark.png" class="creditsearch-tagsinfo-img">
                        <ul class="creditsearch-tagsinfo-ul clearfix">
                                <li class="oneline">
                                    <strong>案号：</strong>
                                        (2014)常执字第00085号
                                </li>
                                <li class="oneline">
                                    <strong>省份：</strong>
                                        江苏
                                </li>
                                <li class="oneline">
                                    <strong>执行法院：</strong>
                                        江苏省常州市中级人民法院
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人具体情形：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>被执行人的履行情况：</strong>
                                        部分未履行
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人行为具体情形：</strong>
                                        其他有履行能力而拒不履行生效法律文书确定义务
                                </li>
                                <li class="oneline">
                                    <strong>法定代表人或者负责人姓名：</strong>
                                        吉少清
                                </li>
                                <li class="oneline">
                                    <strong>立案时间：</strong>
                                        20140219
                                </li>
                                <li class="oneline">
                                    <strong>做出执行依据单位：</strong>
                                        江苏省常州市中级人民法院
                                </li>
                                <li class="oneline">
                                    <strong>生效法律文书确定的义务：</strong>
                                        判决书确定的本金尚有809220元未支付，判决书确定的相应利息未支付。
                                </li>
                                <li class="oneline">
                                    <strong>发布时间：</strong>
                                        2015年09月22日
                                </li>
                                <li class="oneline">
                                    <strong>执行依据文号：</strong>
                                        (2013)常商初字第0240号
                                </li>
                                <li class="oneline">
                                    <strong>作出执行依据单位：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>已履行：</strong>
                                        已支付货款750万元。
                                </li>
                                <li class="oneline">
                                    <strong>未履行：</strong>
                                        判决书确定的本金尚有809220元未支付，判决书确定的相应利息未支付。
                                </li>
                        </ul>
                        <img src="/img/watermark.png" class="creditsearch-tagsinfo-img">
                        <ul class="creditsearch-tagsinfo-ul clearfix">
                                <li class="oneline">
                                    <strong>案号：</strong>
                                        (2015)霍法执字第00533号
                                </li>
                                <li class="oneline">
                                    <strong>省份：</strong>
                                        安徽
                                </li>
                                <li class="oneline">
                                    <strong>执行法院：</strong>
                                        霍邱县人民法院
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人具体情形：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>被执行人的履行情况：</strong>
                                        全部未履行
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人行为具体情形：</strong>
                                        其他有履行能力而拒不履行生效法律文书确定义务
                                </li>
                                <li class="oneline">
                                    <strong>法定代表人或者负责人姓名：</strong>
                                        吉少清
                                </li>
                                <li class="oneline">
                                    <strong>立案时间：</strong>
                                        20150706
                                </li>
                                <li class="oneline">
                                    <strong>做出执行依据单位：</strong>
                                        安徽省霍邱县人民法院
                                </li>
                                <li class="oneline">
                                    <strong>生效法律文书确定的义务：</strong>
                                        一、原告安徽大昌矿业集团有限公司一次性支付被告王明成全部赔偿费用合计人民币36万元，王明成再无其他赔偿要求。支付方式转账支付，协议签订后先支付10万元，2015年2月18日前付10万元，剩余16万元在2015年6月前付清。户名王明成，开户行工商银行霍邱县经济开发区支行，账号6212261314002476954。二、双方劳动关系从本协议签订之日起解除，以后双方再无任何纠纷。三、今后王明成不得再堵闹、妨碍安徽大昌矿业集团有限公司正常办公和生产经营，也不得以任何理由申请劳动仲裁或者起诉安徽大昌矿业集团有限公司，否则安徽大昌矿业集团有限公司有权单方解除本协议，之前王明成已收（借）款项全部返还给安徽大昌矿业集团有限公司。因此产生的费用、损失等全部由王明成承担。五、本协议一式三份，安徽大昌矿业集团有限公司2份，王明成1份，双方签字后生效。案件受理费10元免收
                                </li>
                                <li class="oneline">
                                    <strong>发布时间：</strong>
                                        2015年11月10日
                                </li>
                                <li class="oneline">
                                    <strong>执行依据文号：</strong>
                                        （2014）霍民一初字第02300号民事调解书
                                </li>
                                <li class="oneline">
                                    <strong>作出执行依据单位：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>已履行：</strong>
                                            暂无
                                </li>
                                <li class="oneline">
                                    <strong>未履行：</strong>
                                            暂无
                                </li>
                        </ul>
                        <img src="/img/watermark.png" class="creditsearch-tagsinfo-img">
                        <ul class="creditsearch-tagsinfo-ul clearfix">
                                <li class="oneline">
                                    <strong>案号：</strong>
                                        (2015)霍法执字第00532号
                                </li>
                                <li class="oneline">
                                    <strong>省份：</strong>
                                        安徽
                                </li>
                                <li class="oneline">
                                    <strong>执行法院：</strong>
                                        霍邱县人民法院
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人具体情形：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>被执行人的履行情况：</strong>
                                        全部未履行
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人行为具体情形：</strong>
                                        其他有履行能力而拒不履行生效法律文书确定义务
                                </li>
                                <li class="oneline">
                                    <strong>法定代表人或者负责人姓名：</strong>
                                        吉少清
                                </li>
                                <li class="oneline">
                                    <strong>立案时间：</strong>
                                        20150706
                                </li>
                                <li class="oneline">
                                    <strong>做出执行依据单位：</strong>
                                        安徽省霍邱县人民法院
                                </li>
                                <li class="oneline">
                                    <strong>生效法律文书确定的义务：</strong>
                                        一、原告安徽大昌矿业集团有限公司一次性支付被告杨忠发全部赔偿费用合计人民币36万元，杨忠发再无其他赔偿要求。支付方式转账支付，协议签订后先支付10万元，2015年2月18日前付10万元，剩余16万元在2015年6月前付清。户名杨忠发，开户行工商银行随州南郊支行，账号6212261805001847541。二、双方劳动关系从本协议签订之日起解除，以后双方再无任何纠纷。三、今后杨忠发不得再堵闹、妨碍安徽大昌矿业集团有限公司正常办公和生产经营，也不得以任何理由申请劳动仲裁或者起诉安徽大昌矿业集团有限公司，否则安徽大昌矿业集团有限公司有权单方解除本协议，之前杨忠发已收（借）款项全部返还给安徽大昌矿业集团有限公司。因此产生的费用、损失等全部由杨忠发承担。五、本协议一式三份，安徽大昌矿业集团有限公司2份，杨忠发1份，双方签字后生效
                                </li>
                                <li class="oneline">
                                    <strong>发布时间：</strong>
                                        2015年11月10日
                                </li>
                                <li class="oneline">
                                    <strong>执行依据文号：</strong>
                                        （2014）霍民一初字第02299号民事调解书
                                </li>
                                <li class="oneline">
                                    <strong>作出执行依据单位：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>已履行：</strong>
                                            暂无
                                </li>
                                <li class="oneline">
                                    <strong>未履行：</strong>
                                            暂无
                                </li>
                        </ul>
                        <img src="/img/watermark.png" class="creditsearch-tagsinfo-img">
                        <ul class="creditsearch-tagsinfo-ul clearfix">
                                <li class="oneline">
                                    <strong>案号：</strong>
                                        (2015)霍法执字第00531号
                                </li>
                                <li class="oneline">
                                    <strong>省份：</strong>
                                        安徽
                                </li>
                                <li class="oneline">
                                    <strong>执行法院：</strong>
                                        霍邱县人民法院
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人具体情形：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>被执行人的履行情况：</strong>
                                        全部未履行
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人行为具体情形：</strong>
                                        其他有履行能力而拒不履行生效法律文书确定义务
                                </li>
                                <li class="oneline">
                                    <strong>法定代表人或者负责人姓名：</strong>
                                        吉少清
                                </li>
                                <li class="oneline">
                                    <strong>立案时间：</strong>
                                        20150706
                                </li>
                                <li class="oneline">
                                    <strong>做出执行依据单位：</strong>
                                        安徽省霍邱县人民法院
                                </li>
                                <li class="oneline">
                                    <strong>生效法律文书确定的义务：</strong>
                                        一、原告安徽大昌矿业集团有限公司一次性支付被告陈定国全部赔偿费用合计人民币36万元，陈定国再无其他赔偿要求。支付方式转账支付，协议签订后先支付10万元，2015年2月18日之前付10万元，剩余16万元在2015年6月之前付清。户名陈定国，开户行工商银行安康紫阳县支行，账号6215582607000043238。二、双方劳动关系从本协议签订之日起解除，以后双方再无任何纠纷。三、今后陈定国不得再堵闹、妨碍安徽大昌矿业集团有限公司正常办公和生产经营，也不得以任何理由申请劳动仲裁或者起诉安徽大昌矿业集团有限公司，否则安徽大昌矿业集团有限公司有权单方解除本协议，之前陈定国已收（借）款项全部返还给安徽大昌矿业集团有限公司，因此产生的费用、损失等全部由陈定国承担。五、本协议一式三份，安徽大昌矿业集团有限公司2份，陈定国1份，双方签字后生效
                                </li>
                                <li class="oneline">
                                    <strong>发布时间：</strong>
                                        2015年11月10日
                                </li>
                                <li class="oneline">
                                    <strong>执行依据文号：</strong>
                                        （2014）霍民一初字第02301号民事调解书
                                </li>
                                <li class="oneline">
                                    <strong>作出执行依据单位：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>已履行：</strong>
                                            暂无
                                </li>
                                <li class="oneline">
                                    <strong>未履行：</strong>
                                            暂无
                                </li>
                        </ul>
                        <img src="/img/watermark.png" class="creditsearch-tagsinfo-img">
                        <ul class="creditsearch-tagsinfo-ul clearfix">
                                <li class="oneline">
                                    <strong>案号：</strong>
                                        (2015)霍法执字第00534号
                                </li>
                                <li class="oneline">
                                    <strong>省份：</strong>
                                        安徽
                                </li>
                                <li class="oneline">
                                    <strong>执行法院：</strong>
                                        霍邱县人民法院
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人具体情形：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>被执行人的履行情况：</strong>
                                        全部未履行
                                </li>
                                <li class="oneline">
                                    <strong>失信被执行人行为具体情形：</strong>
                                        其他有履行能力而拒不履行生效法律文书确定义务
                                </li>
                                <li class="oneline">
                                    <strong>法定代表人或者负责人姓名：</strong>
                                        吉少清
                                </li>
                                <li class="oneline">
                                    <strong>立案时间：</strong>
                                        20150706
                                </li>
                                <li class="oneline">
                                    <strong>做出执行依据单位：</strong>
                                        安徽省霍邱县人民法院
                                </li>
                                <li class="oneline">
                                    <strong>生效法律文书确定的义务：</strong>
                                        一、原告安徽大昌矿业集团有限公司一次性支付被告汪为炳全部赔偿费用合计人民币36万元，汪为炳再无其他赔偿要求。支付方式转账支付，协议签订后先支付10万元，2015年2月18日前付10万元，剩余16万元在2015年6月前付清。户名汪为炳，开户行工商银行安康紫阳县支行，账号6212261314002476814。二、双方劳动关系从本协议签订之日起解除，以后双方再无任何纠纷。三、今后汪为炳不得再堵闹安徽大昌矿业集团有限公司，妨碍公司正常办公和生产经营，也不得以任何理由申请劳动仲裁或者起诉安徽大昌矿业集团有限公司，否则安徽大昌矿业集团有限公司有权单方解除本协议，之前汪为炳已收（借）款项全部返还给安徽大昌矿业集团有限公司。因此产生的费用、损失等全部由汪为炳承担。四、本协议一式三份，安徽大昌矿业集团有限公司2份，汪为炳1份，双方签字后生效。案件受理费10元免收
                                </li>
                                <li class="oneline">
                                    <strong>发布时间：</strong>
                                        2015年11月10日
                                </li>
                                <li class="oneline">
                                    <strong>执行依据文号：</strong>
                                        （2014）霍民一初字第02293号民事调解书
                                </li>
                                <li class="oneline">
                                    <strong>作出执行依据单位：</strong>
                                        暂无
                                </li>
                                <li class="oneline">
                                    <strong>已履行：</strong>
                                            暂无
                                </li>
                                <li class="oneline">
                                    <strong>未履行：</strong>
                                            暂无
                                </li>
                        </ul>
                </div>
            </div>
        </div>
    </div>

    <script src="http://static.creditchina.gov.cn/plugins/esl.js"></script>
    <script src="http://static.creditchina.gov.cn/plugins/jquery-1.11.2.js"></script>
    <script>
        var wwwDomain = '';
        require.config({
            baseUrl: 'http://static.creditchina.gov.cn/'
        });
        require(['js/searchDetail'], function (searchDetail) {
            searchDetail.start();
        });

        function reload() {
            window.location.reload();
        }
    </script>    <div class="wrapper-push"></div>

    </div>
    <div class="mod-footer clear">

        <div class="footer-bg-image">
            <div class="container-top"></div>
        </div>
        <div class="container">
    	    <div class="container-bottom">
    	        <p>
    	            <span>©版权所有：信用中国</span> |&nbsp;<a href="/announcement">网站声明</a> |&nbsp;<a href="/about">关于我们</a>
    	        </p>
    	         <p>
    	            主办单位：国家信息中心&nbsp;  京ICP备05052393号-5
    	        </p>
    	        <p>指导单位： 国家发展和改革委员会&nbsp;&nbsp;&nbsp;中国人民银行&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;技术支持：北京百度网讯科技有限公司  &nbsp;</p>

    	    </div>
        </div>
    </div>
    </body>
    </html>
    """
    a = CreditChinaInfo(html.decode("utf8"))
    print a.info()