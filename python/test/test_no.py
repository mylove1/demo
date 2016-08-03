# coding:utf-8
import re
import urllib
import requests
import threading
#
a = '''

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
                <a href="/home"  class="nav-item nav-item-first  "><span>首页</span></a>
                <a href="/channel_news/1"   class="nav-item nav-item-sec "><span>信用动态</span></a>
                <a href="/channel_news/2"  class="nav-item nav-item-thd "><span>政策法规</span></a>
                <a href="/goDisciplinary"  class="nav-item nav-item-forth "><span>联合惩戒</span></a>
                <a href="/channel_news/0" class="nav-item nav-item-fifth "><span>信用服务</span></a>
                <a href="/channel_news/7"  class="nav-item nav-item-sixth "><span>信用研究</span></a>
                <a href="/channel_news/8"  class="nav-item nav-item-sevth "><span>信用知识</span></a>
                <a href="/toNavigation"  class="nav-item nav-item-eight "><span>信用导航</span></a>
                <!--
                <a href="/channel_news/14"  class="nav-item nav-item-eight ">互动话题</a>
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
            <h1>杭州远方光电信息股份有限公司</h1>
        </header>
        <ul class="creditsearch-tags clearfix">
            <li class="disabled">
                <a href="#csdetail1">基础信息</a>
            </li>
            <li >
                <a href="#csdetail2">优良记录（1）</a>
            </li>
            <li >
                <a href="#csdetail3">不良记录（1）</a>
            </li>
            <li class="disabled">
                <a href="#csdetail4">失信记录</a>
            </li>
            <li class="creditsearch-tags-time">
                <span>【查询时间：2016年08月03 14时38分】</span>
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
	                <li class="oneline"><strong>企业名称：</strong>杭州远方光电信息股份有限公司</li>
	                <li class="oneline"><strong>归属地域：</strong>浙江</li>
	                <li class="oneline"><strong>法人：</strong></li>
	                <li class="oneline"><strong>工商注册号：</strong>330108000006636</li>
	                <li class="oneline"><strong>注册资金：</strong>24000.000000 万(元)	                </li>
	                <li class="oneline"><strong>住所：</strong>杭州市滨江区滨康路669号1号楼</li>
	                <li class="oneline"><strong>成立日期：</strong>2003-05-21</li>
	                <li class="oneline"><strong>营业期限：</strong>
	                2003-05-21 至 无固定期限
	                </li>
	                <li class="oneline"><strong>经营范围：</strong>计算机软件、电流表、电压表、电功率表、功率因素表、光学标准灯、积分球、光探测器、亮度计、测色光谱光度计、照度计（专业袖珍照度计）、智能型多功能光度计（《污染物排放许可证》、《制造计量器具许可证》）。 计算机软件，电流表，电压表、电功率表、功率因素表、光学标准灯、积分球、光探测器、亮度计、测色光谱光度计、智能型多功能光度计、专业袖珍照度计的技术开发服务和销售，经营进出口业务。</li>
	                <li class="oneline"><strong>审核日期：</strong>2015-06-16</li>
	                <!-- 企业的基本信息,个人没有该信息 -->
                </ul>
            </div>

            <header>
                <h1 class="clearfix" id="csdetail2">
                    优良记录
                    <small>收起>></small>
                </h1>
            </header>
            <div class="creditsearch-tagsinfo">
                        <img src="/img/watermark.png" class="creditsearch-tagsinfo-img">
                        <ul class="creditsearch-tagsinfo-ul clearfix">
                                <li class="oneline">
                                    <strong>纳税人识别号：</strong>
                                        330107749475817
                                </li>
                                <li class="oneline">
                                    <strong>创建时间：</strong>
                                        2016-01-05
                                </li>
                                <li class="oneline">
                                    <strong>纳税人名称：</strong>
                                        杭州远方光电信息股份有限公司
                                </li>
                                <li class="oneline">
                                    <strong>纳税信用评级结果：</strong>
                                        A
                                </li>
                                <li class="oneline">
                                    <strong>评价年度：</strong>
                                        2014
                                </li>
                                <li class="oneline">
                                    <strong>主管税务机关：</strong>
                                        浙江省国家税务局、地方税务局
                                </li>
                                <li class="oneline">
                                    <strong>所属地域：</strong>
                                        浙江省
                                </li>
                        </ul>
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
                                    <strong>供应商或代理机构名称：</strong>
                                        杭州远方光电信息股份有限公司
                                </li>
                                <li class="oneline">
                                    <strong>地址：</strong>
                                        杭州市滨江区滨康路669号
                                </li>
                                <li class="oneline">
                                    <strong>不良行为的具体情形：</strong>
                                        与其他供应商恶意串通。
                                </li>
                                <li class="oneline">
                                    <strong>处罚结果：</strong>
                                        列入不良行为记录名单，三年内禁止参加济宁市辖区内政府采购活动；处以6万元人民币罚款。
                                </li>
                                <li class="oneline">
                                    <strong>处罚依据：</strong>
                                        《中华人民共和国政府采购法》第七十七条
                                </li>
                                <li class="oneline">
                                    <strong>处罚（记录）日期：</strong>
                                        2015/01/30 17:13:37.000
                                </li>
                                <li class="oneline">
                                    <strong>执法（记录）单位：</strong>
                                        济宁市财政局
                                </li>
                                <li class="oneline">
                                    <strong>处罚结束时间：</strong>
                                        2015/07/15 00:00:00.000
                                </li>
                                <li class="oneline">
                                    <strong>工商登记号：</strong>
                                        330108000006636
                                </li>
                                <li class="oneline">
                                    <strong>归属地域：</strong>
                                        浙江
                                </li>
                        </ul>
            </div>

            <header>
                <h1 class="clearfix" id="csdetail4">
                    失信记录
                    <small>展开>></small>
                </h1>
            </header>
            <div class="creditsearch-tagsinfo hidden">
                <p class="text-info">平台未收录该企业的失信记录。</p>
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
'''
a = ''.join(a.split())
print 'start'
# rea = re.compile('<ulclass="creditsearch-tagsinfo-ul"><liclass="oneline"><strong>企业名称：</strong>(.*?)</li><liclass="oneline"><strong>归属地域：</strong>(.*?)</li><liclass="oneline"><strong>法人：</strong></li><liclass="oneline"><strong>工商注册号：</strong>(.*?)</li><liclass="oneline"><strong>注册资金：</strong>(.*?)万\(元\)</li><liclass="oneline"><strong>住所：</strong>(.*?)</li><liclass="oneline"><strong>成立日期：</strong>(.*?)</li><liclass="oneline"><strong>营业期限：</strong>(.*?)</li><liclass="oneline"><strong>经营范围：</strong>(.*?)</li><liclass="oneline"><strong>审核日期：</strong>(.*?)</li>')
# rea =   re.compile('<ulclass="creditsearch-tagsinfo-ul"><liclass="oneline"><strong>企业名称：</strong>(.*?)</li><liclass="oneline"><strong>归属地域：</strong>(.*?)</li><liclass="oneline"><strong>法人：</strong></li><liclass="oneline"><strong>工商注册号：</strong>(.*?)</li><liclass="oneline"><strong>注册资金：</strong>(.*?)万\(元\)</li><liclass="oneline"><strong>住所：</strong>(.*?)</li><liclass="oneline"><strong>成立日期：</strong>(.*?)</li>')
# 失信记录
reb = re.compile('class="creditsearch-tagsinfo-ulclearfix"><liclass="oneline"><strong>企业名称：</strong>(.*?)</li><liclass="oneline"><strong>组织机构代码：</strong>(.*?)</li><liclass="oneline"><strong>案号：</strong>(.*?)</li><liclass="oneline"><strong>省份：</strong>(.*?)</li><liclass="oneline"><strong>法人：</strong>(.*?)</li><liclass="oneline"><strong>执行法院：</strong>(.*?)</li><liclass="oneline"><strong>失信被执行人具体情形：</strong>(.*?)</li><liclass="oneline"><strong>被执行人的履行情况：</strong>(.*?)</li><liclass="oneline"><strong>失信被执行人行为具体情形：</strong>(.*?)</li><liclass="oneline"><strong>法定代表人或者负责人姓名：</strong>(.*?)</li><liclass="oneline"><strong>立案时间：</strong>(.*?)</li><liclass="oneline"><strong>做出执行依据单位：</strong>(.*?)</li><liclass="oneline"><strong>生效法律文书确定的义务：</strong>(.*?)</li><liclass="oneline"><strong>发布时间：</strong>(.*?)</li><liclass="oneline"><strong>执行依据文号：</strong>(.*?)</li><liclass="oneline"><strong>作出执行依据单位：</strong>(.*?)</li><liclass="oneline"><strong>已履行：</strong>(.*?)</li><liclass="oneline"><strong>未履行：</strong>(.*?)</li>')
# 不良记录
rec = re.compile('class="creditsearch-tagsinfo-ul"><liclass="oneline"><strong>供应商或代理机构名称：</strong>(.*?)</li><liclass="oneline"><strong>地址：</strong>(.*?)</li><liclass="oneline"><strong>不良行为的具体情形：</strong>(.*?)</li><liclass="oneline"><strong>处罚结果：</strong>(.*?)</li><liclass="oneline"><strong>处罚依据：</strong>(.*?)</li><liclass="oneline"><strong>处罚（记录）日期：</strong>(.*?)</li><liclass="oneline"><strong>执法（记录）单位：</strong>(.*?)</li><liclass="oneline"><strong>处罚结束时间：</strong>(.*?)</li><liclass="oneline"><strong>工商登记号：</strong>(.*?)</li><liclass="oneline"><strong>归属地域：</strong>(.*?)</li>')
b = rec.findall(a)
for x in b:
    for y in x:
        print y
