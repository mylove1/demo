# coding:utf-8
from lxml import etree
import requests

# r = requests.get('http://www.xizhi.com/search?wd=上海快大生物工程在在在要一中')
# a = '''<!DOCTYPE html>
# <html lang="zh-CN">
# <head>
# <meta charset="utf-8">
# <meta http-equiv="X-UA-Compatible" content="IE=edge">
# <meta name="viewport" content="width=device-width, initial-scale=1">
# <meta name="Keywords" content="米扑代理,代理,米扑科技,MIMVP,HTTP代理,IP代理,代理IP,免费代理,free proxy,代理服务器,proxy server,高匿代理,匿名代理,HTTP,HTTPS,SOCKS4,SOCKS5,QQ代理">
# <meta name="Description" content="米扑代理,每天提供大量免费http代理,https代理,Socks代理,高匿代理,匿名代理,满足您对代理高可用性,高稳定性的需求。">
# <meta name="author" content="mimvp">
# <link rel="icon" href="favicon.ico">
#
# <title>免费代理 - 米扑代理</title>
#
# <!-- Bootstrap core CSS -->
# <link href="css/bootstrap.min.css" rel="stylesheet">
#
# <!-- Custom styles for this template -->
# <link href="blog/blog.css" rel="stylesheet">
#
# <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
# <!--[if lt IE 9]><script src="../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
# <!--<script src="assets/js/ie-emulation-modes-warning.js"></script>-->
#
# <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
# <!--[if lt IE 9]>
#       <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
#       <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
#     <![endif]-->
#
# <style type="text/css">
#
# a {
# 	color: #228B22;
# 	text-decoration: none;
# }
#
# a:hover {
# 	color: #228B22;
# 	text-decoration: none;
# }
#
# .proxy_use_bg {
# 	background: #eee;
# 	border-bottom: 1px solid #ddd;
# 	margin-top: 40px;
# }
#
# .proxy_use {
# 	padding-top: 20px;
# 	padding-bottom: 10px;
# 	width: 970px;
# 	padding-right: 15px;
# 	padding-left: 15px;
# 	margin-right: auto;
# 	margin-left: auto;
# }
#
# .content_body {
#
# }
#
# .tag_area {
# 	margin: 10px 0 0px 0;
# }
#
# .tag_area .label.active, .tag_area .label.active:hover {
# 	background-color: #228B22;
# }
#
# .tag_area .label {
# 	background-color: #c1c1bf;
# 	background-color: #999999;
# 	text-decoration: none;
# 	font-size: 13px;
# }
#
# .tag_area a {
# 	padding: 8px 8px 8px 8px;
# }
#
# .label {
# 	display: inline-block;
# 	padding: 2px 4px 2px 4px;
# 	font-size: 11px;
# 	font-weight: bold;
# 	line-height: 15px;
# 	color: #fff;
# 	vertical-align: middle;
# 	white-space: nowrap;
# 	text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
# 	background-color: #999;
# 	-webkit-border-radius: 3px;
# 	-moz-border-radius: 3px;
# 	border-radius: 3px;
# 	margin-right: 10px;
# 	margin-bottom: 3px;
# }
#
# .buy {
# 	font-size: 16px;
# 	float: right;
# }
#
# #listnav {
# 	margin: 20px 0 30px 0;
# }
#
# #listnav ul {
# 	text-align: center;
# 	border: solid;
# 	border-width: 0;
# 	padding: 2px 0 0 0;
# }
#
# #listnav li {
# 	display: inline;
# 	padding: 0 0 0 10px;
# 	list-style: none;
# 	border: 1px;
# }
#
# #listnav a {
# 	color: #9d9d9d;
# 	text-decoration: none;
# 	padding: 4px 6px;
# 	border: 1px solid #dfdfdf;
# 	border-radius: 3px;
# }
#
# #listnav a:hover {
# 	color: #9d9d9d;
# 	background: #e5f3f6;
# 	border: 1px solid #49afcd;
# }
#
# #listnav a.active {
# 	color: #fff;
# 	background: #49afcd;
# 	border: 1px solid #49afcd;
# }
#
# #proxy_footer_desc {
# 	padding-left: 10px;
# }
#
# #proxy_footer_desc p a {
# 	color: #428bca;
# 	text-decoration: none;
# }
#
# #proxy_footer_desc p a:hover {
# 	color: #FF8C00;
# 	text-decoration: none;
# }
#
# #proxy_footer_desc p a:visited {
# 	color: #428bca;
# }
#
# .center {
# /* 	width: 100%; */
# 	text-align: center;
# }
#
# .btn {
# 	margin-left: 45%;
# 	margin-top: 10px;
# 	padding: 6px 12px;
# 	font-size: 14px;
# 	font-weight: 400;
# 	line-height: 1.42857143;
# 	text-align: center;
# 	white-space: nowrap;
# 	vertical-align: middle;
# 	cursor: pointer;
# 	user-select: none;
# 	background-image: none;
# 	border: 1px solid transparent;
# 	border-radius: 4px;
# }
#
# .btn a {
# 	height: 36px;
# 	line-height: 36px;
# 	padding: 0 11px;
# 	font-size: 18px;
# 	font-weight: bold;
# 	color: white;
# 	display: inline-block;
# 	text-decoration: none;
# 	background: #228B22;
# 	border-radius: 4px;
# }
#
# .btn a:hover {
# 	background: #006400;
# }
#
# /*
# a {
# color: #428bca;
# text-decoration: none;
# }
#
# a:active, a:hover {
# outline: 0;
# color: #228B22;
# text-decoration: none;
# }
# */
# .time_bgcolor {
# 	width: 100%;
# 	position: relative;
# 	background-color: #CCCCCC;
# }
#
# .bar_time_bgcolor {
# 	width: 53%;
# 	background-color: #ffd700;
# }
#
# .time_bgcolor .bar_time_bgcolor {
# 	display: block;
# 	position: relative;
# 	height: 15px;
# }
#
# .time_bgcolor .bar_time_bgcolor span {
# 	position: absolute;
# 	left: 1em;
# }
#
#
# * {
# 		padding:0;
# 		margin:0;
# 	}
# 	#navigation, #navigation li ul {
# 		list-style-type:none;
# 	}
# 	#navigation li {
# 		float:left;
# 		text-align:center;
# 		position:relative;
# 	}
# 	#navigation li a:link, #navigation li a:visited {
# 		display:block;
# 		text-decoration:none;
# 		width:120px;
# 		background:#375069;
# 		padding-left:10px;
# 	}
# 	#navigation li a:hover {
# 		color:#fff;
# 		background:#2687eb;
# 	}
# 	#navigation li ul li a:hover {
# 		color:#fff;
# 		background:#6b839c;
# 	}
# 	#navigation li ul {
# 		display:none;
# 		position:absolute;
# 		top:40px;
# 		left:0;
# 		margin-top:1px;
# 		width:120px;
# 	}
# 	#navigation li ul li ul {
# 		display:none;
# 		position:absolute;
# 		top:0px;
# 		left:130px;
# 		margin-top:0;
# 		margin-left:1px;
# 		width:120px;
# 	}
# </style>
#
# 	<script type="text/javascript">
# 		function displaySubMenu(li) {
# 			var subMenu = li.getElementsByTagName("ul")[0];
# 			if(subMenu) subMenu.style.display = "block";
# 		}
#
# 		function hideSubMenu(li) {
# 			var subMenu = li.getElementsByTagName("ul")[0];
# 			if(subMenu) subMenu.style.display = "none";
# 		}
# 	</script>
#
# </head>
#
# <body oncontextmenu="return false" onselectstart="return false">
#
# 	<div class="blog-masthead navbar-fixed-top" role="navigation">
# 		<div class="container">
# 			<nav class="blog-nav">
# 				<div class="nav-logo">
# 					<a href="index.php"><img alt="ithomer-logo" src="img/logo.png"></a>
# 				</div>
# 				<div class="nav-title">
# 					<ul id="navigation">
# 						<li onmouseover="displaySubMenu(this)" onmouseout="hideSubMenu(this)">
# 							<a class="blog-nav-item" href="index.php">首页</a>
# 						</li>
# 						<li onmouseover="displaySubMenu(this)" onmouseout="hideSubMenu(this)">
# 							<a class="blog-nav-item active" href="free.php">免费代理</a>
# 						</li>
# 						<li onmouseover="displaySubMenu(this)" onmouseout="hideSubMenu(this)">
# 							<a class="blog-nav-item" href="./price.php">购买代理</a>
# 						</li>
# 						<li onmouseover="displaySubMenu(this)" onmouseout="hideSubMenu(this)">
# 							<a class="blog-nav-item" href="fetch.php">提取代理</a>
# 						</li>
#
# 						<li onmouseover="displaySubMenu(this)" onmouseout="hideSubMenu(this)">
# 							<a class="blog-nav-item" href="stat.php">统计代理</a>
# 							<ul>
# 								<a class="blog-nav-item" href="check.php">检测代理</a>
# 								<a class="blog-nav-item" href="exist.php">检测收录</a>
# 								<a class="blog-nav-item" href="apidoc.php">API 接口</a>
# 								<a class="blog-nav-item" href="demo.php">使用示例</a>
# 								<a class="blog-nav-item" href="help.php">帮助文档</a>
# 							</ul>
# 						</li>
#
# 						<li onmouseover="displaySubMenu(this)" onmouseout="hideSubMenu(this)">
# 							<a class="blog-nav-item" href="usercenter/userinfo.php">会员中心</a>
# 							<ul>
# 								<a class="blog-nav-item" href="usercenter/login.php">用户登陆</a>
# 								<a class="blog-nav-item" href="usercenter/regist.php">用户注册</a>
#
# 							</ul>
# 						</li>
#
# 						<li onmouseover="displaySubMenu(this)" onmouseout="hideSubMenu(this)">
# 							<a class="blog-nav-item" href="about.php">关于我们</a>
# 							<ul>
# 								<a class="blog-nav-item" href="private.php">隐私保护</a>
# 								<a class="blog-nav-item" target="_blank" href="http://domain.mimvp.com/">米扑域名</a>
# 								<a class="blog-nav-item" target="_blank" href="http://money.mimvp.com/">米扑财富</a>
# 								<a class="blog-nav-item" target="_blank" href="http://blog.mimvp.com/">米扑博客</a>
# 								<a class="blog-nav-item" target="_blank" href="http://forum.mimvp.com/">米扑论坛</a>
# 							</ul>
# 						</li>
# 					</ul>
# 				</div>
#
# 				<div class="nav-clear"></div>
# 			</nav>
# 		</div>
# <!--
# 		<div class="bdsharebuttonbox" style="float: right;">
# 			<a href="#" class="bds_more" data-cmd="more"></a>
# 			<a href="#" class="bds_weixin" data-cmd="weixin" title="分享到微信"></a>
# 			<a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博"></a>
# 			<a href="#" class="bds_qzone" data-cmd="qzone" title="分享到QQ空间"></a>
# 			<a href="#" class="bds_tqq" data-cmd="tqq" title="分享到腾讯微博"></a>
# 			<a href="#" class="bds_renren" data-cmd="renren" title="分享到人人网"></a>
# 		</div>
# 		<script>window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"1","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"16"},"share":{}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>
# -->
# 	</div>
#
# 	<div class="proxy_use_bg">
# 		<div class="proxy_use">
# 			<div class="tag_area">
# 				<a id="tag_inner_ta" class="label" href="free.php?proxy=in_tp">Http国内普通</a>
# 				<a id="tag_inner_ha" class="label" href="free.php?proxy=in_hp">Http国内高匿</a>
# 				<a id="tag_outer_ta" class="label" href="free.php?proxy=out_tp">Http国外普通</a>
# 				<a id="tag_outer_ha" class="label" href="free.php?proxy=out_hp">Http国外高匿</a>
# 				<a id="tag_inner_socks" class="label" href="free.php?proxy=in_socks">Socks国内</a>
# 				<a id="tag_outer_socks" class="label" href="free.php?proxy=out_socks">Socks国外</a>
# 				<!--
# 				<a id="tag_qq" class="label" href="free.php?proxy=qq">QQ代理</a>
# 				<a id="tag_msn" class="label" href="free.php?proxy=msn">MSN代理</a>
# 				-->
#
# 				<span style="font-size: 20px; font-weight: bold; color: #ff0000; float: right;">
# 					<font size="3" color="#0000ff" >可用代理数：</font>
# 					19713				</span>
# 			</div>
# 		</div>
# 	</div>
#
# 	<div class="container">
# 		<div class="content_body">
#
#
# 			<div id="list" style="margin-top: 15px;">
# 				<table class="table table-bordered table-striped"
# 					style="table-layout: fixed;">
#
#
# 		        <thead style="background-color: #CEC1DA;">
# 			        <tr>
# 				        <th style="width: 60px;text-align: center;" id="p_id">ID</th>
# 				        <th style="width: 140px;" id="p_ip">IP地址</th>
# 				        <th style="width: 60px;" id="p_port">端口</th>
# 				        <th style="width: 100px;text-align: center;" id="p_type">类型</th>
# 				        <th style="width: 65px;" id="p_anonymous">匿名度</th>
# 				        <th style="width: 130px;" id="p_country">国家(省市)</th>
# 				        <th style="width: 65px;" id="p_isp">运营商</th>
# 			            <th style="width:100px;text-align: center;" id="p_ping">响应时间</th>
# 			            <th style="width:100px;text-align: center;" id="p_transfer">传输速度</th>
# 			            <th style="width:150px;text-align: center;" id="p_checkdtime">验证日期</th>
# 			        </tr>
# 		        </thead>
# 	        <tbody><td style='text-align: center; color:blue;'>1</td><td>120.52.72.54</td><td><img src=common/ygrandimg.php?id=1&port=MmDicm4vMpAO0OO0O /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>欺骗</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>北京</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='联通'>联通</td><td title='999999秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:10%; background-color:#CC3300;"></span></div></td><td title='0.092361秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:93.8426%; background-color:#008000;"></span></div></td><td style='text-align: center;'>2016-07-07 14:54</td></tr><td style='text-align: center; color:blue;'>2</td><td>113.107.57.76</td><td><img src=common/ygrandimg.php?id=2&port=MmDicm4vMpAO0OO0O /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>透明</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>广东</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='电信'>电信</td><td title='0.043461秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:91.3078%; background-color:#008000;"></span></div></td><td title='0.408079秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:76.912028571429%; background-color:#32CD32;"></span></div></td><td style='text-align: center;'>2016-07-07 14:50</td></tr><td style='text-align: center; color:blue;'>3</td><td>163.142.175.187</td><td><img src=common/ygrandimg.php?id=3&port=MmDicm4vMpDgw /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>欺骗</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>广东</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='联通'>联通</td><td title='0.041883秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:91.6234%; background-color:#008000;"></span></div></td><td title='2.992572秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:50.03714%; background-color:#FFD700;"></span></div></td><td style='text-align: center;'>2016-07-07 14:46</td></tr><td style='text-align: center; color:blue;'>4</td><td>219.145.244.250</td><td><img src=common/ygrandimg.php?id=4&port=MmDicmzvMpTI4 /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>透明</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>陕西</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='电信'>电信</td><td title='0.03252秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:93.496%; background-color:#008000;"></span></div></td><td title='9.74676秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:21.01296%; background-color:#FF8C00;"></span></div></td><td style='text-align: center;'>2016-07-07 14:44</td></tr><td style='text-align: center; color:blue;'>5</td><td>111.11.80.163</td><td><img src=common/ygrandimg.php?id=5&port=MmDicm4vMpAO0OO0O /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>欺骗</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>河北</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='移动'>移动</td><td title='0.013535秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:97.293%; background-color:#008000;"></span></div></td><td title='0.088766秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:94.082266666667%; background-color:#008000;"></span></div></td><td style='text-align: center;'>2016-07-07 14:41</td></tr><td style='text-align: center; color:blue;'>6</td><td>117.169.4.139</td><td><img src=common/ygrandimg.php?id=6&port=MmDicm4vMpAO0OO0O /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>欺骗</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>江西</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='移动'>移动</td><td title='0.035364秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:92.9272%; background-color:#008000;"></span></div></td><td title='0.197146秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:86.856933333333%; background-color:#008000;"></span></div></td><td style='text-align: center;'>2016-07-07 14:38</td></tr><td style='text-align: center; color:blue;'>7</td><td>119.6.238.49</td><td><img src=common/ygrandimg.php?id=7&port=MmDicm4vMpAO0OO0O /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>透明</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>四川</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='联通'>联通</td><td title='0.037123秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:92.5754%; background-color:#008000;"></span></div></td><td title='0.667778秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:69.492057142857%; background-color:#32CD32;"></span></div></td><td style='text-align: center;'>2016-07-07 14:36</td></tr><td style='text-align: center; color:blue;'>8</td><td>60.249.4.1</td><td><img src=common/ygrandimg.php?id=8&port=MmDicm4vMpDAw /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>欺骗</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>台湾</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='中华电信'>中华电信</td><td title='0.068351秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:86.3298%; background-color:#008000;"></span></div></td><td title='8.203694秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:27.185224%; background-color:#FF8C00;"></span></div></td><td style='text-align: center;'>2016-07-07 14:36</td></tr><td style='text-align: center; color:blue;'>9</td><td>120.52.72.56</td><td><img src=common/ygrandimg.php?id=9&port=MmDicm4vMpAO0OO0O /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>欺骗</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>北京</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='联通'>联通</td><td title='999999秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:10%; background-color:#CC3300;"></span></div></td><td title='0.015158秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:98.989466666667%; background-color:#008000;"></span></div></td><td style='text-align: center;'>2016-07-07 14:35</td></tr><td style='text-align: center; color:blue;'>10</td><td>27.187.223.211</td><td><img src=common/ygrandimg.php?id=10&port=MmDicmzvMpTI4 /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>透明</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>河北</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='电信'>电信</td><td title='0.01751秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:96.498%; background-color:#008000;"></span></div></td><td title='5.462647秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:38.149412%; background-color:#FF8C00;"></span></div></td><td style='text-align: center;'>2016-07-07 14:34</td></tr><td style='text-align: center; color:blue;'>11</td><td>117.169.4.133</td><td><img src=common/ygrandimg.php?id=11&port=MmDicm4vMpAO0OO0O /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>欺骗</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>江西</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='移动'>移动</td><td title='0.037992秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:92.4016%; background-color:#008000;"></span></div></td><td title='0.194519秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:87.032066666667%; background-color:#008000;"></span></div></td><td style='text-align: center;'>2016-07-07 14:31</td></tr><td style='text-align: center; color:blue;'>12</td><td>113.111.144.204</td><td><img src=common/ygrandimg.php?id=12&port=MmDicm5vNpzk3 /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>欺骗</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>广东</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='电信'>电信</td><td title='0.039624秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:92.0752%; background-color:#008000;"></span></div></td><td title='7.060165秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:31.75934%; background-color:#FF8C00;"></span></div></td><td style='text-align: center;'>2016-07-07 14:31</td></tr><td style='text-align: center; color:blue;'>13</td><td>118.193.84.42</td><td><img src=common/ygrandimg.php?id=13&port=MmDicmzvMpTI4 /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>透明</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>香港</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='null'>null</td><td title='0.06449秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:87.102%; background-color:#008000;"></span></div></td><td title='5.688557秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:37.245772%; background-color:#FF8C00;"></span></div></td><td style='text-align: center;'>2016-07-07 14:29</td></tr><td style='text-align: center; color:blue;'>14</td><td>115.159.90.206</td><td><img src=common/ygrandimg.php?id=14&port=MmDicm4vMpDg4 /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>欺骗</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>上海</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='腾讯集团'>腾讯集团</td><td title='0.026438秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:94.7124%; background-color:#008000;"></span></div></td><td title='4.08551秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:44.57245%; background-color:#FFD700;"></span></div></td><td style='text-align: center;'>2016-07-07 14:20</td></tr><td style='text-align: center; color:blue;'>15</td><td>1.172.95.98</td><td><img src=common/ygrandimg.php?id=15&port=MmDicm4vMpDgw /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>欺骗</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>台湾</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='中华电信'>中华电信</td><td title='999999秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:10%; background-color:#CC3300;"></span></div></td><td title='3.518189秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:47.409055%; background-color:#FFD700;"></span></div></td><td style='text-align: center;'>2016-07-07 14:19</td></tr><td style='text-align: center; color:blue;'>16</td><td>120.52.72.21</td><td><img src=common/ygrandimg.php?id=16&port=MmDicm4vMpAO0OO0O /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>欺骗</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>北京</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='联通'>联通</td><td title='999999秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:10%; background-color:#CC3300;"></span></div></td><td title='0.007009秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:99.532733333333%; background-color:#008000;"></span></div></td><td style='text-align: center;'>2016-07-07 14:19</td></tr><td style='text-align: center; color:blue;'>17</td><td>120.52.72.52</td><td><img src=common/ygrandimg.php?id=17&port=MmDicm4vMpAO0OO0O /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>欺骗</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>北京</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='联通'>联通</td><td title='999999秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:10%; background-color:#CC3300;"></span></div></td><td title='0.08213秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:94.524666666667%; background-color:#008000;"></span></div></td><td style='text-align: center;'>2016-07-07 14:19</td></tr><td style='text-align: center; color:blue;'>18</td><td>60.250.81.118</td><td><img src=common/ygrandimg.php?id=18&port=MmDicm4vMpAO0OO0O /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>透明</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>台湾</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='中华电信'>中华电信</td><td title='0.068831秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:86.2338%; background-color:#008000;"></span></div></td><td title='6.820873秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:32.716508%; background-color:#FF8C00;"></span></div></td><td style='text-align: center;'>2016-07-07 14:18</td></tr><td style='text-align: center; color:blue;'>19</td><td>120.194.18.90</td><td><img src=common/ygrandimg.php?id=19&port=MmDicm4vMpQO0OO0O /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>欺骗</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>河南</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='移动'>移动</td><td title='0.027863秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:94.4274%; background-color:#008000;"></span></div></td><td title='0.229519秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:84.698733333333%; background-color:#008000;"></span></div></td><td style='text-align: center;'>2016-07-07 14:18</td></tr><td style='text-align: center; color:blue;'>20</td><td>222.161.209.168</td><td><img src=common/ygrandimg.php?id=20&port=MmDicm4vMpTAy /></td><td style='text-align: center;white-space:nowrap;overflow:hidden;' title='HTTP'>HTTP</td><td style='text-align: center;'>欺骗</td><td><img src='img/flags/cn.png' alt='cn.png'> 中国 (<font color='blue'>吉林</font>)</td><td style='white-space:nowrap;overflow:hidden;' title='联通'>联通</td><td title='0.022993秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:95.4014%; background-color:#008000;"></span></div></td><td title='0.094639秒'><div class='time_bgcolor'><span class="bar_time_bgcolor" style="width:93.690733333333%; background-color:#008000;"></span></div></td><td style='text-align: center;'>2016-07-07 14:17</td></tr>
# 		        </tbody>
# 				</table>
# 				<div id="proxy_footer_desc">
# 				    <p>注： 游客和免费用户，只能查看第一页IP地址；会员用户可以查看全部翻页IP地址，并享有更多专属服务，购买<a target="_blank" href="price.php"><b>会员</b></a>。</p>
# 				</div>
#
# 				<div id="listnav">
#     				<ul>
#     					<li>第</li>
#
#     					<li><a href='./free.php?proxy=in_tp&amp;sort=&amp;pageindex=1'  class='active'>1</a></li><li><a href='./free.php?proxy=in_tp&amp;sort=&amp;pageindex=2'>2</a></li><li><a href='./free.php?proxy=in_tp&amp;sort=&amp;pageindex=3'>3</a></li><li><a href='./free.php?proxy=in_tp&amp;sort=&amp;pageindex=4'>4</a></li><li><a href='./free.php?proxy=in_tp&amp;sort=&amp;pageindex=5'>5</a></li><li>...</li><li><a href='./free.php?proxy=in_tp&amp;sort=&amp;pageindex=36'>36</a></li>
#     					<li>页</li>
#     				</ul>
#     			</div>
#
#
#
# 				<div class="btn center">
# 					<a id="tobuy" href="price.php" target="_blank">购买更多代理</a>
# 				</div>
# 			</div>
# 		</div>
#
# 	</div>
#
#
# 	<!-- /.container -->
#
#
# 	<!-- linezing tongji -->
# <!--
# 	<script type="text/javascript" src="http://js.tongji.linezing.com/3509932/tongji.js"></script>
# -->
#
# 	<div class="blog-footer">
# 		<div style="float: left;  margin-left: 38%;">
# 			<div class="allright">
# 				© 2009 - 2016 All Rights by <a target="_blank" href="http://mimvp.com" style="color:#999;">mimvp.com</a>
# 			</div>
# 			<div class="ks" id="ks">
# 				京ICP备 <a target="_blank" href="http://www.beianbeian.com/search/mimvp.com" style="color:#999;">14011308号</a>
# 			</div>
# 		</div>
# 		<div class="icon" style="float: right; margin-right: 30px;">
#            <a href="http://webscan.360.cn/index/checkwebsite?url=proxy.mimvp.com" target="_blank" title="360安全认证">
#            		<img width="106" height="40" src="img/secure-webscan.png" alt="360安全认证">
#            </a>
#            &nbsp;&nbsp;&nbsp;&nbsp;
#            <a href="http://zhanzhang.anquan.org/physical/report/?domain=proxy.mimvp.com" target="_blank" title="安全联盟认证">
#            		<img width="106" height="40" src="img/secure-zhanzhang.png" alt="安全联盟认证">
#            </a>
#         </div>
#         <div style="clear: both;"></div>
# 	</div>
#
# 	<!-- baidu tongji -->
# <!--
#    	<script>var _hmt = _hmt || [];(function() {var hm = document.createElement("script");hm.src = "//hm.baidu.com/hm.js?51e3cc975b346e7705d8c255164036b3";var s = document.getElementsByTagName("script")[0];s.parentNode.insertBefore(hm, s);})();</script>
# -->
#
# 	<a href="#top" id="top_btn" class="label btt"
# 		style="display: block; position: fixed; bottom: 80px; right: 10px; opacity: 0.5; background-color: #49afcd; padding: 10px; visibility: hidden;">^
# 	</a>
#
# 	<!-- Bootstrap core JavaScript
#     ================================================== -->
# 	<!-- Placed at the end of the document so the pages load faster -->
# 	<script src="js/jquery.min.js"></script>
# 	<script src="js/bootstrap.min.js"></script>
#
#
# 	<script type="text/javascript">
#
# 		function jumpToAnchor(id){
# 		    if($('#'+id).length > 0){
# 		        var jump_to = $('#'+id).offset();
# 		        window.scrollTo(jump_to.left, jump_to.top);
# 		    }
# 		}
#
# 		if (!Array.prototype.indexOf) {
# 		  Array.prototype.indexOf = function(elt /*, from*/)
# 		  {
# 		    var len = this.length >>> 0;
# 		    var from = Number(arguments[1]) || 0;
# 		    from = (from < 0)
# 		         ? Math.ceil(from)
# 		         : Math.floor(from);
# 		    if (from < 0)
# 		      from += len;
# 		    for (; from < len; from++)
# 		    {
# 		      if (from in this &&
# 		          this[from] === elt)
# 		        return from;
# 		    }
# 		    return -1;
# 		  };
# 		}
#
# 		$(document).ready(function() {
#
# 			if(window.location.pathname.indexOf("?") != -1)
# 		        jumpToAnchor("freelist");
#
# 			var href_params = window.location.href;
# 			var ptag = "#p1";
# 			if(href_params.indexOf("?") <= 0){
# 				$("#tag_inner_ta").addClass("active");
# 			} else {
# 				var proxy = href_params.split("proxy=")[1].split("&sort=")[0];
# 				if(proxy == "in_tp") {
# 					$("#tag_inner_ta").addClass("active");
# 				}
# 				else if(proxy == "in_hp") {
# 					$("#tag_inner_ha").addClass("active");
# 				}
# 				else if(proxy == "out_tp") {
# 					$("#tag_outer_ta").addClass("active");
# 				}
# 				else if(proxy == "out_hp") {
# 					$("#tag_outer_ha").addClass("active");
# 				}
# 				else if(proxy == "in_socks") {
# 					$("#tag_inner_socks").addClass("active");
# 				}
# 				else if(proxy == "out_socks") {
# 					$("#tag_outer_socks").addClass("active");
# 				}
# 				else if(proxy == "qq") {
# 					$("#tag_qq").addClass("active");
# 				}
# 				else if(proxy == "msn") {
# 					$("#tag_msn").addClass("active");
# 				}
# 			}
#
# 			$(".table tr th").dblclick(function() {
# 				sort_by_field = $(this).attr("id");
# 			    $(".label").each(function(index){
# 					old_href = $(this).attr("href").split("&sort")[0];
# 					new_href = old_href + "&sort=" + sort_by_field;
# 					//alert(new_href);
# 					$(this).attr("href", new_href);
# 			     });
# 			});
#
# 			$(".table tr th").click(function() {
# 				sort_by_field = $(this).attr("id");
#
# 				old_href = window.location.href.split("&sort")[0];
# 				if(window.location.href.indexOf("?") == -1){	// if only free.php, add "?proxy=in_tp"
# 					old_href = window.location.href + "?proxy=in_tp";
# 				}
# 				new_href = old_href + "&sort=" + sort_by_field;
# 				window.location.replace(new_href);
# // 			    $(".label").each(function(index){
# // 					old_href = $(this).attr("href").split("&sort")[0];
# // 					new_href = old_href + "&sort=" + sort_by_field;
# // 					//alert(new_href);
# // 					$(this).attr("href", new_href);
# // 			     });
# 			});
#
# 		    $(window).scroll(function () {
# 		        if ($(this).scrollTop() >= 100) {
# 		            $('#top_btn').css("visibility", "visible");
# 		            $('#top_btn').fadeIn(200);
# 		        } else {
# 		            $('#top_btn').fadeOut(200);
# 		            $('#top_btn').css("visibility", "hidden");
# 		        }
# 		    });
# 		    $('#top_btn').mouseover(function () {
# 		        $(this).css("opacity", 1);
# 		    }).mouseout(function () {
# 		        $(this).css("opacity", 0.5);
# 		    }).click(function () {
# 		        $("html, body").animate({
# 		            scrollTop: 0
# 		        }, 500);
# 		        return false;
# 		    });
# 		});
#
# 	</script>
#
# </body>
# </html>'''
# a = '''
# <!DOCTYPE html>
# <html>
# <head>
# <meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
# <title>昂森建材（河北）有限公司</title>
# <meta name="description" content="昂森建材（河北）有限公司位于河北 大城县 廊坊市大城县工业园区，营业范围有防腐、保温建材;防腐保温;玻璃鳞片防腐胶泥;乙烯基玻璃鳞片防腐漆;防火胶泥;岩棉板;硅酸铝板/管;硅酸盐板/管;泡沫玻璃板/管;聚氨酯保温板/管，联系电话为：86-031632611991" />
# <link rel="stylesheet" type="text/css" href="http://7.11467.com/www/css/b2b.css" />
# <link rel="canonical" href="http://www.11467.com/langfang/co/67329.htm" />
# <meta name="location" content="province=河北;city=廊坊">
# <meta name="viewport" content="width=1002px" />
# <meta name="applicable-device" content="pc">
# <meta http-equiv="Cache-Control" content="no-siteapp" />
# <link rel="alternate" media="only screen and (max-width: 640px)"  href="http://m.11467.com/langfang/co/67329.htm" />
# <meta http-equiv="mobile-agent" content="format=xhtml; url=http://m.11467.com/langfang/co/67329.htm" />
# <meta http-equiv="mobile-agent" content="format=html5; url=http://m.11467.com/langfang/co/67329.htm" />
# <link rel="dns-prefetch" href="//7.11467.com" />
# <script type="text/javascript"> var murl = "http://m.11467.com/langfang/co/67329.htm";</script>
# <script src="http://7.11467.com/www/js/co.js" language="javascript"></script>
# </head>
# <body>
#
# <div id="top">
# <div ID="m">
# <div id="menu">
#
# <ul>
# <li><a href="http://www.11467.com" title="企业黄页和免费发布信息">顺企网</a></li>
# <li><a href="http://b2b.11467.com/">公司黄页</a>
# <ul><li><a href="http://www.11467.com/dir.html" title="城市黄页">全国</a></li>
# <li><a href="http://www.11467.com/shanghai/" title="上海黄页">上海</a></li>
# <li><a href="http://www.11467.com/beijing/" title="北京黄页">北京</a></li>
# <li><a href="http://www.11467.com/shenzhen/" title="深圳黄页">深圳</a></li>
# <li><a href="http://www.11467.com/dongguan/" title="东莞黄页">东莞</a></li>
# <li><a href="http://www.11467.com/guangzhou/" title="广州黄页">广州</a></li>
# <li><a href="http://www.11467.com/tianjin/" title="天津黄页">天津</a></li>
# <li><a href="http://www.11467.com/suzhou/" title="苏州黄页">苏州</a></li>
# <li><a href="http://www.11467.com/jinan/" title="济南黄页">济南</a></li>
# <li><a href="http://www.11467.com/qingdao/" title="青岛黄页">青岛</a></li>
# <li><a href="http://www.11467.com/xiamen/" title="厦门黄页">厦门</a></li>
# <li><a href="http://www.11467.com/wuhan/" title="武汉黄页">武汉</a></li>
# </ul>
# </li>
# <li><a href="http://product.11467.com" title="产品供应批发">产品供应</a>
#
# <ul>
# <li><a href="http://product.11467.com/jixie/">机械设备</a></li>
# <li><a href="http://product.11467.com/wujin/">五金工具</a></li>
# <li><a href="http://product.11467.com/xiangsu/">橡胶塑料</a></li>
# <li><a href="http://product.11467.com/jiancai/">装饰建材</a></li>
# <li><a href="http://product.11467.com/dianzi/">电子元件</a></li>
# <li><a href="http://product.11467.com/diangong/">电工电气</a></li>
# <li><a href="http://product.11467.com/zhaoming/">照明灯具</a></li>
# <li><a href="http://product.11467.com/yibiao/">仪器仪表</a></li>
# <li><a href="http://product.11467.com/jiaotong/">交通运输</a></li>
# <li><a href="http://product.11467.com/qipei/">汽摩配件</a></li>
# <li><a href="http://product.11467.com/bangong/">办公用品</a></li>
# <li><a href="http://product.11467.com/fuwu/">商务服务</a></li>
# </ul>
# </li>
# <li><a href="http://buy.11467.com" title="采购网">采购商机</a></li>
# <li><a href="http://blog.11467.com">企业动态</a></li><li><a href="https://cp.11467.com" rel="nofollow">会员中心</a></li>
#
# </ul>
# </div>
# <div  id="toplogin">
# </div>
#  </div>
# </div>
# <div class="top"><div ID="logo"><a href="http://www.11467.com" title="顺企网"></a><h1>昂森建材（河北）有限公司</h1></div>
# <div id="logoright">
# <div id='comenu'><div><a href='#contact'>联系方式</a><a href='#map'>来访路线</a><a href='#cogb'>咨询留言</a></div></div>
# </div>
# </div>
#
# <div id='nav'><a href="http://www.11467.com" title="顺企网">顺企网</a> &raquo; <a href="http://b2b.11467.com/">公司黄页</a>  &raquo; <a href="http://www.11467.com/langfang/" title='廊坊黄页'>廊坊黄页</a>  &raquo; <a href="http://www.11467.com/langfang/search/368.htm">廊坊精细化学品公司</a>  &raquo; <a href="http://www.11467.com/langfang/search/10713.htm">廊坊涂料、油漆公司</a>  &raquo; <a href="http://www.11467.com/langfang/search/10714.htm">廊坊建筑涂料公司</a>&raquo; 昂森建材（河北）有限公司</div><div id="main" style="margin-top:0px;" ><div id='il'><span id="cotop" class="box"><dt><script language="javascript">gg();</script></dt><dd><script language="javascript">bd();</script></dd></span><div class="box"><h4 class="boxtitle">公司介绍</h4><div class="boxcontent text"><p><br />
#     	 昂森建材（河北）有限公司是防腐、保温建材、防腐保温、玻璃鳞片防腐胶泥、乙烯基玻璃鳞片防腐漆、防火胶泥、岩棉板、硅酸铝板/管、硅酸盐板/管、泡沫玻璃板/管、聚氨酯保温板/管等产品专业生产加工的公司，拥有完整、科学的质量管理体系。昂森建材（河北）有限公司的诚信、实力和产品质量获得业界的认可。欢迎各界朋友莅临参观、指导和业务洽谈。 <br />
#      <br />
#     </p><p></p></div></div><div class="t10"><script language='javascript'>var cpro_id = "u2166116";gg();</script></div><div class="box"><h4 class="boxtitle">基本资料</h4><div class="boxcontent"><dl id='contact'><dt>主营产品</dt><dd>防腐、保温建材;防腐保温;玻璃鳞片防腐胶泥;乙烯基玻璃鳞片防腐漆;防火胶泥;岩棉板;硅酸铝板/管;硅酸盐板/管;泡沫玻璃板/管;聚氨酯保温板/管</dd>
# <dt>公司注册地址</dt><dd> 河北  <a class="keylink" href="http://langfang.11467.com/dacheng/">大城县</a>  廊坊市 <a class="keylink" href="http://langfang.11467.com/dacheng/">大城县</a> 工业园区</dd>
# <dt>业务经理</dt><dd>刘梅</dd>
# <dt>邮政编码</dt><dd>065000</dd>
# <dt>电话</dt><dd>86-031632611991 （温馨提示：请核实资质，谨防诈骗）</dd>
# <dt>业务经理手机</dt><dd><img src="http://simg.11467.com/n/00310035003300350030003600390033003000320032.jpg" alt="业务经理手机号码"> 非诚勿扰</dd><dt>传真</dt><dd>-</dd>
# <dt>注册资金</dt><dd>未知</dd><dt>员工数量</dt><dd>51(人)</dd><dt>经营模式</dt><dd>生产加工</dd><dt>网址</dt><dd>http://www.11467.com/langfang/co/67329.htm</dd>
# <dt>信用等级</dt><dd><img src="http://7.11467.com/www/css/stars_5_small.gif" alt="五星" /></dd>
# <dt>企业人气</dt><dd>第<font color='#66cc00'>140</font>次被浏览</dd>
# <dt>所属分类</dt><dd><a href="http://b2b.11467.com/search/10714.htm">建筑涂料企业名录</a></dd>
# <dt>所属城市</dt><dd><a href="http://langfang.11467.com">廊坊企业名录</a></dd>
# </dl></div></div><div class="t10"><script language='javascript'>var cpro_id = "u2166116";gg();</script></div><div class="box"><h4 class="boxtitle">小提示</h4><div class="boxcontent" id="cotips">本页是 [昂森建材（河北）有限公司] 在顺企网的黄页介绍页，如果您是负责人并希望管理这家公司， <br />认领该企业后可以删除广告，或者信息有误需要纠正或者删除，请 [ <a rel="nofollow" href="https://cp.11467.com/app/manage.asp?cityid=langfang&id=67329&uid=21307849" style="color:#E10000">纠正或删除信息</a> ] </div></div><div id='map' class="box"><h4 class='boxtitle'>昂森建材（河北）有限公司的地图</h4><div class="boxcontent" ><div id="mapcontent"><script language="javascript">map('%BA%D3%B1%B1+%B4%F3%B3%C7%CF%D8+%C0%C8%B7%BB%CA%D0%B4%F3%B3%C7%CF%D8%B9%A4%D2%B5%D4%B0%C7%F8','%C0%C8%B7%BB','%B0%BA%C9%AD%BD%A8%B2%C4%A3%A8%BA%D3%B1%B1%A3%A9%D3%D0%CF%DE%B9%AB%CB%BE');</script></div>百度地图中的红点是昂森建材（河北）有限公司在廊坊的具体位置标注，您可以用鼠标拖动查找，双击放大缩小地图</div></div><div class="t10"><script language='javascript'>var cpro_id = "u2166116";gg();</script></div><div id='cogb'></div><div class="box sidesubcat"><h4 class="boxtitle">其他城市建筑涂料</h4><div class="boxcontent"><ul><li><a href="http://www.11467.com/shanghai/search/10714.htm">上海建筑涂料公司</a></li><li><a href="http://www.11467.com/shenzhen/search/10714.htm">深圳建筑涂料公司</a></li><li><a href="http://www.11467.com/beijing/search/10714.htm">北京建筑涂料公司</a></li><li><a href="http://www.11467.com/guangzhou/search/10714.htm">广州建筑涂料公司</a></li><li><a href="http://www.11467.com/dongguan/search/10714.htm">东莞建筑涂料公司</a></li><li><a href="http://www.11467.com/foshan/search/10714.htm">佛山建筑涂料公司</a></li><li><a href="http://www.11467.com/hangzhou/search/10714.htm">杭州建筑涂料公司</a></li><li><a href="http://www.11467.com/suzhou/search/10714.htm">苏州建筑涂料公司</a></li><li><a href="http://www.11467.com/chengdu/search/10714.htm">成都建筑涂料公司</a></li><li><a href="http://www.11467.com/chongqing/search/10714.htm">重庆建筑涂料公司</a></li><li><a href="http://www.11467.com/wenzhou/search/10714.htm">温州建筑涂料公司</a></li><li><a href="http://www.11467.com/wuxi/search/10714.htm">无锡建筑涂料公司</a></li></ul><div class="clear b10"></div></div></div></div><div id="sidebox"  class="sideboxclass"> <div class="t10"> <script language='javascript'>var cpro_id = "u1992721";gg();</script></div><div class="box"><h4 class="boxtitle">廊坊相关建筑涂料公司</h4><div class="boxcontent"><ul><li><a href='http://www.11467.com/langfang/co/67970.htm' title='大城县弥格防火材料厂'>大城县弥格防火材料厂</a></li><li><a href='http://www.11467.com/langfang/co/67968.htm' title='中国河北廊坊天澈贸易有限公司'>中国河北廊坊天澈贸易有限公司</a></li><li><a href='http://www.11467.com/langfang/co/67693.htm' title='大城鑫旺密封防水材料厂'>大城鑫旺密封防水材料厂</a></li><li><a href='http://www.11467.com/langfang/co/67365.htm' title='大城盘石防火材料厂'>大城盘石防火材料厂</a></li><li><a href='http://www.11467.com/langfang/co/67364.htm' title='廊坊荣兴保温建材有限公司'>廊坊荣兴保温建材有限公司</a></li><li><a href='http://www.11467.com/langfang/co/67329.htm' title='昂森建材（河北）有限公司'>昂森建材（河北）有限公司</a></li><li><a href='http://www.11467.com/langfang/co/65227.htm' title='万腾防腐材料有限公司'>万腾防腐材料有限公司</a></li><li><a href='http://www.11467.com/langfang/co/59909.htm' title='河北聚昌保温材料有限公司'>河北聚昌保温材料有限公司</a></li><li><a href='http://www.11467.com/langfang/co/49177.htm' title='河北廊坊金泽化工建材有限公司'>河北廊坊金泽化工建材有限公司</a></li><li><a href='http://www.11467.com/langfang/co/49041.htm' title='廊坊市顺兴源保温密封有限公司'>廊坊市顺兴源保温密封有限公司</a></li></ul></div></div><div class="t10"> <script language='javascript'>var cpro_id = "u2645567";gg();</script></div><div class="box"><h4 class="boxtitle">廊坊推荐企业</h4><div class="boxcontent"><ul><li><a href='http://www.11467.com/langfang/co/96061.htm' title='固安县绿泽物业服务有限公司'>固安县绿泽物业服务有限公司</a></li><li><a href='http://www.11467.com/langfang/co/96060.htm' title='廊坊市房汇轩房地产经纪有限公司'>廊坊市房汇轩房地产经纪有限公司</a></li><li><a href='http://www.11467.com/langfang/co/96059.htm' title='廊坊市中润商贸有限公司'>廊坊市中润商贸有限公司</a></li><li><a href='http://www.11467.com/langfang/co/96058.htm' title='廊坊市悦祥装饰工程有限公司'>廊坊市悦祥装饰工程有限公司</a></li><li><a href='http://www.11467.com/langfang/co/96057.htm' title='河北跃展豪科技有限公司'>河北跃展豪科技有限公司</a></li><li><a href='http://www.11467.com/langfang/co/96056.htm' title='廊坊市锋锐网络科技有限公司'>廊坊市锋锐网络科技有限公司</a></li><li><a href='http://www.11467.com/langfang/co/96055.htm' title='廊坊恒博农业发展有限公司'>廊坊恒博农业发展有限公司</a></li><li><a href='http://www.11467.com/langfang/co/96054.htm' title='河北三玉利保险代理有限公司廊坊第二十营业部'>河北三玉利保险代理有限公司廊坊第二十营业部</a></li><li><a href='http://www.11467.com/langfang/co/96053.htm' title='廊坊市和佳房产经纪有限公司开发区分公司'>廊坊市和佳房产经纪有限公司开发区分公司</a></li><li><a href='http://www.11467.com/langfang/co/96052.htm' title='大城县沣佃家庭农场有限公司'>大城县沣佃家庭农场有限公司</a></li></ul></div></div></div><div style='clear:both'></div>
# <script src="http://simg.11467.com/count.asp?cityid=langfang&id=67329&click=140"></script>
# <script type="text/javascript">
#     /*neiwen*/
# var cpro_id = "u1830537";
# </script>
# <script src="http://cpro.baidustatic.com/cpro/ui/cnw.js" type="text/javascript"></script>
#
# <div ID="b">
#
#
# <div id="bottomnav">
# <a href="http://www.11467.com/"  rel="nofollow">顺企网</a> |
# <a href="http://b2b.11467.com/" rel="nofollow">公司黄页</a> |
# <a href="http://product.11467.com"  rel="nofollow">产品供应</a> |
# <a href="http://www.11467.com/html/about.htm" title="关于顺企" rel="nofollow">关于顺企</a> |
# <a href="http://www.11467.com/html/contact.htm" title="联系顺企" rel="nofollow">联系顺企网</a> |
# <a href="http://www.11467.com/html/law.htm" title="法律声明" rel="nofollow">法律声明</a> |
# <a href="http://m.11467.com/langfang/co/67329.htm" title="手机版" rel="nofollow">手机版</a> </div>
#
# <div class="alert">免责声明：本站信息由企业自行发布，本站所有服务免费，请提防诈骗，顺企网不负任何责任
# </div>
# &copy; 11467.com 顺企网版权所有  发布批发采购信息、查询企业黄页，上顺企网 <br />
#  费时70毫秒，缓存：2016/6/25 0:52:50
# <script src="http://7.11467.com/www/js/b.js"></script>
#
# </div>
# </body>
# </html>'''
# r.encoding = 'utf8'
r = requests.get('http://httpbin.org/ip')
a = r.text
tree = etree.HTML(a)
print a
# print tree.xpath('//h2[@class="result-tit fl"]/span/text()')[0]


# tree.xpath("//h3/a/@href")














# [kuaidaili]'http://www.kuaidaili.com/free/inha/24/'
# ip = tree.xpath("//td[@data-title='IP']/text()")
# port = tree.xpath("//td[@data-title='PORT']/text()")
# for x in range(15):
#     print ip[x] + ':' + port[x]

# [zhihu] 登陆之后的页面
# name = tree.xpath("//span[@class='name']/text()")[0]
# ques = tree.xpath("//h2/a/text()")
# list_num = len(ques)
# print(name)
# for x in range(1, list_num):
#     print x, '   ', ques[x].strip()
#
# # print(u"美国经历过" in a)