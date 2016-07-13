# -*- coding:utf-8 -*-
#import requests
import bs4
import re
from lxml import etree
# url = "http://222.143.24.157/businessPublicity.jspx?id=35ED94CD71B4A102E053050A080A5B20&sourceType=1"
# r = requests.get(url)
# print r.status_code

html = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <META HTTP-EQUIV="pragma" CONTENT="no-cache"/>
    <META HTTP-EQUIV="Cache-Control" CONTENT="no-cache, must-revalidate"/>
    <META HTTP-EQUIV="expires" CONTENT="Wed, 26 Feb 1997 08:21:57 GMT"/>
    <title>全国企业信用信息公示系统</title>
    <link href="/css/public3.css" type="text/css" rel="stylesheet"/>
    <script type="text/javascript" src="/js/ajax.js"></script>
</head>
<body>
<div id="header">
    <div class="top">
        <div class="top-a">
		<a href="http://gsxt.saic.gov.cn"  style="font-size:14px ; font-family:'微软雅黑'">全国首页</a>&nbsp;&nbsp;<a href="/search.jspx"
		style="font-size:14px ; font-family:'微软雅黑'">地方局首页</a>
        </div>
    </div>
</div>
<br><br><br><br>

<div id="details" class="clear" style="height:930px">

    <h2 id="gsh2">
        南阳市丹尼斯新华店珀莱雅化妆品专柜&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;注册号：411391616090340&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“该个体工商户标记为经营异常状态”
    </h2>

<br/>

<div id="leftTabs">
    <ul>
        <li class="current" style="margin-bottom:2px;"><p>工<br/>商<br/>公<br/>示<br/>信<br/>息</p></li>
        <li onclick="togo('2')" style="margin-bottom:2px;"><p>个<br />体<br />工<br />商<br />户<br />公<br />示<br />信<br />息</p></li>
        <li onclick="togo('3')" style="margin-bottom:2px;"><p>其<br/>他<br/>部<br/>门<br/>公<br/>示<br/>信<br/>息</p></li>
    </ul>
</div>
<div id="detailsCon" style="height:900px">
<div class="dConBox">
<div class="tabs" id="tabs">
    <ul>
        <li id="1" class="current" onclick="r1(),changeStyle('tabs',this)">登记信息</li>
        <li id="2" onclick="r2(),changeStyle('tabs',this)">备案信息</li>
        <li id="3" onclick="r4(),changeStyle('tabs',this)">动产抵押登记信息</li>
        <li id="5" onclick="r7(),changeStyle('tabs',this)">行政处罚信息</li>
        <li id="4" onclick="r5(),changeStyle('tabs',this)">经营异常信息</li>
        <li id="6" onclick="r8(),changeStyle('tabs',this)">抽查检查信息</li>
    </ul>
</div>

<div id="jibenxinxi" style="height: 850px;width:930px;overflow: auto">
</br>
<table cellspacing="0" cellpadding="0" class="detailsList">
    <tr>
        <th colspan="4" style="text-align:center;">基本信息</th>
    </tr>

    <tr>
   		<th width="20%">注册号</th>
        <td>411391616090340&nbsp;</td>
        <th>名称</th>
        <td colspan="">南阳市丹尼斯新华店珀莱雅化妆品专柜</td>
    </tr>
    <tr>
        <th>类型</th>
        <td>个体工商户</td>
        <th width="20%">经营者</th>
        <td>王倩</td>
    </tr>
    <tr>
        <th>经营场所</th>
        <td colspan="3">南阳市丹尼斯新华店一楼</td>
    </tr>
    <tr>
        <th>组成形式</th>
        <td>
            个人经营
        </td>
        <th>注册日期</th>
        <td>
            2013年12月20日
        </td>
    </tr>
    <tr>
        <th>经营范围</th>
        <td colspan="3">
            化妆品 零售*
        </td>
    </tr>
    <tr>
        <th>登记机关</th>
        <td>南阳市工商行政管理局专业分局家电大世界市场管理办公室</td>
        <th>核准日期</th>
        <td>
                2015年5月29日
        </td>
    </tr>
    <tr>
        <th>登记状态</th>
        <td>存续</td>
        <th></th>
        <td></td>

    </tr>

</table>
<br>

</br>


    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="4" style="text-align:center;">变更信息</th>
        </tr>
        <tr width="95%">
            <th width="15%" style="text-align:center;"> 变更事项</th>
            <th width="25%" style="text-align:center;"> 变更前内容</th>
            <th width="25%" style="text-align:center;"> 变更后内容</th>
            <th width="10%" style="text-align:center;"> 变更日期</th>
        </tr>
    </table>
    <div id="altDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList" id="altTab">
        </table>
    </div>

</div>


<div id="beian" style="align:center;display:none;height: 850px;width:930px;overflow: auto">
    <br>
    <table style="width:100%;" id="t30" cellpadding="0" cellspacing="0" class="detailsList">
					<tr width="939px">
					<th colspan="4" style="text-align:center;">参加经营的家庭成员姓名</th>
                    </tr>
				    <tr>
                    <th style="width:10%;text-align:center">序号</th>
					<th style="width:20%;text-align:center">姓名</th>
                    <th style="width:10%;text-align:center">序号</th>
					<th style="width:20%;text-align:center">姓名</th>
					</tr>
              </table>
              <div id="memDiv">
                <table cellspacing="0" cellpadding="0" class="detailsList">
				</table>
			</div>
</div>


<div id="dongchandiya" style="display:none ;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="9" style="text-align:center;">动产抵押登记信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="20%" style="text-align:center;">登记编号</th>
            <th width="12%" style="text-align:center;">登记日期</th>
            <th width="20%" style="text-align:center;">登记机关</th>
            <th width="15%" style="text-align:center;">被担保债权数额</th>
            <th width="7%" style="text-align:center;">状态</th>
            <th width="13%" style="text-align:center;">公示日期</th>
            <th width="10%" style="text-align:center;">详情</th>
        </tr>
    </table>

    <div id="mortDiv">
        <table cellpadding="0" cellspacing="0" class="detailsList">
    </table>
    </div>
    <br/>
</div>

<div id="jingyingyichangminglu" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="6" style="text-align:center;">经营异常信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="20%" style="text-align:center;">标记经营异常状态原因</th>
            <th width="13%" style="text-align:center;">标记日期</th>
            <th width="25%" style="text-align:center;">恢复正常记载状态原因</th>
            <th width="13%" style="text-align:center;">恢复日期</th>
            <!--<th width="13%" style="text-align:center;">公示日期</th>-->
            <th width="19%" style="text-align:center;">作出决定机关</th>
        </tr>
    </table>
    <div id="excDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList" id="excTab">
                <tr>
                    <td width="5%" style="text-align:center;">1</td>
                    <td width="20%">2013年度，个体工商户未按照《个体工商户年度报告办法》规定报送年度报告的</td>
                    <td width="13%" style="text-align:center">
                        2016年6月22日
                    </td>
                    <td width="25%"></td>
                    <td width="13%" style="text-align:center">

                    </td>
                    <!--<td width="13%" style="text-align:center">-->
                           <!--2016年6月22日-->
                        <!--</td>-->
                    <td width="19%">南阳市工商行政管理局专业分局</td>
                </tr>

    </table>
    </div>
            <table cellpadding="0" cellspacing="0" class="detailsList">
                <th colspan="4" style="text-align:right;">
                    <span style="color:blue"><<</span>
                        &nbsp;<a id="aexc1" href='javascript:goPage6("exc",1);' style="text-decoration:none"><span id="spanexc1" style="color:red">1</span></a>
                                                        &nbsp;<span style="color:blue">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                </th>
            </table>
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="9" style="text-align:center;">年报信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="13%" style="text-align:center;">年报年度</th>
            <th width="13%" style="text-align:center;">上报情况</th>
            <th width="69%" style="text-align:center;">标记状态说明</th>
        </tr>
    </table>
    <div id="invExcDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList" id="invExcTab">

        </table>
    </div>
</div>


<div id="xingzhengchufa" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="9" style="text-align:center;">行政处罚信息</th>
        </tr>
        <tr width="95%">
            <th width="5%"  style="text-align:center;">序号</th>
            <th width="10%" style="text-align:center;">行政处罚<br>决定书文号</th>
            <th width="20%" style="text-align:center;">违法行为类型</th>
            <th width="18%" style="text-align:center;">行政处罚内容</th>
            <th width="18%" style="text-align:center;">作出行政处罚<br>决定机关名称</th>
            <th width="12%" style="text-align:center;">作出行政处罚<br>决定日期</th>
            <th width="12%" style="text-align:center;">公示日期</th>
            <th width="12%" style="text-align:center;">详情</th>

        </tr>
    </table>
    <div id="punDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList" id="punTab">
                    <tr width="95%">
                        <td width="5%" style="text-align:center;" valign="middle">
                            1
                        </td>
                        <td width="10%">
                            宛专工商处字[2015]67号
                        </td>
                        <td width="20%">
                            虚假宣传
                        </td>
                        <td width="18%">
                            罚款;
                        </td>
                        <td width="18%">
                            南阳市工商行政管理局专业分局
                        </td>
                        <td width="12%" style="text-align:center">
                            2015年5月26日
                        </td>
                        <td width="12%" style="text-align:center">2016年3月9日</td>
                        <td width="12%"  id="detailTd0">
                            <a href="javascript:void(0)" onclick="window.open('/punishInfoDetail.jspx?id=141000013135102316')">详情</a>
                        </td>

                    </tr>

    </table>
    </div>
            <table cellpadding="0" cellspacing="0" class="detailsList">
                <th colspan="4" style="text-align:right;">
                    <span style="color:blue"><<</span>
                        &nbsp;<a id="apun1" href='javascript:goPage5("pun",1);' style="text-decoration:none"><span id="spanpun1" style="color:red">1</span></a>
                                                        &nbsp;<span style="color:blue">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                </th>
            </table>
    <br/>
</div>

<div id="chouchaxinxi" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="5" style="text-align:center;">抽查检查信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="35%" style="text-align:center;">检查实施机关</th>
            <th width="10%" style="text-align:center;">类型</th>
            <th width="15%" style="text-align:center;">日期</th>
            <!--<th width="15%" style="text-align:center;">公示日期</th>-->
            <th width="25%" style="text-align:center;">结果</th>
        </tr>
     </table>
    <div id="spotCheckDiv">
    <table cellpadding="0" cellspacing="0" class="detailsList">
    </table>
    </div>
    <br/>
</div>
</div>
</div>
</div>

<br/> <br/>
<div class="banqun">
    版权所有：河南省工商行政管理局 <a target="_blank" style="color:red;text-decoration:underline;font-size:14px; " href="http://gsxt.haaic.gov.cn/phone.jspx">业务(技术)支持电话</a><br/>
    地址：郑州市花园路127号&nbsp;&nbsp;邮政编码：450008&nbsp;&nbsp;<span style="color:red">建议使用IE8及以上版本浏览器</span>
</div>
</body>
</html>
""" # 个体工商户
html = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <META HTTP-EQUIV="pragma" CONTENT="no-cache"/>
    <META HTTP-EQUIV="Cache-Control" CONTENT="no-cache, must-revalidate"/>
    <META HTTP-EQUIV="expires" CONTENT="Wed, 26 Feb 1997 08:21:57 GMT"/>
    <title>全国企业信用信息公示系统</title>
    <link href="/css/public3.css" type="text/css" rel="stylesheet"/>
    <script type="text/javascript" src="/js/infoExpand.js"></script>
    <script type="text/javascript" src="/js/ajax.js"></script>
	<script type="text/javascript">
		function closephone(){
			document.getElementById('sxphone').style.display='none';
			document.getElementById('bgDiv').style.display='none';
		}
		function iframeLoad(){
			var sxphoneHeight=$('#sxphone').height();
			$('#phoneiframe').height(sxphoneHeight-40);
		}
		function openphone(){
			window.scrollTo(0,0);
				var winWidth = 0;
		        var winHeight = 0;
		        if (window.innerWidth)
		              winWidth = window.innerWidth;
		        else if ((document.body) && (document.body.clientWidth))
		              winWidth = document.body.clientWidth;
		        //获取窗口高度
		        if (window.innerHeight)
		              winHeight = window.innerHeight;
		        else if ((document.body) && (document.body.clientHeight))
		              winHeight = document.body.clientHeight;

			var sxphone=document.getElementById("sxphone");
			if(sxphone){
				sxphone.top="50%";
				sxphone.left="50%";
				 //获取窗口宽度
				sxphone.style.display="";
				document.getElementById('bgDiv').style.display='';
			}
			else{
			 	var bgObj =document.createElement("div");
			    bgObj.setAttribute('id','bgDiv');
			    bgObj.style.position="absolute";
			    bgObj.style.top="0";
			    bgObj.style.background="#777";
			    bgObj.style.filter="progid:DXImageTransform.Microsoft.Alpha(style=3,opacity=25,finishOpacity=75";
			    bgObj.style.opacity="0.6";
			    bgObj.style.left="0";
			    bgObj.style.width=winWidth + "px";
			    bgObj.style.height=winHeight + "px";
			    bgObj.style.zIndex = "1000";
			    bgObj.style.MozOpacity="0.7";

			    document.body.appendChild(bgObj);
				var div = document.createElement("div");
				//div.id="sxphone";
				div.setAttribute('id','sxphone');
				div.style.height="80%";
				div.style.width="800px";
				div.style.border="0px solid red";
				div.style.position="absolute";
				div.style.left="50%";
				div.style.margin="0 0 0 -400px";
				div.style.top="5%";
				div.style.zIndex = "10001";
				div.style.MozBorderRadius="5px";
				div.style.webkitBorderRadius="5px";
				div.style.borderRadius="5px";
				div.style.background="#2D84B2";
				div.style.filter="progid:DXImageTransform.Microsoft.Alpha(style=3,opacity=100,finishOpacity=100";
				div.style.padding="0";
				  div.style.MozOpacity="1";
				div.innerHTML = "<div style='font-weight: bold;color: #fff;height:20px;padding:5px 20px;font-size:14px'><img src='/js/skins/ZCMS/images/icon.gif'/>咨询电话<span style='margin-left:660px;'>"+
				"<a style='color:#fff;font-size:12px' href='javascript:closephone();' title='关闭'>关闭</a></span></div>"+
					"<iframe id='phoneiframe' src='/sxphone.jspx' style='width:790px;border:0px solid red;padding:0;margin:5px 5px -10px 5px;' onload='iframeLoad()'></iframe>";
				document.body.appendChild(div);
				var ua = navigator.userAgent;
			    if (ua.lastIndexOf("MSIE 6.0") != -1) {
			    	var phoneiframe=document.getElementById("phoneiframe");
			    	//phoneiframe.style.width="840px";
			    	phoneiframe.style.height="580px";
			    	phoneiframe.style.marginRight="-15px";
				}
			}
		}
		function iframeLoadHb(){
			var sxphoneHeight=$('#sxphone').height();
			$('#phoneiframe').height(sxphoneHeight-60);
		}
			function openphonehb(){
			window.scrollTo(0,0);
				var winWidth = 0;
		        var winHeight = 0;
		        if (window.innerWidth)
		              winWidth = window.innerWidth;
		        else if ((document.body) && (document.body.clientWidth))
		              winWidth = document.body.clientWidth;
		        //获取窗口高度
		        if (window.innerHeight)
		              winHeight = window.innerHeight;
		        else if ((document.body) && (document.body.clientHeight))
		              winHeight = document.body.clientHeight;

			var sxphone=document.getElementById("sxphone");
			if(sxphone){
				sxphone.top="50%";
				sxphone.left="50%";
				 //获取窗口宽度
				sxphone.style.display="";
				document.getElementById('bgDiv').style.display='';
			}
			else{
			 	var bgObj =document.createElement("div");
			    bgObj.setAttribute('id','bgDiv');
			    bgObj.style.position="absolute";
			    bgObj.style.top="0";
			    bgObj.style.background="#777";
			    bgObj.style.filter="progid:DXImageTransform.Microsoft.Alpha(style=3,opacity=25,finishOpacity=75";
			    bgObj.style.opacity="0.6";
			    bgObj.style.left="0";
			    bgObj.style.width=winWidth + "px";
			    bgObj.style.height=winHeight + "px";
			    bgObj.style.zIndex = "1000";
			    bgObj.style.MozOpacity="0.7";

			    document.body.appendChild(bgObj);
				var div = document.createElement("div");
				//div.id="sxphone";
				div.setAttribute('id','sxphone');
				div.style.height="80%";
				div.style.width="800px";
				div.style.border="0px solid red";
				div.style.position="absolute";
				div.style.left="50%";
				div.style.margin="0 0 0 -400px";
				div.style.top="5%";
				div.style.zIndex = "10001";
				div.style.background="#ECEEEE";
				div.style.filter="progid:DXImageTransform.Microsoft.Alpha(style=3,opacity=100,finishOpacity=100";
				div.style.padding="0";
				  div.style.MozOpacity="1";
				div.innerHTML = "<div style='font-weight: bold;color: #000;height:20px;padding:5px 20px;font-size:14px;'>咨询电话<span style='float:right;'>"+
				"<a style='color:#000;font-size:12px' href='javascript:closephone();' title='关闭'>关闭</a></span></div>"+
				"<hr />"+
					"<iframe id='phoneiframe' src='/hbphone.jspx' style='width:790px;border:0px solid red;padding:0;margin:5px 5px -10px 5px;' onload='iframeLoadHb()'></iframe>";
				document.body.appendChild(div);
				var ua = navigator.userAgent;
			    if (ua.lastIndexOf("MSIE 6.0") != -1) {
			    	var phoneiframe=document.getElementById("phoneiframe");
			    	//phoneiframe.style.width="840px";
			    	phoneiframe.style.height="580px";
			    	phoneiframe.style.marginRight="-15px";
				}
			}
		}
	</script>
    <script type="text/javascript">
        function r1() {
            document.getElementById('jibenxinxi').style.display = 'block';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';

        }
        function r2() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'block';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';

        }
        function r4() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'block';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';
        }
        function r5() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'block';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';
        }
        function r6() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'block';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';
        }
        function r7() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'block';
            document.getElementById('chouchaxinxi').style.display = 'none';
        }
        function r8() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'block';
        }

        function togo(str) {
            if (str == '1') {
                window.location = '/businessPublicity.jspx?id=35F2504DA82C7363E053050A080ACA37';
            } else if (str == '2') {
                window.location = '/enterprisePublicity.jspx?id=35F2504DA82C7363E053050A080ACA37';
            }else if (str == '3') {
                window.location = '/otherDepartment.jspx?id=35F2504DA82C7363E053050A080ACA37';
            }
        }

    </script>

    <script type="text/javascript" defer="defer">
        function changeStyle(divId, ele) {
            var liAry = document.getElementById(divId).getElementsByTagName("li");
            var liLen = liAry.length;
            var liID = ele.id;
            for (var i = 0; i < liLen; i++) {
                if (liAry[i].id == liID) {
                    liAry[i].className = "current";

                }
                else {
                    liAry[i].className = "";
                }
            }
        }

        function ShowSpan(obj, n) {
            var span = obj.parentNode.getElementsByTagName("tabs");
            for (var i = 0; i < span.length; i++) {
                span[i].className = "current";
            }
            span[n].className = "";
            var li = obj.parentNode.getElementsByTagName("li")
            li[n].className = "current";
            for (var i = 0; i < li.length; i++) {
                if (i != n) {
                    li[i].className = "";
                }
                li[i].onmouseout = function () {
                    this.className = "current";
                }
            }
        }
          function changeTab() {
                var sourType = "1";
                   if (sourType == "1") {
                    r5();
                    var tab = document.getElementById("5");
                    changeStyle('tabs',tab);
                  } else if (sourType == "2") {
                    r6();
                    var tab = document.getElementById("6");
                    changeStyle('tabs',tab);
                  } else if (sourType == "3") {
                    r8();
                    var tab = document.getElementById("8");
                    changeStyle('tabs',tab);
                  }
        }
        window.onload = function() {
              changeTab();
        }
    </script>

</head>
<style type="text/css">
   th,td{word-break:break-all;}
  .top{width:990px; height:124px; background:url("/images/henan.png") no-repeat; }
  .banqun{width:990px; clear:both; height:59px; bottom:0; background:url("/images/ban-bj.png") repeat-x  ; padding-top:20px;font-size:14px; text-align:center; margin:0 auto;color:#fff;font-family:"微软雅黑";}
</style>

<body>
<div id="header">
    <div class="top">
        <div class="top-a">
		<a href="http://gsxt.saic.gov.cn"  style="font-size:14px ; font-family:'微软雅黑'">全国首页</a>&nbsp;&nbsp;<a href="/search.jspx"
		style="font-size:14px ; font-family:'微软雅黑'">地方局首页</a>
        </div>
    </div>
</div>
<br><br><br><br>

<div id="details" class="clear" style="height:930px">

    <h2 id="gsh2">
        洛阳市洛龙区启点网吧 &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; 注册号/统一社会信用代码：410307200000477&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp;“该企业已列入经营异常名录”
    </h2>

<br/>

<div id="leftTabs">
    <ul>
        <li class="current" style="margin-bottom:2px;"><p>工<br/>商<br/>公<br/>示<br/>信<br/>息</p></li>
        <li onclick="togo('2')" style="margin-bottom:2px;"><p>企<br/>业<br/>公<br/>示<br/>信<br/>息</p></li>
        <li onclick="togo('3')" style="margin-bottom:2px;"><p>其<br/>他<br/>部<br/>门<br/>公<br/>示<br/>信<br/>息</p></li>
    </ul>
</div>
<div id="detailsCon" style="height:900px">
<div class="dConBox">
<div class="tabs" id="tabs">
    <ul>
        <li id="1" class="current" onclick="r1(),changeStyle('tabs',this)">登记信息</li>
        <li id="2" onclick="r2(),changeStyle('tabs',this)">备案信息</li>
        <li id="4" onclick="r4(),changeStyle('tabs',this)">动产抵押登记信息</li>
        <li id="7" onclick="r7(),changeStyle('tabs',this)">行政处罚信息</li>
        <li id="5" onclick="r5(),changeStyle('tabs',this)">经营异常信息</li>
        <li id="6" onclick="r6(),changeStyle('tabs',this)">严重违法信息</li>
        <li id="8" onclick="r8(),changeStyle('tabs',this)">抽查检查信息</li>
    </ul>
</div>

<div id="jibenxinxi" style="height: 850px;width:930px;overflow: auto">
</br>
<table cellspacing="0" cellpadding="0" class="detailsList">
    <tr>
        <th colspan="4" style="text-align:center;">基本信息</th>
    </tr>

    <tr>
        <th width="20%">注册号/统一社会信用代码</th>
        <td width="30%"> 410307200000477 </td>
        <th>名称</th>
        <td width="30%">洛阳市洛龙区启点网吧</td>
    </tr>
    <tr>
        <th>类型</th>
        <td>个人独资企业</td>
        <th width="20%">投资人</th>
        <td>郝建民</td>
    </tr>

    <tr>
        <th>住所</th>
        <td colspan="3">
            洛阳市洛龙区安乐西侧（安乐宾馆隔壁）
        </td>
    </tr>

    <tr>
        <th>经营范围<br/></th>
        <td colspan="3">
            互联网上网服务（网络文化经营许可证有效期至2013年2月底）；预包装食品零售（食品流通许可证有效期至2014年3月31日）。
        </td>
    </tr>
    <tr>
        <th>登记机关</th>
        <td>洛阳市工商局关林分局</td>
        <th>核准日期</th>
        <td align="center">
                2016年6月21日
        </td>
    </tr>
    <tr>
        <th>成立日期</th>
        <td align="center">
                2007年4月17日
        </td>
        <th>登记状态</th>
        <td>吊销，未注销</td>


    </tr>

</table>
<br>
<table cellspacing="0" cellpadding="0" class="detailsList" id="touziren">
    <tr>
        <th colspan="2" style="text-align:center;">投资人信息</th>
    </tr>
    <tr width="95%">
        <th width="40%" style="text-align:center;">姓名</th>
        <th width="60%" style="text-align:center;">出资方式</th>
    </tr>
</table>
<div id="invDiv">
    <table cellspacing="0" cellpadding="0" class="detailsList">
    </table>
</div>
</br>


    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="4" style="text-align:center;">变更信息</th>
        </tr>
        <tr width="95%">
            <th width="15%" style="text-align:center;"> 变更事项</th>
            <th width="25%" style="text-align:center;"> 变更前内容</th>
            <th width="25%" style="text-align:center;"> 变更后内容</th>
            <th width="10%" style="text-align:center;"> 变更日期</th>
        </tr>
    </table>
    <div id="altDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList" id="altTab">
        </table>
    </div>
</div>


<div id="beian" style="align:center;display:none;height: 850px;width:930px;overflow: auto">
    <br>

    <table id="t31" cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="939px">
            <th colspan="4" style="text-align:center;">分支机构信息</th>
        </tr>
        <tr>
            <th style="text-align:center;width:10%;">序号</th>
            <th style="text-align:center;width:25%">注册号/统一社会信用代码</th>
            <th style="text-align:center;width:25%">名称</th>
            <th style="text-align:center;width:20%">登记机关</th>
        </tr>
    </table>
    <div id="childDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList">
        </table>
    </div>
</div>


<div id="dongchandiya" style="display:none ;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="8" style="text-align:center;">动产抵押登记信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="20%" style="text-align:center;">登记编号</th>
            <th width="12%" style="text-align:center;">登记日期</th>
            <th width="20%" style="text-align:center;">登记机关</th>
            <th width="15%" style="text-align:center;">被担保债权数额</th>
            <th width="7%" style="text-align:center;">状态</th>
            <th width="13%" style="text-align:center;">公示日期</th>
            <th width="10%" style="text-align:center;">详情</th>
        </tr>
    </table>

    <div id="mortDiv">
        <table cellpadding="0" cellspacing="0" class="detailsList">
    </table>
    </div>
    <br/>
</div>

<div id="jingyingyichangminglu" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="6" style="text-align:center;">经营异常信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="20%" style="text-align:center;">列入经营异常名录原因</th>
            <th width="13%" style="text-align:center;">列入日期</th>
            <th width="25%" style="text-align:center;">移出经营异常名录原因</th>
            <th width="13%" style="text-align:center;">移出日期</th>
            <!--<th width="13%" style="text-align:center;">公示日期</th>-->
            <th width="19%" style="text-align:center;">作出决定机关</th>
        </tr>
    </table>
    <div id="excDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList" id="excTab">
                    <tr width="95%">
                        <td style="text-align:center;" width="5%">1</td>
                        <td width="20%">通过登记的住所或者经营场所无法联系的</td>
                        <td style="text-align:center" width="13%">
                            2016年6月20日
                        </td>
                        <td width="25%"></td>
                        <td style="text-align:center" width="13%">

                        </td>
                         <!--<td width="13%" style="text-align:center">-->
                        <!--2016年6月20日-->
                        <!--</td>-->
                        <td width="19%">洛阳市工商局关林分局</td>
                    </tr>
                    <tr width="95%">
                        <td style="text-align:center;" width="5%">2</td>
                        <td width="20%">2014年度，未依照《企业信息公示暂行条例》第八条规定的期限公示年度报告的</td>
                        <td style="text-align:center" width="13%">
                            2015年7月14日
                        </td>
                        <td width="25%"></td>
                        <td style="text-align:center" width="13%">

                        </td>
                         <!--<td width="13%" style="text-align:center">-->
                        <!--2015年7月14日-->
                        <!--</td>-->
                        <td width="19%">洛阳市工商局关林分局</td>
                    </tr>
                    <tr width="95%">
                        <td style="text-align:center;" width="5%">3</td>
                        <td width="20%">2013年度，未依照《企业信息公示暂行条例》第八条规定的期限公示年度报告的</td>
                        <td style="text-align:center" width="13%">
                            2015年7月14日
                        </td>
                        <td width="25%"></td>
                        <td style="text-align:center" width="13%">

                        </td>
                         <!--<td width="13%" style="text-align:center">-->
                        <!--2015年7月14日-->
                        <!--</td>-->
                        <td width="19%">洛阳市工商局关林分局</td>
                    </tr>
                    <tr width="95%">
                        <td style="text-align:center;" width="5%">4</td>
                        <td width="20%">通过登记的住所或者经营场所无法联系的</td>
                        <td style="text-align:center" width="13%">
                            2015年6月22日
                        </td>
                        <td width="25%"></td>
                        <td style="text-align:center" width="13%">

                        </td>
                         <!--<td width="13%" style="text-align:center">-->
                        <!--2015年6月22日-->
                        <!--</td>-->
                        <td width="19%">洛阳市工商局关林分局</td>
                    </tr>
        </table>
    </div>
            <table cellpadding="0" cellspacing="0" class="detailsList">
                <th colspan="4" style="text-align:right;">
                    <span style="color:blue"><<</span>
                    &nbsp;<a id="aexc1" href='javascript:goPage6("exc",1);' style="text-decoration:none"><span id="spanexc1" style="color:red">1</span></a>
                                                        &nbsp;<span style="color:blue">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                </th>
            </table>
    <br/>
</div>

<div id="yanzhongweifaqiye" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="6" style="text-align:center;">严重违法信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="15%" style="text-align:center;">列入严重违法失信企业名单原因</th>
            <th width="13%" style="text-align:center;">列入日期</th>
            <th width="20%" style="text-align:center;">移出严重违法失信企业名单原因</th>
            <th width="13%" style="text-align:center;">移出日期</th>
            <!--<th width="13%" style="text-align:center;">公示日期</th>-->
            <th width="23%" style="text-align:center;">作出决定机关</th>
        </tr>
    </table>
    <div id="serillDiv">
    <table cellpadding="0" cellspacing="0" class="detailsList">
     </table>
     </div>
    <br/>
</div>

<div id="xingzhengchufa" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="8" style="text-align:center;">行政处罚信息</th>
        </tr>
        <tr width="95%">
            <th width="5%"  style="text-align:center;">序号</th>
            <th width="10%" style="text-align:center;">行政处罚<br>决定书文号</th>
            <th width="20%" style="text-align:center;">违法行为类型</th>
            <th width="18%" style="text-align:center;">行政处罚内容</th>
            <th width="18%" style="text-align:center;">作出行政处罚<br>决定机关名称</th>
            <th width="12%" style="text-align:center;">作出行政处罚<br>决定日期</th>
            <th width="12%" style="text-align:center;">公示日期</th>
            <th width="12%" style="text-align:center;">详情</th>

        </tr>
    </table>
    <div id="punDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList" id="punTab">
    </table>
    </div>
    <br/>
</div>

<div id="chouchaxinxi" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="5" style="text-align:center;">抽查检查信息</th>
        </tr>
        <tbody id="tableChoucha">
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="35%" style="text-align:center;">检查实施机关</th>
            <th width="10%" style="text-align:center;">类型</th>
            <th width="15%" style="text-align:center;">日期</th>
            <!--<th width="15%" style="text-align:center;">公示日期</th>-->
            <th width="25%" style="text-align:center;">结果</th>
        </tr>
     </table>
    <div id="spotCheckDiv">
    <table cellpadding="0" cellspacing="0" class="detailsList">
        </tbody>
    </table>
    </div>
    <br/>
</div>

</div>
</div>
</div>

<br/> <br/>
<div class="banqun">
    版权所有：河南省工商行政管理局 <a target="_blank" style="color:red;text-decoration:underline;font-size:14px; " href="http://gsxt.haaic.gov.cn/phone.jspx">业务(技术)支持电话</a><br/>
    地址：郑州市花园路127号&nbsp;&nbsp;邮政编码：450008&nbsp;&nbsp;<span style="color:red">建议使用IE8及以上版本浏览器</span>
</div>
</body>
</html>
<script>
    var pageNo1 = 1;
    var pageNo2 = 1;
    var pageNo3 = 1;
    var pageNo4 = 1;
    var pageNo5 = 1;//行政处罚
    var pageNo6 = 1;//经营异常
    function goPage1(flag, n) {
        var request = new ajax.Request();
        pageNo1 = n;
        setRed(flag, n);
        if (flag != null && flag == 'mem') {
            request.loadTextByGet("/QueryMemList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshMemList);
        } else if (flag != null && flag == 'child') {
            request.loadTextByGet("/QueryChildList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshChildList);
        }else if (flag != null && flag == 'alt') {
            request.loadTextByGet("/QueryAltList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshAltList);
        } else {
            request.loadTextByGet("/ownInvList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshInvList);
        }

    }
    function goPage2(flag, n) {
        var request = new ajax.Request();
        pageNo2 = n;
        setRed(flag, n);
        if (flag != null && flag == 'mem') {
            request.loadTextByGet("/QueryMemList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshMemList);
        } else if (flag != null && flag == 'child') {
            request.loadTextByGet("/QueryChildList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshChildList);
        }else if (flag != null && flag == 'alt') {
            request.loadTextByGet("/QueryAltList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshAltList);
        } else {
            request.loadTextByGet("/ownInvList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshInvList);
        }

    }
    function goPage3(flag, n) {
        var request = new ajax.Request();
        pageNo3 = n;
        setRed(flag, n);
        if (flag != null && flag == 'mem') {
            request.loadTextByGet("/QueryMemList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshMemList);
        } else if (flag != null && flag == 'child') {
            request.loadTextByGet("/QueryChildList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshChildList);
        }else if (flag != null && flag == 'alt') {
            request.loadTextByGet("/QueryAltList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshAltList);
        } else if (flag != null && flag == 'serill') {
            request.loadTextByGet("/QuerySerillList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshSerillList);
        }else if (flag != null && flag == 'spotCheck') {
            request.loadTextByGet("/QuerySpotCheckList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshSpotCheckList);
        }else {
            request.loadTextByGet("/ownInvList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshInvList);
        }

    }
    function slipFive(flag,lastMaxPage,totalPage,preOrNext) {
        var tpage = '0';
        var CurrentFirstPage ;
        if(preOrNext=='next'){
            if(lastMaxPage>=totalPage){
                CurrentFirstPage = (Math.floor(totalPage/5))*5+1;
            }else{
                CurrentFirstPage = lastMaxPage + 1;
            }
        }else{
            if(lastMaxPage<=5){
                CurrentFirstPage = 1;
            }else{
                if(lastMaxPage%5==0){
                    CurrentFirstPage = lastMaxPage - 9;
                }else{
                    CurrentFirstPage = (Math.floor(lastMaxPage/5))*5 - 4;
                }
            }
        }
       	if (flag != null && flag == 'inv') {
            tpage = '0';
        } else if (flag != null && flag == 'mem') {
            tpage = '1';
        } else if (flag != null && flag == 'child') {
            tpage = '0';
        } else if (flag != null && flag == 'alt') {
            tpage = '0';
        }else if (flag != null && flag == 'pledge') {
            tpage = '0';
        }else if (flag != null && flag == 'mort') {
            tpage = '0';
        }else if (flag != null && flag == 'exc') {
            tpage = '1';
        }else if (flag != null && flag == 'serill') {
            tpage = '0';
        }else if (flag != null && flag == 'puun') {
            tpage = '0';
        }else if (flag != null && flag == 'spotCheck') {
            tpage = '0';
        }

        goShowNextFive(flag, tpage,CurrentFirstPage,totalPage);
    }
   function goShowNextFive(flag, n,CurrentFirstPage,totalPage) {
        var currentMaxPage = 0;
        if((CurrentFirstPage+4)<totalPage){
            currentMaxPage = CurrentFirstPage+4;
        } else{
            currentMaxPage = totalPage;
        }
        var request = new ajax.Request();
        if (flag != null && flag == 'inv') {
            var invPagination = document.getElementById("invPagination");
            invPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"inv\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"ainv"+i+"\" href='javascript:goPage3(\"inv\","+i+");'><span id=\"spaninv"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"inv\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            invPagination.innerHTML= innerHTML;
            goPage3("inv",CurrentFirstPage);
        }else if (flag != null && flag == 'mem') {
            var memPagination = document.getElementById("memPagination");
            memPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"mem\","+currentMaxPage+",1,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"amem"+i+"\" href='javascript:goPage3(\"mem\","+i+");'><span id=\"spanmem"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"mem\","+currentMaxPage+",1,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            memPagination.innerHTML= innerHTML;
            goPage3("mem",CurrentFirstPage);
        } else if (flag != null && flag == 'child') {
            var childPagination = document.getElementById("childPagination");
            childPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"child\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"achild"+i+"\" href='javascript:goPage3(\"child\","+i+");'><span id=\"spanchild"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"child\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            childPagination.innerHTML= innerHTML;
            goPage3("child",CurrentFirstPage);
        }else if (flag != null && flag == 'alt') {
            var altPagination = document.getElementById("altPagination");
            altPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"alt\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"aalt"+i+"\" href='javascript:goPage3(\"alt\","+i+");'><span id=\"spanalt"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"alt\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            altPagination.innerHTML= innerHTML;
            goPage3("alt",CurrentFirstPage);
        }else if (flag != null && flag == 'pledge') {
            var pledgePagination = document.getElementById("pledgePagination");
            pledgePagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"pledge\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"apledge"+i+"\" href='javascript:goPage9(\"pledge\","+i+");'><span id=\"spanpledge"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"pledge\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            pledgePagination.innerHTML= innerHTML;
            goPage9("pledge",CurrentFirstPage);
        }else if (flag != null && flag == 'mort') {
            var mortPagination = document.getElementById("mortPagination");
            mortPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"mort\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"amort"+i+"\" href='javascript:goPage10(\"mort\","+i+");'><span id=\"spanmort"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"mort\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            mortPagination.innerHTML= innerHTML;
            goPage10("mort",CurrentFirstPage);
        }else if (flag != null && flag == 'exc') {
            var excPagination = document.getElementById("excPagination");
            excPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"exc\","+currentMaxPage+",1,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"aexc"+i+"\" href='javascript:goPage6(\"exc\","+i+");'><span id=\"spanexc"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"exc\","+currentMaxPage+",1,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            excPagination.innerHTML= innerHTML;
            goPage6("exc",CurrentFirstPage);
        }else if (flag != null && flag == 'serill') {
            var serillPagination = document.getElementById("serillPagination");
            serillPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"serill\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"aserill"+i+"\" href='javascript:goPage3(\"serill\","+i+");'><span id=\"spanserill"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"serill\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            serillPagination.innerHTML= innerHTML;
            goPage3("serill",CurrentFirstPage);
        }else if (flag != null && flag == 'pun') {
            var punPagination = document.getElementById("punPagination");
            punPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"pun\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"apun"+i+"\" href='javascript:goPage5(\"pun\","+i+");'><span id=\"spanpun"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"pun\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            punPagination.innerHTML= innerHTML;
            goPage5("pun",CurrentFirstPage);
        }else if (flag != null && flag == 'spotCheck') {
            var spotCheckPagination = document.getElementById("spotCheckPagination");
            spotCheckPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"spotCheck\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"aspotCheck"+i+"\" href='javascript:goPage3(\"spotCheck\","+i+");'><span id=\"spanspotCheck"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"spotCheck\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            spotCheckPagination.innerHTML= innerHTML;
            goPage3("spotCheck",CurrentFirstPage);
        }

    }
    function goPage4(flag, n) {
        var request = new ajax.Request();
        pageNo4 = n;
        setRed(flag, n);
        if (flag != null && flag == 'mem') {
            request.loadTextByGet("/QueryMemList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshMemList);
        } else if (flag != null && flag == 'child') {
            request.loadTextByGet("/QueryChildList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshChildList);
        }else if (flag != null && flag == 'alt') {
            request.loadTextByGet("/QueryAltList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshAltList);
        } else {
            request.loadTextByGet("/ownInvList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37", refreshInvList);
        }

    }

    function goPage5(flag, n) {
        var request = new ajax.Request();
        pageNo5 = n;
        setRed(flag, n);
        request.loadTextByGet("/QueryPunList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37&ran="+Math.random(), refreshPunList);
    }

    function goPage6(flag, n) {
        var request = new ajax.Request();
        pageNo6 = n;
        setRed(flag, n);
        request.loadTextByGet("/QueryExcList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37&ran="+Math.random(), refreshExcList);
    }

    function refreshInvList(message) {
        var divTab = document.getElementById("invDiv");
        divTab.innerHTML = '';
        divTab.innerHTML = message.substr(1, message.length - 2);
    }
    function refreshMemList(message) {
        var memDiv = document.getElementById("memDiv");
        memDiv.innerHTML = '';
        memDiv.innerHTML = message.substr(1, message.length - 2);
    }
    function refreshChildList(message) {
        var childDiv = document.getElementById("childDiv");
        childDiv.innerHTML = '';
        childDiv.innerHTML = message.substr(1, message.length - 2);
    }
    function refreshAltList(message) {
        var altDiv = document.getElementById("altDiv");
        altDiv.innerHTML = '';
        altDiv.innerHTML = message.substr(1, message.length - 2);
        doExpand();
    }
    function refreshPunList(message) {
        var punDiv = document.getElementById("punDiv");
        punDiv.innerHTML = '';
        punDiv.innerHTML = message.substr(1, message.length - 2);
        doExpand_pun();
    }
    function refreshExcList(message) {
        var excDiv = document.getElementById("excDiv");
        excDiv.innerHTML = '';
        excDiv.innerHTML = message.substr(1, message.length - 2);
        doExpand_exc();
    }
    function refreshSerillList(message) {
        var serillDiv = document.getElementById("serillDiv");
        serillDiv.innerHTML = '';
        serillDiv.innerHTML = message.substr(1, message.length - 2);
    }
    function refreshSpotCheckList(message) {
        var spotCheckDiv = document.getElementById("spotCheckDiv");
        spotCheckDiv.innerHTML = '';
        spotCheckDiv.innerHTML = message.substr(1, message.length - 2);
    }


    function next1(flag) {
        var tpage = '0';
        if (flag != null && flag == 'mem') {
            tpage = '1';
        } else if (flag != null && flag == 'child') {
            tpage = '0';
        } else if (flag != null && flag == 'alt') {
            tpage = '0';
        }

        goPage1(flag, tpage);
    }
    function next2(flag) {
        var tpage = '0';
        if (flag != null && flag == 'mem') {
            tpage = '1';
        } else if (flag != null && flag == 'child') {
            tpage = '0';
        } else if (flag != null && flag == 'alt') {
            tpage = '0';
        }

        goPage2(flag, tpage);
    }
    function next3(flag) {
        var tpage = '0';
        if (flag != null && flag == 'mem') {
            tpage = '1';
        } else if (flag != null && flag == 'child') {
            tpage = '0';
        } else if (flag != null && flag == 'alt') {
            tpage = '0';
        }else if (flag != null && flag == 'serill') {
            tpage = '0';
        }else if (flag != null && flag == 'spotCheck') {
            tpage = '0';
        }

        goPage3(flag, tpage);
    }
    function next4(flag) {
        var tpage = '0';
        if (flag != null && flag == 'mem') {
            tpage = '1';
        } else if (flag != null && flag == 'child') {
            tpage = '0';
        } else if (flag != null && flag == 'alt') {
            tpage = '0';
        }

        goPage4(flag, tpage);
    }
    function next5(flag) {
        var tpage = '0';
        goPage5(flag, tpage);
    }
    function next6(flag) {
        var tpage = '1';
        goPage6(flag, tpage);
    }


    function pre1(flag) {
        goPage1(flag, 1);
    }
    function pre2(flag) {
        goPage2(flag, 1);
    }
    function pre3(flag) {
        goPage3(flag, 1);
    }
    function pre4(flag) {
        goPage4(flag, 1);
    }
    function pre5(flag) {
        goPage5(flag, 1);
    }
    function pre6(flag) {
        goPage6(flag, 1);
    }

    function setRed(flag, n) {
        var currentFirstPage = Math.ceil(n/5)*5-4;
        var tpage = '0';
        if (flag != null && flag == 'inv') {
            tpage = '0';
        }else if (flag != null && flag == 'mem') {
            tpage = '1';
        } else if (flag != null && flag == 'child') {
            tpage = '0';
        } else if (flag != null && flag == 'alt') {
            tpage = '0';
        }else if (flag != null && flag == 'pun') {
            tpage = '0';
        }else if (flag != null && flag == 'exc') {
            tpage = '1';
        }else if (flag != null && flag == 'pledge') {
            tpage = '0';
        } else if (flag != null && flag == 'mort') {
            tpage = '0';
        }else if (flag != null && flag == 'serill') {
            tpage = '0';
        } else if (flag != null && flag == 'spotCheck') {
            tpage = '0';
        }

        for (var i = currentFirstPage; i <= (currentFirstPage+4); i++) {
            if(i>tpage){

            }else{
                document.getElementById("span" + flag + i).style.color = "";
                document.getElementById("a" + flag + i).style.textDecoration = "underline";
            }
        }
        document.getElementById("span" + flag + n).style.color = "red";
        document.getElementById("a" + flag + n).style.textDecoration = "none";
    }

    var pageNo10 = 1;//动产抵押
    function goPage10(flag, n) {
        var request = new ajax.Request();
        pageNo10 = n;
        setRed(flag, n);
        request.loadTextByGet("/QueryMortList.jspx?pno=" + n + "&mainId=35F2504DA82C7363E053050A080ACA37&ran=" + Math.random(), refreshMortList);
    }

    function next10(flag) {
        var tpage = '0';
        goPage10(flag, tpage);
    }

    function pre10(flag) {
        goPage10(flag, 1);
    }

    function refreshMortList(message) {
        var mortDiv = document.getElementById("mortDiv");
        mortDiv.innerHTML = '';
        mortDiv.innerHTML = message.substr(1, message.length - 2);
    }
     //显示更多
    function showAlterMore(rowIndex,size){
        var a = document.getElementById("a"+rowIndex);
        var td = document.getElementById("td"+rowIndex);
        var detailTd = document.getElementById("detailTd"+rowIndex);
        var div = document.getElementById("xingzhengchufa");
        var ele = document.getElementById("7");
        var showDiv1 = document.getElementById("tr"+rowIndex+1);
        if(showDiv1.style.display=="none"){
            a.innerText="收起更多";
            td.rowSpan=size+1;
            detailTd.rowSpan=size+1;
        }else{
             a.innerText="更多";
             td.rowSpan = 2;
            detailTd.rowSpan=2;
             changeStyle('tabs',ele);
             if(div.style.display="block"){
                div.style.display="";
             }else{
                 div.style.display="block";
             }
        }

        for(var i=1;i<size;i++){
            var showDiv = document.getElementById("tr"+rowIndex+i);
            if(showDiv.style.display=="none"){
                   showDiv.style.display="";
                }else{
                   showDiv.style.display="none";
                }
        }

    }

/*经营异常展开、缩起*/
    var arr_excIn = new Array();
    var arr_excOut = new Array();
    /*展开内容*/
    doExpand_exc();
/*变更信息展开、缩起*/
    var arr_altBe = new Array();
    var arr_altAf = new Array();
    /*展开内容*/

/*行政处罚 内容展开、收起*/
    var arr_punBasis = new Array();
    var arr_punResult = new Array();
    var arr_punAlt = new Array();

</script>
""" # 个人独资企业
html = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <META HTTP-EQUIV="pragma" CONTENT="no-cache"/>
    <META HTTP-EQUIV="Cache-Control" CONTENT="no-cache, must-revalidate"/>
    <META HTTP-EQUIV="expires" CONTENT="Wed, 26 Feb 1997 08:21:57 GMT"/>
    <title>全国企业信用信息公示系统</title>
    <link href="/css/public3.css" type="text/css" rel="stylesheet"/>
    <script type="text/javascript" src="/js/infoExpand.js"></script>
    <script type="text/javascript" src="/js/ajax.js"></script>
	<script type="text/javascript">
		function closephone(){
			document.getElementById('sxphone').style.display='none';
			document.getElementById('bgDiv').style.display='none';
		}
		function iframeLoad(){
			var sxphoneHeight=$('#sxphone').height();
			$('#phoneiframe').height(sxphoneHeight-40);
		}
		function openphone(){
			window.scrollTo(0,0);
				var winWidth = 0;
		        var winHeight = 0;
		        if (window.innerWidth)
		              winWidth = window.innerWidth;
		        else if ((document.body) && (document.body.clientWidth))
		              winWidth = document.body.clientWidth;
		        //获取窗口高度
		        if (window.innerHeight)
		              winHeight = window.innerHeight;
		        else if ((document.body) && (document.body.clientHeight))
		              winHeight = document.body.clientHeight;

			var sxphone=document.getElementById("sxphone");
			if(sxphone){
				sxphone.top="50%";
				sxphone.left="50%";
				 //获取窗口宽度
				sxphone.style.display="";
				document.getElementById('bgDiv').style.display='';
			}
			else{
			 	var bgObj =document.createElement("div");
			    bgObj.setAttribute('id','bgDiv');
			    bgObj.style.position="absolute";
			    bgObj.style.top="0";
			    bgObj.style.background="#777";
			    bgObj.style.filter="progid:DXImageTransform.Microsoft.Alpha(style=3,opacity=25,finishOpacity=75";
			    bgObj.style.opacity="0.6";
			    bgObj.style.left="0";
			    bgObj.style.width=winWidth + "px";
			    bgObj.style.height=winHeight + "px";
			    bgObj.style.zIndex = "1000";
			    bgObj.style.MozOpacity="0.7";

			    document.body.appendChild(bgObj);
				var div = document.createElement("div");
				//div.id="sxphone";
				div.setAttribute('id','sxphone');
				div.style.height="80%";
				div.style.width="800px";
				div.style.border="0px solid red";
				div.style.position="absolute";
				div.style.left="50%";
				div.style.margin="0 0 0 -400px";
				div.style.top="5%";
				div.style.zIndex = "10001";
				div.style.MozBorderRadius="5px";
				div.style.webkitBorderRadius="5px";
				div.style.borderRadius="5px";
				div.style.background="#2D84B2";
				div.style.filter="progid:DXImageTransform.Microsoft.Alpha(style=3,opacity=100,finishOpacity=100";
				div.style.padding="0";
				  div.style.MozOpacity="1";
				div.innerHTML = "<div style='font-weight: bold;color: #fff;height:20px;padding:5px 20px;font-size:14px'><img src='/js/skins/ZCMS/images/icon.gif'/>咨询电话<span style='margin-left:660px;'>"+
				"<a style='color:#fff;font-size:12px' href='javascript:closephone();' title='关闭'>关闭</a></span></div>"+
					"<iframe id='phoneiframe' src='/sxphone.jspx' style='width:790px;border:0px solid red;padding:0;margin:5px 5px -10px 5px;' onload='iframeLoad()'></iframe>";
				document.body.appendChild(div);
				var ua = navigator.userAgent;
			    if (ua.lastIndexOf("MSIE 6.0") != -1) {
			    	var phoneiframe=document.getElementById("phoneiframe");
			    	//phoneiframe.style.width="840px";
			    	phoneiframe.style.height="580px";
			    	phoneiframe.style.marginRight="-15px";
				}
			}
		}
		function iframeLoadHb(){
			var sxphoneHeight=$('#sxphone').height();
			$('#phoneiframe').height(sxphoneHeight-60);
		}
			function openphonehb(){
			window.scrollTo(0,0);
				var winWidth = 0;
		        var winHeight = 0;
		        if (window.innerWidth)
		              winWidth = window.innerWidth;
		        else if ((document.body) && (document.body.clientWidth))
		              winWidth = document.body.clientWidth;
		        //获取窗口高度
		        if (window.innerHeight)
		              winHeight = window.innerHeight;
		        else if ((document.body) && (document.body.clientHeight))
		              winHeight = document.body.clientHeight;

			var sxphone=document.getElementById("sxphone");
			if(sxphone){
				sxphone.top="50%";
				sxphone.left="50%";
				 //获取窗口宽度
				sxphone.style.display="";
				document.getElementById('bgDiv').style.display='';
			}
			else{
			 	var bgObj =document.createElement("div");
			    bgObj.setAttribute('id','bgDiv');
			    bgObj.style.position="absolute";
			    bgObj.style.top="0";
			    bgObj.style.background="#777";
			    bgObj.style.filter="progid:DXImageTransform.Microsoft.Alpha(style=3,opacity=25,finishOpacity=75";
			    bgObj.style.opacity="0.6";
			    bgObj.style.left="0";
			    bgObj.style.width=winWidth + "px";
			    bgObj.style.height=winHeight + "px";
			    bgObj.style.zIndex = "1000";
			    bgObj.style.MozOpacity="0.7";

			    document.body.appendChild(bgObj);
				var div = document.createElement("div");
				//div.id="sxphone";
				div.setAttribute('id','sxphone');
				div.style.height="80%";
				div.style.width="800px";
				div.style.border="0px solid red";
				div.style.position="absolute";
				div.style.left="50%";
				div.style.margin="0 0 0 -400px";
				div.style.top="5%";
				div.style.zIndex = "10001";
				div.style.background="#ECEEEE";
				div.style.filter="progid:DXImageTransform.Microsoft.Alpha(style=3,opacity=100,finishOpacity=100";
				div.style.padding="0";
				  div.style.MozOpacity="1";
				div.innerHTML = "<div style='font-weight: bold;color: #000;height:20px;padding:5px 20px;font-size:14px;'>咨询电话<span style='float:right;'>"+
				"<a style='color:#000;font-size:12px' href='javascript:closephone();' title='关闭'>关闭</a></span></div>"+
				"<hr />"+
					"<iframe id='phoneiframe' src='/hbphone.jspx' style='width:790px;border:0px solid red;padding:0;margin:5px 5px -10px 5px;' onload='iframeLoadHb()'></iframe>";
				document.body.appendChild(div);
				var ua = navigator.userAgent;
			    if (ua.lastIndexOf("MSIE 6.0") != -1) {
			    	var phoneiframe=document.getElementById("phoneiframe");
			    	//phoneiframe.style.width="840px";
			    	phoneiframe.style.height="580px";
			    	phoneiframe.style.marginRight="-15px";
				}
			}
		}
	</script>
    <script type="text/javascript">
        function r1() {
            document.getElementById('jibenxinxi').style.display = 'block';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('guquanchuzhi').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';

        }
        function r2() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'block';
            document.getElementById('guquanchuzhi').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';

        }
        function r3() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('guquanchuzhi').style.display = 'block';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';

        }
        function r4() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('guquanchuzhi').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'block';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';
        }
        function r5() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('guquanchuzhi').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'block';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';
        }
        function r6() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('guquanchuzhi').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'block';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';
        }
        function r7() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('guquanchuzhi').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'block';
            document.getElementById('chouchaxinxi').style.display = 'none';
        }
        function r8() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('guquanchuzhi').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'block';
        }

        function togo(str) {
            if (str == '1') {
                window.location = '/businessPublicity.jspx?id=35F33C590436FDCCE053050A080A8396';
            } else if (str == '2') {
                window.location = '/enterprisePublicity.jspx?id=35F33C590436FDCCE053050A080A8396';
            }else if (str == '3') {
                window.location = '/otherDepartment.jspx?id=35F33C590436FDCCE053050A080A8396';
            }else if(str == '4'){
                window.location = '/justiceAssistance.jspx?id=35F33C590436FDCCE053050A080A8396';
            }
        }

    </script>

    <script type="text/javascript" defer="defer">
        function changeStyle(divId, ele) {
            var liAry = document.getElementById(divId).getElementsByTagName("li");
            var liLen = liAry.length;
            var liID = ele.id;
            for (var i = 0; i < liLen; i++) {
                if (liAry[i].id == liID) {
                    liAry[i].className = "current";

                }
                else {
                    liAry[i].className = "";
                }
            }
        }

        function ShowSpan(obj, n) {
            var span = obj.parentNode.getElementsByTagName("tabs");
            for (var i = 0; i < span.length; i++) {
                span[i].className = "current";
            }
            span[n].className = "";
            var li = obj.parentNode.getElementsByTagName("li")
            li[n].className = "current";
            for (var i = 0; i < li.length; i++) {
                if (i != n) {
                    li[i].className = "";
                }
                li[i].onmouseout = function () {
                    this.className = "current";
                }
            }
        }
        function changeTab() {
                var sourType = "1";
                   if (sourType == "1") {
                    r5();
                    var tab = document.getElementById("5");
                    changeStyle('tabs',tab);
                  } else if (sourType == "2") {
                    r6();
                    var tab = document.getElementById("6");
                    changeStyle('tabs',tab);
                  } else if (sourType == "3") {
                    r8();
                    var tab = document.getElementById("8");
                    changeStyle('tabs',tab);
                  }
        }
        window.onload = function() {
              changeTab();
        }
    </script>

</head>
<style type="text/css">
    th,td{word-break:break-all;}
  .top{width:990px; height:124px; background:url("/images/henan.png") no-repeat; }
  .banqun{width:990px; height:59px; bottom:0; background:url("/images/ban-bj.png") repeat-x  ; padding-top:22px;font-size:14px; text-align:center; margin:0 auto;color:#fff;font-family:"微软雅黑";clear:both;}
</style>
<body>
<div id="header">
    <div class="top">
        <div class="top-a">
		<a href="http://gsxt.saic.gov.cn"  style="font-size:14px ; font-family:'微软雅黑'">全国首页</a>&nbsp;&nbsp;<a href="/search.jspx"
		style="font-size:14px ; font-family:'微软雅黑'">地方局首页</a>
        </div>
    </div>
</div>
<br><br><br><br>

<div id="details" class="clear" style="min-height: 880px;height: auto;">

    <h2 id="gsh2">
       商丘商为电子商务有限公司 &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; 注册号/统一社会信用代码： 91411402MA3X4MDH6M &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp;“该企业已列入经营异常名录”
    </h2>

<br/>

<div id="leftTabs">
    <ul>
        <li class="current" style="margin-bottom:2px;"><p>工<br/>商<br/>公<br/>示<br/>信<br/>息</p></li>
        <li onclick="togo('2')" style="margin-bottom:2px;"><p>企<br/>业<br/>公<br/>示<br/>信<br/>息</p></li>
        <li onclick="togo('3')" style="margin-bottom:2px;"><p>其<br/>他<br/>部<br/>门<br/>公<br/>示<br/>信<br/>息</p></li>
        	<li onclick="togo('4')"  style="margin-bottom:2px;"><p>司<br/>法<br/>协<br/>助<br/>公<br/>示<br/>信<br/>息</p></li>
    </ul>
</div>
<div id="detailsCon" style="height:1040px;overflow:atuo">
<div class="dConBox">
<div class="tabs" id="tabs">
    <ul>
        <li id="1" class="current" onclick="r1(),changeStyle('tabs',this)">登记信息</li>
        <li id="2" onclick="r2(),changeStyle('tabs',this)">备案信息</li>
        <li id="4" onclick="r4(),changeStyle('tabs',this)">动产抵押登记信息</li>
        <li id="3" onclick="r3(),changeStyle('tabs',this)">股权出质登记信息</li>
        <li id="7" onclick="r7(),changeStyle('tabs',this)">行政处罚信息</li>
        <li id="5" onclick="r5(),changeStyle('tabs',this)">经营异常信息</li>
        <li id="6" onclick="r6(),changeStyle('tabs',this)">严重违法信息</li>
        <li id="8" onclick="r8(),changeStyle('tabs',this)">抽查检查信息</li>
    </ul>
</div>

<div id="jibenxinxi" style="height: 850px;width:930px;overflow: auto">
</br>
<table cellspacing="0" cellpadding="0" class="detailsList">
    <tr>
        <th colspan="4" style="text-align:center;">基本信息</th>
    </tr>

    <tr>
        <th width="20%">注册号/<br/>统一社会信用代码</th>
        <td width="30%">  91411402MA3X4MDH6M
            </td>
        <th>名称</th>
        <td width="30%">商丘商为电子商务有限公司</td>
    </tr>
    <tr>
        <th>类型</th>
        <td>有限责任公司（自然人独资）</td>
        <th width="20%">法定代表人</th>
        <td>赵威博</td>
    </tr>
    <tr>
        <th>注册资本</th>
        <td>360万元</td>
        <th width="20%">成立日期</th>
        <td>
                2015年10月30日
        </td>

    </tr>
    <tr>
        <th>住所</th>
        <td colspan="3">
            商丘市民主路与归德路交叉口东300米路南腾飞综合楼2单元5层西户
        </td>
    </tr>
    <tr>
        <th>营业期限自</th>
        <td>
                2015年10月30日
        </td>
        <th>营业期限至</th>
        <td>
                2035年10月29日
        </td>
    </tr>
    <tr>
        <th>经营范围<br/></th>
        <td colspan="3">
            计算机软件开发、网络技术服务及推广；网上销售：计算机及周边耗材、电子产品、日用百货、安全技术防范产品、水果、干果、坚果、蔬菜、花卉。
        </td>
    </tr>
    <tr>
        <th>登记机关</th>
        <td>商丘市工商行政管理局梁园分局</td>
        <th>核准日期</th>
        <td>
                2015年10月30日
        </td>
    </tr>
    <tr>
        <th>登记状态</th>
        <td>存续</td>
        <th></th>
        <td></td>

    </tr>

</table>
<br>
<table cellspacing="0" cellpadding="0" class="detailsList" id="touziren">
    <tr>
        <th colspan="5" style="text-align:center;">股东信息<br/>
        </th>
</tr>
    <tr width="95%">
        <th width="20%" style="text-align:center;">股东</th>
        <th width="20%" style="text-align:center;">证照/证件类型</th>
        <th width="20%" style="text-align:center;">证照/证件号码</th>
        <th width="20%" style="text-align:center;">股东类型</th>
        <th width="20%" style="text-align:center;">详情</th>
    </tr>
</table>
<div id="invDiv">
    <table cellspacing="0" cellpadding="0" class="detailsList">
                <tr>
                    <td width="20%">
                          赵威博
                    </td>
                    <td width="20%">
                            中华人民共和国居民身份证
                    </td>
                    <td width="20%">
                            *****
                    </td>
                    <td width="20%">
                         自然人股东
                    </td>
                    <td width="20%">
                        <a href="javascript:void(0)" onclick="window.open('/queryInvDetailAction.jspx?id=141000012834602045')">详情</a>
                    </td>
                </tr>
    </table>
</div>
            <table cellpadding="0" cellspacing="0" class="detailsList">
                <th colspan="4" style="text-align:right;">
                    <span style="color:blue"><<</span>
                        &nbsp;<a id="ainv1" href='javascript:goPage3("inv",1);' style="text-decoration:none"><span id="spaninv1" style="color:red">1</span></a>
	                                                    &nbsp;<span style="color:blue">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                </th>
            </table>

<br/>


    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="4" style="text-align:center;">变更信息</th>
        </tr>
        <tr width="95%">
            <th width="15%" style="text-align:center;"> 变更事项</th>
            <th width="25%" style="text-align:center;"> 变更前内容</th>
            <th width="25%" style="text-align:center;"> 变更后内容</th>
            <th width="10%" style="text-align:center;"> 变更日期</th>
        </tr>
    </table>
    <div id="altDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList" id="altTab">
        </table>
    </div>

</div>


<div id="beian" style="align:center;display:none;height: 850px;width:930px;overflow: auto">
    <br>
    <table style="width:100%;" id="t30" cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="939px">
            <th colspan="6" style="text-align:center;">主要人员信息</th>
        </tr>
        <th style="width:10%;text-align:center">序号</th>
        <th style="width:20%;text-align:center">姓名</th>
        <th style="width:20%;text-align:center">职务</th>
        <th style="width:10%;text-align:center">序号</th>
        <th style="width:20%;text-align:center">姓名</th>
        <th style="width:20%;text-align:center">职务</th>
        </tr>
    </table>
    <div id="memDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList">
                        <tr>
                    <td style="width:10%;text-align:center">1</td>
                    <td style="width:20%">赵威博</td>
                    <td style="width:20%">执行董事</td>

                    <td style="width:10%;text-align:center">2</td>
                    <td style="width:20%">尚银涛</td>
                    <td style="width:20%">监事</td>
                        </tr>

        </table>
    </div>
            <table cellpadding="0" cellspacing="0" class="detailsList">
                <th colspan="4" style="text-align:right;">
                    <span style="color:blue"><<</span>
                        &nbsp;<a id="amem1" href='javascript:goPage3("mem",1);' style="text-decoration:none;"><span id="spanmem1" style="color:red">1</span></a>
                                                        &nbsp;<span style="color:blue">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                </th>
            </table>
    </br>

    <br>

    <table id="t31" cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="939px">
            <th colspan="4" style="text-align:center;">分支机构信息</th>
        </tr>
        <tr>
            <th style="text-align:center;width:10%;">序号</th>
            <th style="text-align:center;width:25%">注册号/统一社会信用代码</th>
            <th style="text-align:center;width:25%">名称</th>
            <th style="text-align:center;width:20%">登记机关</th>
        </tr>
    </table>
    <div id="childDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList">
        </table>
    </div>

    <br>


    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="939px">
            <th colspan="5" style="text-align:center;">清算信息</th>
        </tr>
        <tr>
            <th style="width:20%">清算组负责人</th>
            <td colspan="4">
            </td>
        </tr>
        <tr>
            <th rowspan="">清算组成员 </th>
            <td colspan="4">
            </td>
        </tr>
    </table>
</div>

<div id="guquanchuzhi" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="11" style="text-align:center;">股权出质登记信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="8%" style="text-align:center;">登记编号</th>
            <th width="6%" style="text-align:center;">出质人</th>
            <th width="13%" style="text-align:center;">证照/证件号码</th>
            <th width="8%" style="text-align:center;">出质股权数额</th>
            <th width="8%" style="text-align:center;">质权人</th>
            <th width="13%" style="text-align:center;">证照/证件号码</th>
            <th width="12%" style="text-align:center;">股权出质设立登记日期</th>
            <th width="7%" style="text-align:center;">状态</th>
             <th width="11%" style="text-align:center;">公示日期</th>
            <th width="6%" style="text-align:center;">变化情况</th>
        </tr>
    </table>

    <div id="pledgeDiv">
        <table cellpadding="0" cellspacing="0" class="detailsList">
        </table>
    </div>

    <br/>
</div>

<div id="dongchandiya" style="display:none ;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="8" style="text-align:center;">动产抵押登记信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="20%" style="text-align:center;">登记编号</th>
            <th width="12%" style="text-align:center;">登记日期</th>
            <th width="20%" style="text-align:center;">登记机关</th>
            <th width="15%" style="text-align:center;">被担保债权数额</th>
            <th width="7%" style="text-align:center;">状态</th>
             <th width="13%" style="text-align:center;">公示日期</th>
            <th width="10%" style="text-align:center;">详情</th>
        </tr>
    </table>

    <div id="mortDiv">
        <table cellpadding="0" cellspacing="0" class="detailsList">
    </table>
    </div>
    <br/>
</div>

<div id="jingyingyichangminglu" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="6" style="text-align:center;">经营异常信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="20%" style="text-align:center;">列入经营异常名录原因</th>
            <th width="13%" style="text-align:center;">列入日期</th>
            <th width="25%" style="text-align:center;">移出经营异常名录原因</th>
            <th width="13%" style="text-align:center;">移出日期</th>
            <!--<th width="13%" style="text-align:center;">公示日期</th>-->
            <th width="19%" style="text-align:center;">作出决定机关</th>
        </tr>
    </table>
    <div id="excDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList" id="excTab">
                <tr width="95%">
                    <td style="text-align:center;" width="5%">1</td>
                    <td width="20%">通过登记的住所或者经营场所无法联系的</td>
                    <td style="text-align:center" width="13%">
                        2016年6月23日
                    </td>
                    <td width="25%"></td>
                    <td style="text-align:center" width="13%">

                    </td>
                    <!--<td width="13%" style="text-align:center">-->
                        <!--2016年6月23日-->
                     <!--</td>-->
                    <td width="19%">商丘市工商行政管理局梁园分局</td>
                </tr>

    </table>
    </div>
            <table cellpadding="0" cellspacing="0" class="detailsList">
                <th colspan="4" style="text-align:right;">
                    <span style="color:blue"><<</span>
                        &nbsp;<a id="aexc1" href='javascript:goPage6("exc",1);' style="text-decoration:none"><span id="spanexc1" style="color:red">1</span></a>
                                                        &nbsp;<span style="color:blue">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                </th>
            </table>
    <br/>
</div>

<div id="yanzhongweifaqiye" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="6" style="text-align:center;">严重违法信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="15%" style="text-align:center;">列入严重违法失信企业名单原因</th>
            <th width="13%" style="text-align:center;">列入日期</th>
            <th width="20%" style="text-align:center;">移出严重违法失信企业名单原因</th>
            <th width="13%" style="text-align:center;">移出日期</th>
            <!--<th width="13%" style="text-align:center;">公示日期</th>-->
            <th width="23%" style="text-align:center;">作出决定机关</th>
        </tr>
    </table>
    <div id="serillDiv">
    <table cellpadding="0" cellspacing="0" class="detailsList">
     </table>
     </div>
    <br/>
</div>

<div id="xingzhengchufa" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="8" style="text-align:center;">行政处罚信息</th>
        </tr>
        <tr width="95%">
            <th width="5%"  style="text-align:center;">序号</th>
            <th width="10%" style="text-align:center;">行政处罚<br>决定书文号</th>
            <th width="20%" style="text-align:center;">违法行为类型</th>
            <th width="18%" style="text-align:center;">行政处罚内容</th>
            <th width="18%" style="text-align:center;">作出行政处罚<br>决定机关名称</th>
            <th width="12%" style="text-align:center;">作出行政处罚<br>决定日期</th>
            <th width="12%" style="text-align:center;">公示日期</th>
            <th width="12%" style="text-align:center;">详情</th>

        </tr>
    </table>
    <div id="punDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList" id="punTab">
    </table>
    </div>
    <br/>
</div>

<div id="chouchaxinxi" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="5" style="text-align:center;">抽查检查信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="35%" style="text-align:center;">检查实施机关</th>
            <th width="10%" style="text-align:center;">类型</th>
            <th width="15%" style="text-align:center;">日期</th>
            <!--<th width="15%" style="text-align:center;">公示日期</th>-->
            <th width="25%" style="text-align:center;">结果</th>
        </tr>
     </table>
    <div id="spotCheckDiv">
    <table cellpadding="0" cellspacing="0" class="detailsList">
    </table>
    </div>
    <br/>
</div>

</div>
</div>
</div>
<br/> <br/>
<div class="banqun">
    版权所有：河南省工商行政管理局 <a target="_blank" style="color:red;text-decoration:underline;font-size:14px; " href="http://gsxt.haaic.gov.cn/phone.jspx">业务(技术)支持电话</a><br/>
    地址：郑州市花园路127号&nbsp;&nbsp;邮政编码：450008&nbsp;&nbsp;<span style="color:red">建议使用IE8及以上版本浏览器</span>
</div>
</body>
</html>
<script>
    var pageNo1 = 1;
    var pageNo2 = 1;
    var pageNo3 = 1;
    var pageNo4 = 1;
    var pageNo5 = 1;//行政处罚
    var pageNo6 = 1;//经营异常
    function goPage1(flag, n) {
        var request = new ajax.Request();
        pageNo1 = n;
        setRed(flag, n);
        if (flag != null && flag == 'mem') {
            request.loadTextByGet("/QueryMemList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshMemList);
        } else if (flag != null && flag == 'child') {
            request.loadTextByGet("/QueryChildList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshChildList);
        }else if (flag != null && flag == 'alt') {
            request.loadTextByGet("/QueryAltList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshAltList);
        } else {
            request.loadTextByGet("/QueryInvList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshInvList);
        }

    }
    function goPage2(flag, n) {
        var request = new ajax.Request();
        pageNo2 = n;
        setRed(flag, n);
        if (flag != null && flag == 'mem') {
            request.loadTextByGet("/QueryMemList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshMemList);
        } else if (flag != null && flag == 'child') {
            request.loadTextByGet("/QueryChildList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshChildList);
        }else if (flag != null && flag == 'alt') {
            request.loadTextByGet("/QueryAltList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshAltList);
        } else {
            request.loadTextByGet("/QueryInvList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshInvList);
        }

    }
    function goPage3(flag, n) {
        var request = new ajax.Request();
        pageNo3 = n;
        setRed(flag, n);
        if (flag != null && flag == 'mem') {
            request.loadTextByGet("/QueryMemList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshMemList);
        } else if (flag != null && flag == 'child') {
            request.loadTextByGet("/QueryChildList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshChildList);
        }else if (flag != null && flag == 'alt') {
            request.loadTextByGet("/QueryAltList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshAltList);
        }else if (flag != null && flag == 'serill') {
            request.loadTextByGet("/QuerySerillList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshSerillList);
        }else if (flag != null && flag == 'spotCheck') {
            request.loadTextByGet("/QuerySpotCheckList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshSpotCheckList);
        }else {
            request.loadTextByGet("/QueryInvList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshInvList);
        }

    }
    function slipFive(flag,lastMaxPage,totalPage,preOrNext) {
        var tpage = '1';
        var CurrentFirstPage ;
        if(preOrNext=='next'){
            if(lastMaxPage>=totalPage){
                CurrentFirstPage = (Math.floor(totalPage/5))*5+1;
            }else{
                CurrentFirstPage = lastMaxPage + 1;
            }
        }else{
            if(lastMaxPage<=5){
                CurrentFirstPage = 1;
            }else{
                if(lastMaxPage%5==0){
                    CurrentFirstPage = lastMaxPage - 9;
                }else{
                    CurrentFirstPage = (Math.floor(lastMaxPage/5))*5 - 4;
                }
            }
        }
        if (flag != null && flag == 'inv') {
            tpage = '1';
        } else if (flag != null && flag == 'mem') {
            tpage = '1';
        } else if (flag != null && flag == 'child') {
            tpage = '0';
        } else if (flag != null && flag == 'alt') {
            tpage = '0';
        }else if (flag != null && flag == 'pledge') {
            tpage = '0';
        }else if (flag != null && flag == 'mort') {
            tpage = '0';
        }else if (flag != null && flag == 'exc') {
            tpage = '1';
        }else if (flag != null && flag == 'serill') {
            tpage = '0';
        }else if (flag != null && flag == 'puun') {
            tpage = '0';
        }else if (flag != null && flag == 'spotCheck') {
            tpage = '0';
        }

        goShowNextFive(flag, tpage,CurrentFirstPage,totalPage);
    }
    function goShowNextFive(flag, n,CurrentFirstPage,totalPage) {
        var currentMaxPage = 0;
        if((CurrentFirstPage+4)<totalPage){
            currentMaxPage = CurrentFirstPage+4;
        } else{
            currentMaxPage = totalPage;
        }
        var request = new ajax.Request();
        if (flag != null && flag == 'inv') {
            var invPagination = document.getElementById("invPagination");
            invPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"inv\","+currentMaxPage+",1,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"ainv"+i+"\" href='javascript:goPage3(\"inv\","+i+");'><span id=\"spaninv"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"inv\","+currentMaxPage+",1,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            invPagination.innerHTML= innerHTML;
            goPage3("inv",CurrentFirstPage);
        }else if (flag != null && flag == 'mem') {
            var memPagination = document.getElementById("memPagination");
            memPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"mem\","+currentMaxPage+",1,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"amem"+i+"\" href='javascript:goPage3(\"mem\","+i+");'><span id=\"spanmem"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"mem\","+currentMaxPage+",1,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            memPagination.innerHTML= innerHTML;
            goPage3("mem",CurrentFirstPage);
        } else if (flag != null && flag == 'child') {
            var childPagination = document.getElementById("childPagination");
            childPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"child\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"achild"+i+"\" href='javascript:goPage3(\"child\","+i+");'><span id=\"spanchild"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"child\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            childPagination.innerHTML= innerHTML;
            goPage3("child",CurrentFirstPage);
        }else if (flag != null && flag == 'alt') {
            var altPagination = document.getElementById("altPagination");
            altPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"alt\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"aalt"+i+"\" href='javascript:goPage3(\"alt\","+i+");'><span id=\"spanalt"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"alt\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            altPagination.innerHTML= innerHTML;
            goPage3("alt",CurrentFirstPage);
        }else if (flag != null && flag == 'pledge') {
            var pledgePagination = document.getElementById("pledgePagination");
            pledgePagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"pledge\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"apledge"+i+"\" href='javascript:goPage9(\"pledge\","+i+");'><span id=\"spanpledge"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"pledge\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            pledgePagination.innerHTML= innerHTML;
            goPage9("pledge",CurrentFirstPage);
        }else if (flag != null && flag == 'mort') {
            var mortPagination = document.getElementById("mortPagination");
            mortPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"mort\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"amort"+i+"\" href='javascript:goPage10(\"mort\","+i+");'><span id=\"spanmort"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"mort\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            mortPagination.innerHTML= innerHTML;
            goPage10("mort",CurrentFirstPage);
        }else if (flag != null && flag == 'exc') {
            var excPagination = document.getElementById("excPagination");
            excPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"exc\","+currentMaxPage+",1,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"aexc"+i+"\" href='javascript:goPage6(\"exc\","+i+");'><span id=\"spanexc"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"exc\","+currentMaxPage+",1,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            excPagination.innerHTML= innerHTML;
            goPage6("exc",CurrentFirstPage);
        }else if (flag != null && flag == 'serill') {
            var serillPagination = document.getElementById("serillPagination");
            serillPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"serill\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"aserill"+i+"\" href='javascript:goPage3(\"serill\","+i+");'><span id=\"spanserill"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"serill\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            serillPagination.innerHTML= innerHTML;
            goPage3("serill",CurrentFirstPage);
        }else if (flag != null && flag == 'pun') {
            var punPagination = document.getElementById("punPagination");
            punPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"pun\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"apun"+i+"\" href='javascript:goPage5(\"pun\","+i+");'><span id=\"spanpun"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"pun\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            punPagination.innerHTML= innerHTML;
            goPage5("pun",CurrentFirstPage);
        }else if (flag != null && flag == 'spotCheck') {
            var spotCheckPagination = document.getElementById("spotCheckPagination");
            spotCheckPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"spotCheck\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"aspotCheck"+i+"\" href='javascript:goPage3(\"spotCheck\","+i+");'><span id=\"spanspotCheck"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"spotCheck\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            spotCheckPagination.innerHTML= innerHTML;
            goPage3("spotCheck",CurrentFirstPage);
        }

    }
    function goPage4(flag, n) {
        var request = new ajax.Request();
        pageNo4 = n;
        setRed(flag, n);
        if (flag != null && flag == 'mem') {
            request.loadTextByGet("/QueryMemList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshMemList);
        } else if (flag != null && flag == 'child') {
            request.loadTextByGet("/QueryChildList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshChildList);
        }else if (flag != null && flag == 'alt') {
            request.loadTextByGet("/QueryAltList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshAltList);
        } else {
            request.loadTextByGet("/QueryInvList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396", refreshInvList);
        }

    }

    function goPage5(flag, n) {
        var request = new ajax.Request();
        pageNo5 = n;
        setRed(flag, n);
        request.loadTextByGet("/QueryPunList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396&ran="+Math.random(), refreshPunList);
    }

    function goPage6(flag, n ) {
        var request = new ajax.Request();
        pageNo6 = n;
        setRed(flag, n);
        request.loadTextByGet("/QueryExcList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396&ran="+Math.random(), refreshExcList);
    }

    function refreshInvList(message) {
        var divTab = document.getElementById("invDiv");
        divTab.innerHTML = '';
        divTab.innerHTML = message.substr(1, message.length - 2);
    }
    function refreshMemList(message) {
        var memDiv = document.getElementById("memDiv");
        memDiv.innerHTML = '';
        memDiv.innerHTML = message.substr(1, message.length - 2);
    }
    function refreshChildList(message) {
        var childDiv = document.getElementById("childDiv");
        childDiv.innerHTML = '';
        childDiv.innerHTML = message.substr(1, message.length - 2);
    }
    function refreshAltList(message) {
        var altDiv = document.getElementById("altDiv");
        altDiv.innerHTML = '';
        altDiv.innerHTML = message.substr(1, message.length - 2);
        doExpand();
    }
    function refreshSerillList(message) {
        var serillDiv = document.getElementById("serillDiv");
        serillDiv.innerHTML = '';
        serillDiv.innerHTML = message.substr(1, message.length - 2);
    }
    function refreshSpotCheckList(message) {
        var spotCheckDiv = document.getElementById("spotCheckDiv");
        spotCheckDiv.innerHTML = '';
        spotCheckDiv.innerHTML = message.substr(1, message.length - 2);
    }
    function refreshPunList(message) {
        var punDiv = document.getElementById("punDiv");
        punDiv.innerHTML = '';
        punDiv.innerHTML = message.substr(1, message.length - 2);
        doExpand_pun();
    }
    function refreshExcList(message) {
        var excDiv = document.getElementById("excDiv");
        excDiv.innerHTML = '';
        excDiv.innerHTML = message.substr(1, message.length - 2);
        doExpand_exc();
    }

    function next1(flag) {
        var tpage = '1';
        if (flag != null && flag == 'mem') {
            tpage = '1';
        } else if (flag != null && flag == 'child') {
            tpage = '0';
        } else if (flag != null && flag == 'alt') {
            tpage = '0';
        }

        goPage1(flag, tpage);
    }
    function next2(flag) {
        var tpage = '1';
        if (flag != null && flag == 'mem') {
            tpage = '1';
        } else if (flag != null && flag == 'child') {
            tpage = '0';
        } else if (flag != null && flag == 'alt') {
            tpage = '0';
        }

        goPage2(flag, tpage);
    }
    function next3(flag) {
        var tpage = '1';
        if (flag != null && flag == 'mem') {
            tpage = '1';
        } else if (flag != null && flag == 'child') {
            tpage = '0';
        } else if (flag != null && flag == 'alt') {
            tpage = '0';
        }else if (flag != null && flag == 'serill') {
            tpage = '0';
        }else if (flag != null && flag == 'spotCheck') {
            tpage = '0';
        }

        goPage3(flag, tpage);
    }
    function next4(flag) {
        var tpage = '1';
        if (flag != null && flag == 'mem') {
            tpage = '1';
        } else if (flag != null && flag == 'child') {
            tpage = '0';
        } else if (flag != null && flag == 'alt') {
            tpage = '0';
        }

        goPage4(flag, tpage);
    }
    function next5(flag) {
        var tpage = '0';
        goPage5(flag, tpage);
    }
    function next6(flag) {
        var tpage = '1';
        goPage6(flag, tpage);
    }

    function pre1(flag) {
        goPage1(flag, 1);
    }
    function pre2(flag) {
        goPage2(flag, 1);
    }
    function pre3(flag) {
        goPage3(flag, 1);
    }
    function pre4(flag) {
        goPage4(flag, 1);
    }
    function pre5(flag) {
        goPage5(flag, 1);
    }
    function pre6(flag) {
        goPage6(flag, 1);
    }

    function setRed(flag, n) {
        var currentFirstPage = Math.ceil(n/5)*5-4;
        var tpage = '1';
        if (flag != null && flag == 'inv') {
            tpage = '1';
        }else if (flag != null && flag == 'mem') {
            tpage = '1';
        } else if (flag != null && flag == 'child') {
            tpage = '0';
        } else if (flag != null && flag == 'alt') {
            tpage = '0';
        }else if (flag != null && flag == 'pun') {
            tpage = '0';
        }else if (flag != null && flag == 'exc') {
            tpage = '1';
        }else if (flag != null && flag == 'pledge') {
            tpage = '0';
        } else if (flag != null && flag == 'mort') {
            tpage = '0';
        }else if (flag != null && flag == 'serill') {
            tpage = '0';
        } else if (flag != null && flag == 'spotCheck') {
            tpage = '0';
        }

        for (var i = currentFirstPage; i <= (currentFirstPage+4); i++) {
            if(i>tpage){

            }else{
                document.getElementById("span" + flag + i).style.color = "";
                document.getElementById("a" + flag + i).style.textDecoration = "underline";
            }
        }
        document.getElementById("span" + flag + n).style.color = "red";
        document.getElementById("a" + flag + n).style.textDecoration = "none";
    }

    var pageNo9 = 1;//股权出质
    function goPage9(flag, n) {
        var request = new ajax.Request();
        pageNo9 = n;
        if(typeof(redFlag)!="undefined" && !redFlag){
             //页码滑动不标红当前页
        } else {
            setRed(flag, n);
        }
        request.loadTextByGet("/QueryPledgeList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396&ran=" + Math.random(), refreshPledgeList);
    }

    function next9(flag) {
        var tpage = '0';
        goPage9(flag, tpage);
    }

    function pre9(flag) {
        goPage9(flag, 1);
    }

    function refreshPledgeList(message) {
        var pledgeDiv = document.getElementById("pledgeDiv");
        pledgeDiv.innerHTML = '';
        pledgeDiv.innerHTML = message.substr(1, message.length - 2);
    }

    var pageNo10 = 1;//动产抵押
    function goPage10(flag, n) {
        var request = new ajax.Request();
        pageNo10 = n;
        setRed(flag, n);
        request.loadTextByGet("/QueryMortList.jspx?pno=" + n + "&mainId=35F33C590436FDCCE053050A080A8396&ran=" + Math.random(), refreshMortList);
    }

    function next10(flag) {
        var tpage = '0';
        goPage10(flag, tpage);
    }

    function pre10(flag) {
        goPage10(flag, 1);
    }

    function refreshMortList(message) {
        var mortDiv = document.getElementById("mortDiv");
        mortDiv.innerHTML = '';
        mortDiv.innerHTML = message.substr(1, message.length - 2);
    }
    //显示更多
    function showAlterMore(rowIndex,size){
        /*var a = document.getElementById("a"+rowIndex);
        var td = document.getElementById("td"+rowIndex);
        var detailTd = document.getElementById("detailTd"+rowIndex);
        var div = document.getElementById("xingzhengchufa");
        var ele = document.getElementById("7");
        var showDiv1 = document.getElementById("tr"+rowIndex+1);
        if(showDiv1.style.display=="none"){
            a.innerText="收起更多";
            td.rowSpan=size+1;
            detailTd.rowSpan=size+1;
        }else{
             a.innerText="更多";
             td.rowSpan = 2;
            detailTd.rowSpan=2;
             changeStyle('tabs',ele);
             if(div.style.display="block"){
                div.style.display="";
             }else{
                 div.style.display="block";
             }
        }

        for(var i=1;i<size;i++){
            var showDiv = document.getElementById("tr"+rowIndex+i);
            if(showDiv.style.display=="none"){
                   showDiv.style.display="";
                }else{
                   showDiv.style.display="none";
                }
        }*/
        var altPunTD = document.getElementById("altPunTD");
        var h = altPunTD.offsetHeight;  //高度
        alert(h);

    }
/*变更信息 内容展开、收起*/
    var arr_altBe = new Array();
    var arr_altAf = new Array();
    /*展开内容*/
/*经营异常信息 内容展开、收起*/
    var arr_excIn = new Array();
    var arr_excOut = new Array();
    /*展开内容*/
    doExpand_exc();

/*行政处罚信息 内容展开、收起*/
    var arr_punBasis = new Array();
    var arr_punResult = new Array();
    var arr_punAlt = new Array();


</script>
""" # 有限责任公司（自然人独资）
html = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <META HTTP-EQUIV="pragma" CONTENT="no-cache"/>
    <META HTTP-EQUIV="Cache-Control" CONTENT="no-cache, must-revalidate"/>
    <META HTTP-EQUIV="expires" CONTENT="Wed, 26 Feb 1997 08:21:57 GMT"/>
    <title>全国企业信用信息公示系统</title>
    <link href="/css/public3.css" type="text/css" rel="stylesheet"/>
    <script type="text/javascript" src="/js/ajax.js"></script>
    <script type="text/javascript" src="/js/infoExpand.js"></script>
	<script type="text/javascript">
		function closephone(){
			document.getElementById('sxphone').style.display='none';
			document.getElementById('bgDiv').style.display='none';
		}
		function iframeLoad(){
			var sxphoneHeight=$('#sxphone').height();
			$('#phoneiframe').height(sxphoneHeight-40);
		}
		function openphone(){
			window.scrollTo(0,0);
				var winWidth = 0;
		        var winHeight = 0;
		        if (window.innerWidth)
		              winWidth = window.innerWidth;
		        else if ((document.body) && (document.body.clientWidth))
		              winWidth = document.body.clientWidth;
		        //获取窗口高度
		        if (window.innerHeight)
		              winHeight = window.innerHeight;
		        else if ((document.body) && (document.body.clientHeight))
		              winHeight = document.body.clientHeight;

			var sxphone=document.getElementById("sxphone");
			if(sxphone){
				sxphone.top="50%";
				sxphone.left="50%";
				 //获取窗口宽度
				sxphone.style.display="";
				document.getElementById('bgDiv').style.display='';
			}
			else{
			 	var bgObj =document.createElement("div");
			    bgObj.setAttribute('id','bgDiv');
			    bgObj.style.position="absolute";
			    bgObj.style.top="0";
			    bgObj.style.background="#777";
			    bgObj.style.filter="progid:DXImageTransform.Microsoft.Alpha(style=3,opacity=25,finishOpacity=75";
			    bgObj.style.opacity="0.6";
			    bgObj.style.left="0";
			    bgObj.style.width=winWidth + "px";
			    bgObj.style.height=winHeight + "px";
			    bgObj.style.zIndex = "1000";
			    bgObj.style.MozOpacity="0.7";

			    document.body.appendChild(bgObj);
				var div = document.createElement("div");
				//div.id="sxphone";
				div.setAttribute('id','sxphone');
				div.style.height="80%";
				div.style.width="800px";
				div.style.border="0px solid red";
				div.style.position="absolute";
				div.style.left="50%";
				div.style.margin="0 0 0 -400px";
				div.style.top="5%";
				div.style.zIndex = "10001";
				div.style.MozBorderRadius="5px";
				div.style.webkitBorderRadius="5px";
				div.style.borderRadius="5px";
				div.style.background="#2D84B2";
				div.style.filter="progid:DXImageTransform.Microsoft.Alpha(style=3,opacity=100,finishOpacity=100";
				div.style.padding="0";
				  div.style.MozOpacity="1";
				div.innerHTML = "<div style='font-weight: bold;color: #fff;height:20px;padding:5px 20px;font-size:14px'><img src='/js/skins/ZCMS/images/icon.gif'/>咨询电话<span style='margin-left:660px;'>"+
				"<a style='color:#fff;font-size:12px' href='javascript:closephone();' title='关闭'>关闭</a></span></div>"+
					"<iframe id='phoneiframe' src='/sxphone.jspx' style='width:790px;border:0px solid red;padding:0;margin:5px 5px -10px 5px;' onload='iframeLoad()'></iframe>";
				document.body.appendChild(div);
				var ua = navigator.userAgent;
			    if (ua.lastIndexOf("MSIE 6.0") != -1) {
			    	var phoneiframe=document.getElementById("phoneiframe");
			    	//phoneiframe.style.width="840px";
			    	phoneiframe.style.height="580px";
			    	phoneiframe.style.marginRight="-15px";
				}
			}
		}
		function iframeLoadHb(){
			var sxphoneHeight=$('#sxphone').height();
			$('#phoneiframe').height(sxphoneHeight-60);
		}
			function openphonehb(){
			window.scrollTo(0,0);
				var winWidth = 0;
		        var winHeight = 0;
		        if (window.innerWidth)
		              winWidth = window.innerWidth;
		        else if ((document.body) && (document.body.clientWidth))
		              winWidth = document.body.clientWidth;
		        //获取窗口高度
		        if (window.innerHeight)
		              winHeight = window.innerHeight;
		        else if ((document.body) && (document.body.clientHeight))
		              winHeight = document.body.clientHeight;

			var sxphone=document.getElementById("sxphone");
			if(sxphone){
				sxphone.top="50%";
				sxphone.left="50%";
				 //获取窗口宽度
				sxphone.style.display="";
				document.getElementById('bgDiv').style.display='';
			}
			else{
			 	var bgObj =document.createElement("div");
			    bgObj.setAttribute('id','bgDiv');
			    bgObj.style.position="absolute";
			    bgObj.style.top="0";
			    bgObj.style.background="#777";
			    bgObj.style.filter="progid:DXImageTransform.Microsoft.Alpha(style=3,opacity=25,finishOpacity=75";
			    bgObj.style.opacity="0.6";
			    bgObj.style.left="0";
			    bgObj.style.width=winWidth + "px";
			    bgObj.style.height=winHeight + "px";
			    bgObj.style.zIndex = "1000";
			    bgObj.style.MozOpacity="0.7";

			    document.body.appendChild(bgObj);
				var div = document.createElement("div");
				//div.id="sxphone";
				div.setAttribute('id','sxphone');
				div.style.height="80%";
				div.style.width="800px";
				div.style.border="0px solid red";
				div.style.position="absolute";
				div.style.left="50%";
				div.style.margin="0 0 0 -400px";
				div.style.top="5%";
				div.style.zIndex = "10001";
				div.style.background="#ECEEEE";
				div.style.filter="progid:DXImageTransform.Microsoft.Alpha(style=3,opacity=100,finishOpacity=100";
				div.style.padding="0";
				  div.style.MozOpacity="1";
				div.innerHTML = "<div style='font-weight: bold;color: #000;height:20px;padding:5px 20px;font-size:14px;'>咨询电话<span style='float:right;'>"+
				"<a style='color:#000;font-size:12px' href='javascript:closephone();' title='关闭'>关闭</a></span></div>"+
				"<hr />"+
					"<iframe id='phoneiframe' src='/hbphone.jspx' style='width:790px;border:0px solid red;padding:0;margin:5px 5px -10px 5px;' onload='iframeLoadHb()'></iframe>";
				document.body.appendChild(div);
				var ua = navigator.userAgent;
			    if (ua.lastIndexOf("MSIE 6.0") != -1) {
			    	var phoneiframe=document.getElementById("phoneiframe");
			    	//phoneiframe.style.width="840px";
			    	phoneiframe.style.height="580px";
			    	phoneiframe.style.marginRight="-15px";
				}
			}
		}
	</script>
    <script type="text/javascript">
        function r1() {
            document.getElementById('jibenxinxi').style.display = 'block';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('guquanchuzhi').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';

        }
        function r2() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'block';
            document.getElementById('guquanchuzhi').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';

        }
        function r3() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('guquanchuzhi').style.display = 'block';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';

        }
        function r4() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('guquanchuzhi').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'block';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';
        }
        function r5() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('guquanchuzhi').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'block';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';
        }
        function r6() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('guquanchuzhi').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'block';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'none';
        }
        function r7() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('guquanchuzhi').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'block';
            document.getElementById('chouchaxinxi').style.display = 'none';
        }
        function r8() {
            document.getElementById('jibenxinxi').style.display = 'none';
            document.getElementById('beian').style.display = 'none';
            document.getElementById('guquanchuzhi').style.display = 'none';
            document.getElementById('dongchandiya').style.display = 'none';
            document.getElementById('jingyingyichangminglu').style.display = 'none';
            document.getElementById('yanzhongweifaqiye').style.display = 'none';
            document.getElementById('xingzhengchufa').style.display = 'none';
            document.getElementById('chouchaxinxi').style.display = 'block';
        }

        function togo(str) {
            if (str == '1') {
                window.location = '/businessPublicity.jspx?id=35FF188B1850F08EE053050A080A6100';
            } else if (str == '2') {
                window.location = '/enterprisePublicity.jspx?id=35FF188B1850F08EE053050A080A6100';
            }else if (str == '3') {
                window.location = '/otherDepartment.jspx?id=35FF188B1850F08EE053050A080A6100';
            }else if(str == '4'){
                window.location = '/justiceAssistance.jspx?id=35FF188B1850F08EE053050A080A6100';
            }
        }
          function changeTab() {
                var sourType = "1";
                   if (sourType == "1") {
                    r5();
                    var tab = document.getElementById("5");
                    changeStyle('tabs',tab);
                  } else if (sourType == "2") {
                    r6();
                    var tab = document.getElementById("6");
                    changeStyle('tabs',tab);
                  } else if (sourType == "3") {
                    r8();
                    var tab = document.getElementById("8");
                    changeStyle('tabs',tab);
                  }
        }
        window.onload = function() {
              changeTab();
        }
    </script>

    <script type="text/javascript" defer="defer">
        function changeStyle(divId, ele) {
            var liAry = document.getElementById(divId).getElementsByTagName("li");
            var liLen = liAry.length;
            var liID = ele.id;
            for (var i = 0; i < liLen; i++) {
                if (liAry[i].id == liID) {
                    liAry[i].className = "current";

                }
                else {
                    liAry[i].className = "";
                }
            }
        }

        function ShowSpan(obj, n) {
            var span = obj.parentNode.getElementsByTagName("tabs");
            for (var i = 0; i < span.length; i++) {
                span[i].className = "current";
            }
            span[n].className = "";
            var li = obj.parentNode.getElementsByTagName("li")
            li[n].className = "current";
            for (var i = 0; i < li.length; i++) {
                if (i != n) {
                    li[i].className = "";
                }
                li[i].onmouseout = function () {
                    this.className = "current";
                }
            }
        }
    </script>

</head>
<style type="text/css">
    th,td{word-break:break-all;}
  .top{width:990px; height:124px; background:url("/images/henan.png") no-repeat; }
  .banqun{width:990px; height:59px; bottom:0; background:url("/images/ban-bj.png") repeat-x  ; padding-top:20px;font-size:14px; text-align:center; margin:0 auto;color:#fff;font-family:"微软雅黑";clear:both;}
</style>

<body>
<div id="header">
    <div class="top">
        <div class="top-a">
		<a href="http://gsxt.saic.gov.cn"  style="font-size:14px ; font-family:'微软雅黑'">全国首页</a>&nbsp;&nbsp;<a href="/search.jspx"
		style="font-size:14px ; font-family:'微软雅黑'">地方局首页</a>
        </div>
    </div>
</div>
<br><br><br><br>

<div id="details" class="clear" style="min-height: 880px;height: auto;">

    <h2 id="gsh2">
      许昌联鑫投资股份有限公司 &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; 注册号/统一社会信用代码：411000000005683&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp;“该企业已列入经营异常名录”
    </h2>

<br/>

<div id="leftTabs">
    <ul>
        <li class="current" style="margin-bottom:2px;"><p>工<br/>商<br/>公<br/>示<br/>信<br/>息</p></li>
        <li onclick="togo('2')" style="margin-bottom:2px;"><p>企<br/>业<br/>公<br/>示<br/>信<br/>息</p></li>
        <li onclick="togo('3')" style="margin-bottom:2px;"><p>其<br/>他<br/>部<br/>门<br/>公<br/>示<br/>信<br/>息</p></li>
        <li onclick="togo('4')"  style="margin-bottom:2px;"><p>司<br/>法<br/>协<br/>助<br/>公<br/>示<br/>信<br/>息</p></li>
    </ul>
</div>
<div id="detailsCon" style="height:1038px;overflow:atuo">
<div class="dConBox">
<div class="tabs" id="tabs">
    <ul>
        <li id="1" class="current" onclick="r1(),changeStyle('tabs',this)">登记信息</li>
        <li id="2" onclick="r2(),changeStyle('tabs',this)">备案信息</li>
        <li id="4" onclick="r4(),changeStyle('tabs',this)">动产抵押登记信息</li>
        <li id="3" onclick="r3(),changeStyle('tabs',this)">股权出质登记信息</li>
        <li id="7" onclick="r7(),changeStyle('tabs',this)">行政处罚信息</li>
        <li id="5" onclick="r5(),changeStyle('tabs',this)">经营异常信息</li>
        <li id="6" onclick="r6(),changeStyle('tabs',this)">严重违法信息</li>
        <li id="8" onclick="r8(),changeStyle('tabs',this)">抽查检查信息</li>
    </ul>
</div>

<div id="jibenxinxi" style="height: 850px;width:930px;overflow: auto">
    </br>
    <table cellspacing="0" cellpadding="0" class="detailsList">
        <tr>
            <th colspan="4" style="text-align:center;">基本信息</th>
        </tr>

        <tr>
        <th width="20%">注册号/统一社会信用代码</th>
        <td width="30%"> 411000000005683 </td>
        <th>名称</th>
        <td width="30%">许昌联鑫投资股份有限公司</td>
    </tr>
        <tr>
            <th>类型</th>
            <td>股份有限公司(非上市、自然人投资或控股)</td>
            <th width="20%">法定代表人</th>
            <td>袁新</td>
        </tr>
        <tr>
            <th>注册资本</th>
            <td>500万元</td>
            <th width="20%">成立日期</th>
            <td>
                    2010年7月21日
            </td>

        </tr>
        <tr>
            <th>住所</th>
            <td colspan="3">
                禹州市建设路中段南侧
            </td>
        </tr>
        <tr>
            <th>营业期限自</th>
            <td>
                    2010年7月21日
            </td>
            <th>营业期限至</th>
            <td>
                    2020年7月30日
            </td>
        </tr>
        <tr>
            <th>经营范围<br/></th>
            <td colspan="3">
                对室内装潢设计、园林绿化、工程设施安装、房地产开发、水电安装、物业管理、商业贸易、科学技术、农业行业、中小企业进行投资（国家限制投资的行业和项目除外）；商务信息、房地产信息、旅游信息、财务信息、劳务信息、教育信息的咨询（国家法律法规规定需专项审批的项目除外）。
            </td>
        </tr>
        <tr>
            <th>登记机关</th>
            <td>许昌市工商行政管理局</td>
            <th>核准日期</th>
            <td>
                    2010年7月21日
            </td>
        </tr>
        <tr>
            <th>登记状态</th>
            <td>存续</td>
            <th></th>
            <td></td>

        </tr>

    </table>
    <br>
    <table cellspacing="0" cellpadding="0" class="detailsList" id="touziren">
        <tr>
            <th colspan="5" style="text-align:center;">股东（发起人）信息<br/>
                </th>

        </tr>
        <tr width="95%">
            <th width="20%" style="text-align:center;">股东（发起人）</th>
            <th width="20%" style="text-align:center;">证照/证件类型</th>
            <th width="20%" style="text-align:center;">证照/证件号码</th>
            <th width="20%" style="text-align:center;">股东（发起人）类型</th>
            <th width="20%" style="text-align:center;">详情</th>
        </tr>
    </table>
    <div id="invDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList">
                    <tr>
                          <td width="20%">
                            侯松杰
                        </td>
                         <td width="20%">
                                中华人民共和国居民身份证
                        </td>
                        <td width="20%">
                                *****
                        </td>
                         <td width="20%">
                            自然人股东
                        </td>
                        <td width="20%">
                            <a href="javascript:void(0)" onclick="window.open('/queryInvDetailAction.jspx?id=141000010063351583')">详情</a>
                        </td>
                    </tr>
                    <tr>
                          <td width="20%">
                            袁新
                        </td>
                         <td width="20%">
                                中华人民共和国居民身份证
                        </td>
                        <td width="20%">
                                *****
                        </td>
                         <td width="20%">
                            自然人股东
                        </td>
                        <td width="20%">
                            <a href="javascript:void(0)" onclick="window.open('/queryInvDetailAction.jspx?id=141000010063351584')">详情</a>
                        </td>
                    </tr>
        </table>
    </div>
            <table cellpadding="0" cellspacing="0" class="detailsList">
                <th colspan="4" style="text-align:right;">
                    <span style="color:blue"><<</span>
                        &nbsp;<a id="ainv1" href='javascript:goPage3("inv",1);' style="text-decoration:none"><span id="spaninv1" style="color:red">1</span></a>
	                                                    &nbsp;<span style="color:blue">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                </th>
            </table>

    </br>


    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="4" style="text-align:center;">变更信息</th>
        </tr>
        <tr width="95%">
            <th width="15%" style="text-align:center;"> 变更事项</th>
            <th width="25%" style="text-align:center;"> 变更前内容</th>
            <th width="25%" style="text-align:center;"> 变更后内容</th>
            <th width="10%" style="text-align:center;"> 变更日期</th>
        </tr>
    </table>
    <div id="altDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList" id="altTab">
        </table>
    </div>

</div>


<div id="beian" style="align:center;display:none;height: 850px;width:930px;overflow: auto">
    <br>
    <table style="width:100%;" id="t30" cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="939px">
            <th colspan="6" style="text-align:center;">主要人员信息</th>
        </tr>
        <th style="width:10%;text-align:center">序号</th>
        <th style="width:20%;text-align:center">姓名</th>
        <th style="width:20%;text-align:center">职务</th>
        <th style="width:10%;text-align:center">序号</th>
        <th style="width:20%;text-align:center">姓名</th>
        <th style="width:20%;text-align:center">职务</th>
        </tr>
    </table>
    <div id="memDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList">
                        <tr>
                    <td style="width:10%;text-align:center">1</td>
                    <td style="width:20%">常晓兰</td>
                    <td style="width:20%">董事</td>

                    <td style="width:10%;text-align:center">2</td>
                    <td style="width:20%">侯丽敏</td>
                    <td style="width:20%">董事</td>
                        </tr>

                        <tr>
                    <td style="width:10%;text-align:center">3</td>
                    <td style="width:20%">杨红杰</td>
                    <td style="width:20%">董事</td>

                    <td style="width:10%;text-align:center">4</td>
                    <td style="width:20%">杨晓非</td>
                    <td style="width:20%">监事</td>
                        </tr>

                        <tr>
                    <td style="width:10%;text-align:center">5</td>
                    <td style="width:20%">侯松杰</td>
                    <td style="width:20%">监事</td>

                    <td style="width:10%;text-align:center">6</td>
                    <td style="width:20%">李会景</td>
                    <td style="width:20%">董事</td>
                        </tr>

                        <tr>
                    <td style="width:10%;text-align:center">7</td>
                    <td style="width:20%">王定远</td>
                    <td style="width:20%">监事</td>

                    <td style="width:10%;text-align:center">8</td>
                    <td style="width:20%">袁新</td>
                    <td style="width:20%">董事长、总经理</td>
                        </tr>

        </table>
    </div>
            <table cellpadding="0" cellspacing="0" class="detailsList">
                <th colspan="4" style="text-align:right;">
                    <span style="color:blue"><<</span>
                        &nbsp;<a id="amem1" href='javascript:goPage3("mem",1);' style="text-decoration:none"><span id="spanmem1" style="color:red">1</span></a>
                                                        &nbsp;<span style="color:blue">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                </th>
            </table>

    </br>

    <br>

    <table id="t31" cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="939px">
            <th colspan="4" style="text-align:center;">分支机构信息</th>
        </tr>
        <tr>
            <th style="text-align:center;width:10%;">序号</th>
            <th style="text-align:center;width:25%">注册号/统一社会信用代码</th>
            <th style="text-align:center;width:25%">名称</th>
            <th style="text-align:center;width:20%">登记机关</th>
        </tr>
    </table>
    <div id="childDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList">
        </table>
    </div>

    <br>


    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="939px">
            <th colspan="5" style="text-align:center;">清算信息</th>
        </tr>
        <tr>
            <th style="width:20%">清算组负责人</th>
            <td colspan="4">


            </td>
        </tr>
        <tr>
            <th rowspan="">清算组成员 </th>
            <td colspan="4">
            </td>
        </tr>
    </table>
</div>

<div id="guquanchuzhi" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="11" style="text-align:center;">股权出质登记信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="8%" style="text-align:center;">登记编号</th>
            <th width="6%" style="text-align:center;">出质人</th>
            <th width="13%" style="text-align:center;">证照/证件号码</th>
            <th width="8%" style="text-align:center;">出质股权数额</th>
            <th width="8%" style="text-align:center;">质权人</th>
            <th width="13%" style="text-align:center;">证照/证件号码</th>
            <th width="12%" style="text-align:center;">股权出质设立登记日期</th>
            <th width="7%" style="text-align:center;">状态</th>
            <th width="11%" style="text-align:center">公示日期</th>
            <th width="6%" style="text-align:center;">变化情况</th>
        </tr>
    </table>

    <div id="pledgeDiv">
        <table cellpadding="0" cellspacing="0" class="detailsList">
        </table>
    </div>

    <br/>
</div>

<div id="dongchandiya" style="display:none ;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="9" style="text-align:center;">动产抵押登记信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="20%" style="text-align:center;">登记编号</th>
            <th width="12%" style="text-align:center;">登记日期</th>
            <th width="20%" style="text-align:center;">登记机关</th>
            <th width="15%" style="text-align:center;">被担保债权数额</th>
            <th width="7%" style="text-align:center;">状态</th>
            <th width="13%" style="text-align:center;">公示日期</th>
            <th width="10%" style="text-align:center;">详情</th>
        </tr>
    </table>

    <div id="mortDiv">
        <table cellpadding="0" cellspacing="0" class="detailsList">
    </table>
    </div>
    <br/>
</div>

<div id="jingyingyichangminglu" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="6" style="text-align:center;">经营异常信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="20%" style="text-align:center;">列入经营异常名录原因</th>
            <th width="13%" style="text-align:center;">列入日期</th>
            <th width="25%" style="text-align:center;">移出经营异常名录原因</th>
            <th width="13%" style="text-align:center;">移出日期</th>
            <!--<th width="13%" style="text-align:center;">公示日期</th>-->
            <th width="19%" style="text-align:center;">作出决定机关</th>
        </tr>
    </table>
    <div id="excDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList" id="excTab">
                <tr>
                   <td width="5%" style="text-align:center;">1</td>
                    <td width="20%">通过登记的住所或者经营场所无法联系的</td>
                    <td width="13%" style="text-align:center">
                        2016年6月23日
                    </td>
                    <td width="25%"></td>
                    <td width="13%" style="text-align:center">

                    </td>
                    <!--<td width="13%" style="text-align:center">-->
                           <!--2016年6月23日-->
                        <!--</td>-->
                    <td width="19%">许昌市工商行政管理局</td>
                </tr>

    </table>
    </div>
            <table cellpadding="0" cellspacing="0" class="detailsList">
                <th colspan="4" style="text-align:right;">
                    <span style="color:blue"><<</span>
                        &nbsp;<a id="aexc1" href='javascript:goPage6("exc",1);' style="text-decoration:none"><span id="spanexc1" style="color:red">1</span></a>
                                                        &nbsp;<span style="color:blue">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                </th>
            </table>

    <br/>
</div>

<div id="yanzhongweifaqiye" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="6" style="text-align:center;">严重违法信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="15%" style="text-align:center;">列入严重违法失信企业名单原因</th>
            <th width="13%" style="text-align:center;">列入日期</th>
            <th width="20%" style="text-align:center;">移出严重违法失信企业名单原因</th>
            <th width="13%" style="text-align:center;">移出日期</th>
            <!--<th width="13%" style="text-align:center;">公示日期</th>-->
            <th width="23%" style="text-align:center;">作出决定机关</th>
        </tr>
    </table>
    <div id="serillDiv">
    <table cellpadding="0" cellspacing="0" class="detailsList">
     </table>
     </div>
    <br/>
</div>

<div id="xingzhengchufa" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="9" style="text-align:center;">行政处罚信息</th>
        </tr>
        <tr width="95%">
            <th width="5%"  style="text-align:center;">序号</th>
            <th width="10%" style="text-align:center;">行政处罚<br>决定书文号</th>
            <th width="20%" style="text-align:center;">违法行为类型</th>
            <th width="18%" style="text-align:center;">行政处罚内容</th>
            <th width="18%" style="text-align:center;">作出行政处罚<br>决定机关名称</th>
            <th width="12%" style="text-align:center;">作出行政处罚<br>决定日期</th>
            <th width="12%" style="text-align:center;">公示日期</th>
            <th width="12%" style="text-align:center;">详情</th>

        </tr>
    </table>
    <div id="punDiv">
        <table cellspacing="0" cellpadding="0" class="detailsList" id="punTab">
    </table>
    </div>
    <br/>
</div>

<div id="chouchaxinxi" style="display:none;height: 850px;width:930px;overflow: auto">
    <br/>
    <table cellpadding="0" cellspacing="0" class="detailsList">
        <tr width="95%">
            <th colspan="5" style="text-align:center;">抽查检查信息</th>
        </tr>
        <tr width="95%">
            <th width="5%" style="text-align:center;">序号</th>
            <th width="35%" style="text-align:center;">检查实施机关</th>
            <th width="10%" style="text-align:center;">类型</th>
            <th width="15%" style="text-align:center;">日期</th>
            <!--<th width="15%" style="text-align:center;">公示日期</th>-->
            <th width="25%" style="text-align:center;">结果</th>
        </tr>
     </table>
    <div id="spotCheckDiv">
    <table cellpadding="0" cellspacing="0" class="detailsList">
    </table>
    </div>

    <br/>
</div>

</div>
</div>
</div>
<br/> <br/>
<div class="banqun">
    版权所有：河南省工商行政管理局 <a target="_blank" style="color:red;text-decoration:underline;font-size:14px; " href="http://gsxt.haaic.gov.cn/phone.jspx">业务(技术)支持电话</a><br/>
    地址：郑州市花园路127号&nbsp;&nbsp;邮政编码：450008&nbsp;&nbsp;<span style="color:red">建议使用IE8及以上版本浏览器</span>
</div>
</body>
</html>
<script>
var pageNo1 = 1;
var pageNo2 = 1;
var pageNo3 = 1;
var pageNo4 = 1;
var pageNo5 = 1;//行政处罚
var pageNo6 = 1;//经营异常
function goPage1(flag, n) {
    var request = new ajax.Request();
    pageNo1 = n;
    setRed(flag, n);
    if (flag != null && flag == 'mem') {
        request.loadTextByGet("/QueryMemList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshMemList);
    } else if (flag != null && flag == 'child') {
        request.loadTextByGet("/QueryChildList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshChildList);
    }else if (flag != null && flag == 'alt') {
        request.loadTextByGet("/QueryAltList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshAltList);
    } else {
        request.loadTextByGet("/QueryInvList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshInvList);
    }

}
function goPage2(flag, n) {
    var request = new ajax.Request();
    pageNo2 = n;
    setRed(flag, n);
    if (flag != null && flag == 'mem') {
        request.loadTextByGet("/QueryMemList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshMemList);
    } else if (flag != null && flag == 'child') {
        request.loadTextByGet("/QueryChildList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshChildList);
    }else if (flag != null && flag == 'alt') {
        request.loadTextByGet("/QueryAltList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshAltList);
    } else {
        request.loadTextByGet("/QueryInvList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshInvList);
    }

}
function goPage3(flag, n) {
    var request = new ajax.Request();
    pageNo3 = n;
    setRed(flag, n);
    if (flag != null && flag == 'mem') {
        request.loadTextByGet("/QueryMemList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshMemList);
    } else if (flag != null && flag == 'child') {
        request.loadTextByGet("/QueryChildList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshChildList);
    }else if (flag != null && flag == 'alt') {
        request.loadTextByGet("/QueryAltList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshAltList);
    }else if (flag != null && flag == 'serill') {
        request.loadTextByGet("/QuerySerillList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshSerillList);
    }else if (flag != null && flag == 'spotCheck') {
        request.loadTextByGet("/QuerySpotCheckList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshSpotCheckList);
    } else {
        request.loadTextByGet("/QueryInvList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshInvList);
    }

}
    function slipFive(flag,lastMaxPage,totalPage,preOrNext) {
        var tpage = '1';
        var CurrentFirstPage ;
        if(preOrNext=='next'){
            if(lastMaxPage>=totalPage){
                CurrentFirstPage = (Math.floor(totalPage/5))*5+1;
            }else{
                CurrentFirstPage = lastMaxPage + 1;
            }
        }else{
            if(lastMaxPage<=5){
                CurrentFirstPage = 1;
            }else{
                 if(lastMaxPage%5==0){
                    CurrentFirstPage = lastMaxPage - 9;
                }else{
                    CurrentFirstPage = (Math.floor(lastMaxPage/5))*5 - 4;
                }
            }
        }
       	if (flag != null && flag == 'inv') {
            tpage = '1';
        } else if (flag != null && flag == 'mem') {
            tpage = '1';
        } else if (flag != null && flag == 'child') {
            tpage = '0';
        } else if (flag != null && flag == 'alt') {
            tpage = '0';
        }else if (flag != null && flag == 'pledge') {
            tpage = '0';
        }else if (flag != null && flag == 'mort') {
            tpage = '0';
        }else if (flag != null && flag == 'exc') {
            tpage = '1';
        }else if (flag != null && flag == 'serill') {
            tpage = '0';
        }else if (flag != null && flag == 'puun') {
            tpage = '0';
        }else if (flag != null && flag == 'spotCheck') {
            tpage = '0';
        }

        goShowNextFive(flag, tpage,CurrentFirstPage,totalPage);
    }
    function goShowNextFive(flag, n,CurrentFirstPage,totalPage) {
        var currentMaxPage = 0;
        if((CurrentFirstPage+4)<totalPage){
            currentMaxPage = CurrentFirstPage+4;
        } else{
            currentMaxPage = totalPage;
        }
        var request = new ajax.Request();
        if (flag != null && flag == 'inv') {
            var invPagination = document.getElementById("invPagination");
            invPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"inv\","+currentMaxPage+",1,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"ainv"+i+"\" href='javascript:goPage3(\"inv\","+i+");'><span id=\"spaninv"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"inv\","+currentMaxPage+",1,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            invPagination.innerHTML= innerHTML;
            goPage3("inv",CurrentFirstPage);
        }else if (flag != null && flag == 'mem') {
            var memPagination = document.getElementById("memPagination");
            memPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"mem\","+currentMaxPage+",1,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"amem"+i+"\" href='javascript:goPage3(\"mem\","+i+");'><span id=\"spanmem"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"mem\","+currentMaxPage+",1,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            memPagination.innerHTML= innerHTML;
            goPage3("mem",CurrentFirstPage);
        } else if (flag != null && flag == 'child') {
            var childPagination = document.getElementById("childPagination");
            childPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"child\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"achild"+i+"\" href='javascript:goPage3(\"child\","+i+");'><span id=\"spanchild"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"child\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            childPagination.innerHTML= innerHTML;
            goPage3("child",CurrentFirstPage);
        }else if (flag != null && flag == 'alt') {
            var altPagination = document.getElementById("altPagination");
            altPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"alt\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"aalt"+i+"\" href='javascript:goPage3(\"alt\","+i+");'><span id=\"spanalt"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"alt\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            altPagination.innerHTML= innerHTML;
            goPage3("alt",CurrentFirstPage);
        }else if (flag != null && flag == 'pledge') {
            var pledgePagination = document.getElementById("pledgePagination");
            pledgePagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"pledge\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"apledge"+i+"\" href='javascript:goPage9(\"pledge\","+i+");'><span id=\"spanpledge"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"pledge\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            pledgePagination.innerHTML= innerHTML;
            goPage9("pledge",CurrentFirstPage);
        }else if (flag != null && flag == 'mort') {
            var mortPagination = document.getElementById("mortPagination");
            mortPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"mort\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"amort"+i+"\" href='javascript:goPage10(\"mort\","+i+");'><span id=\"spanmort"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"mort\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            mortPagination.innerHTML= innerHTML;
            goPage10("mort",CurrentFirstPage);
        }else if (flag != null && flag == 'exc') {
            var excPagination = document.getElementById("excPagination");
            excPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"exc\","+currentMaxPage+",1,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"aexc"+i+"\" href='javascript:goPage6(\"exc\","+i+");'><span id=\"spanexc"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"exc\","+currentMaxPage+",1,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            excPagination.innerHTML= innerHTML;
            goPage6("exc",CurrentFirstPage);
        }else if (flag != null && flag == 'serill') {
            var serillPagination = document.getElementById("serillPagination");
            serillPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"serill\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"aserill"+i+"\" href='javascript:goPage3(\"serill\","+i+");'><span id=\"spanserill"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"serill\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            serillPagination.innerHTML= innerHTML;
            goPage3("serill",CurrentFirstPage);
        }else if (flag != null && flag == 'pun') {
            var punPagination = document.getElementById("punPagination");
            punPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"pun\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"apun"+i+"\" href='javascript:goPage5(\"pun\","+i+");'><span id=\"spanpun"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"pun\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            punPagination.innerHTML= innerHTML;
            goPage5("pun",CurrentFirstPage);
        }else if (flag != null && flag == 'spotCheck') {
            var spotCheckPagination = document.getElementById("spotCheckPagination");
            spotCheckPagination.innerHTML='';
            var innerHTML="<table cellpadding=\"0\" cellspacing=\"0\" class=\"detailsList\">"+
                "<th colspan=\"4\" style=\"text-align:right;\">";
            if(CurrentFirstPage==1){
                innerHTML += "<span style=\"color:blue\"><<</span>";
            }else{
                innerHTML += "<span><a href='javascript:slipFive(\"spotCheck\","+currentMaxPage+",0,\"pre\");'><<</a></span>";
            }
            for(var i=CurrentFirstPage;i<=currentMaxPage;i++){
                innerHTML += "    &nbsp;<a id=\"aspotCheck"+i+"\" href='javascript:goPage3(\"spotCheck\","+i+");'><span id=\"spanspotCheck"+i+"\">"+i+"</span></a>";
            }
            if(currentMaxPage==totalPage){
                innerHTML += "&nbsp;&nbsp;<span style=\"color:blue\">>></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }else{
                innerHTML += "&nbsp;&nbsp;<a href='javascript:slipFive(\"spotCheck\","+currentMaxPage+",0,\"next\");'><span>>></span></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+
                        "</th>"+
                        "</table>";
            }
            spotCheckPagination.innerHTML= innerHTML;
            goPage3("spotCheck",CurrentFirstPage);
        }

    }
function goPage4(flag, n) {
    var request = new ajax.Request();
    pageNo4 = n;
    setRed(flag, n);
    if (flag != null && flag == 'mem') {
        request.loadTextByGet("/QueryMemList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshMemList);
    } else if (flag != null && flag == 'child') {
        request.loadTextByGet("/QueryChildList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshChildList);
    }else if (flag != null && flag == 'alt') {
        request.loadTextByGet("/QueryAltList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshAltList);
    } else {
        request.loadTextByGet("/QueryInvList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100", refreshInvList);
    }

}
function goPage5(flag, n) {
    var request = new ajax.Request();
    pageNo5 = n;
    setRed(flag, n);
    request.loadTextByGet("/QueryPunList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100&ran="+Math.random(), refreshPunList);
}

function goPage6(flag, n) {
    var request = new ajax.Request();
    pageNo6 = n;
    setRed(flag, n);
    request.loadTextByGet("/QueryExcList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100&ran="+Math.random(), refreshExcList);
}


function refreshInvList(message) {
    var divTab = document.getElementById("invDiv");
    divTab.innerHTML = '';
    divTab.innerHTML = message.substr(1, message.length - 2);
}
function refreshMemList(message) {
    var memDiv = document.getElementById("memDiv");
    memDiv.innerHTML = '';
    memDiv.innerHTML = message.substr(1, message.length - 2);
}
function refreshChildList(message) {
    var childDiv = document.getElementById("childDiv");
    childDiv.innerHTML = '';
    childDiv.innerHTML = message.substr(1, message.length - 2);
}
function refreshAltList(message) {
    var altDiv = document.getElementById("altDiv");
    altDiv.innerHTML = '';
    altDiv.innerHTML = message.substr(1, message.length - 2);
    doExpand();
}
function refreshPunList(message) {
    var punDiv = document.getElementById("punDiv");
    punDiv.innerHTML = '';
    punDiv.innerHTML = message.substr(1, message.length - 2);
    doExpand_pun();
}
function refreshExcList(message) {
    var excDiv = document.getElementById("excDiv");
    excDiv.innerHTML = '';
    excDiv.innerHTML = message.substr(1, message.length - 2);
    doExpand_exc();
}
    function refreshSerillList(message) {
        var serillDiv = document.getElementById("serillDiv");
        serillDiv.innerHTML = '';
        serillDiv.innerHTML = message.substr(1, message.length - 2);
    }
    function refreshSpotCheckList(message) {
        var spotCheckDiv = document.getElementById("spotCheckDiv");
        spotCheckDiv.innerHTML = '';
        spotCheckDiv.innerHTML = message.substr(1, message.length - 2);
    }

function next1(flag) {
    var tpage = '1';
    if (flag != null && flag == 'mem') {
        tpage = '1';
    } else if (flag != null && flag == 'child') {
        tpage = '0';
    } else if (flag != null && flag == 'alt') {
        tpage = '0';
    }

    goPage1(flag, tpage);
}
function next2(flag) {
    var tpage = '1';
    if (flag != null && flag == 'mem') {
        tpage = '1';
    } else if (flag != null && flag == 'child') {
        tpage = '0';
    } else if (flag != null && flag == 'alt') {
        tpage = '0';
    }

    goPage2(flag, tpage);
}
function next3(flag) {
    var tpage = '1';
    if (flag != null && flag == 'mem') {
        tpage = '1';
    } else if (flag != null && flag == 'child') {
        tpage = '0';
    } else if (flag != null && flag == 'alt') {
        tpage = '0';
    }else if (flag != null && flag == 'serill') {
        tpage = '0';
    }else if (flag != null && flag == 'spotCheck') {
        tpage = '0';
    }

    goPage3(flag, tpage);
}
function next4(flag) {
    var tpage = '1';
    if (flag != null && flag == 'mem') {
        tpage = '1';
    } else if (flag != null && flag == 'child') {
        tpage = '0';
    } else if (flag != null && flag == 'alt') {
        tpage = '0';
    }

    goPage4(flag, tpage);
}
function next5(flag) {
    var tpage = '0';
    goPage5(flag, tpage);
}
function next6(flag) {
    var tpage = '1';
    goPage6(flag, tpage);
}



function pre1(flag) {
    goPage1(flag, 1);
}
function pre2(flag) {
    goPage2(flag, 1);
}
function pre3(flag) {
    goPage3(flag, 1);
}
function pre4(flag) {
    goPage4(flag, 1);
}
function pre5(flag) {
    goPage5(flag, 1);
}
function pre6(flag) {
    goPage6(flag, 1);
}


    function setRed(flag, n) {
        var currentFirstPage = Math.ceil(n/5)*5-4;
        var tpage = '1';
        if (flag != null && flag == 'inv') {
            tpage = '1';
        }else if (flag != null && flag == 'mem') {
            tpage = '1';
        } else if (flag != null && flag == 'child') {
            tpage = '0';
        } else if (flag != null && flag == 'alt') {
            tpage = '0';
        }else if (flag != null && flag == 'pun') {
            tpage = '0';
        }else if (flag != null && flag == 'exc') {
            tpage = '1';
        }else if (flag != null && flag == 'pledge') {
            tpage = '0';
        } else if (flag != null && flag == 'mort') {
            tpage = '0';
        }else if (flag != null && flag == 'serill') {
            tpage = '0';
        } else if (flag != null && flag == 'spotCheck') {
            tpage = '0';
        }

        for (var i = currentFirstPage; i <= (currentFirstPage+4); i++) {
            if(i>tpage){

            }else{
                document.getElementById("span" + flag + i).style.color = "";
                document.getElementById("a" + flag + i).style.textDecoration = "underline";
            }
        }
        document.getElementById("span" + flag + n).style.color = "red";
        document.getElementById("a" + flag + n).style.textDecoration = "none";
    }

var pageNo9 = 1;//股权出质
function goPage9(flag, n) {
    var request = new ajax.Request();
    pageNo9 = n;
    setRed(flag, n);
    request.loadTextByGet("/QueryPledgeList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100&ran=" + Math.random(), refreshPledgeList);
}

function next9(flag) {
    var tpage = '0';
    goPage9(flag, tpage);
}

function pre9(flag) {
    goPage9(flag, 1);
}

function refreshPledgeList(message) {
    var pledgeDiv = document.getElementById("pledgeDiv");
    pledgeDiv.innerHTML = '';
    pledgeDiv.innerHTML = message.substr(1, message.length - 2);
}

var pageNo10 = 1;//动产抵押
function goPage10(flag, n) {
    var request = new ajax.Request();
    pageNo10 = n;
    setRed(flag, n);
    request.loadTextByGet("/QueryMortList.jspx?pno=" + n + "&mainId=35FF188B1850F08EE053050A080A6100&ran=" + Math.random(), refreshMortList);
}

function next10(flag) {
    var tpage = '0';
    goPage10(flag, tpage);
}

function pre10(flag) {
    goPage10(flag, 1);
}

function refreshMortList(message) {
    var mortDiv = document.getElementById("mortDiv");
    mortDiv.innerHTML = '';
    mortDiv.innerHTML = message.substr(1, message.length - 2);
}
 //显示更多
    function showAlterMore(rowIndex,size){
        var a = document.getElementById("a"+rowIndex);
        var td = document.getElementById("td"+rowIndex);
        var detailTd = document.getElementById("detailTd"+rowIndex);
        var div = document.getElementById("xingzhengchufa");
        var ele = document.getElementById("7");
        var showDiv1 = document.getElementById("tr"+rowIndex+1);
        if(showDiv1.style.display=="none"){
            a.innerText="收起更多";
            td.rowSpan=size+1;
            detailTd.rowSpan=size+1;
        }else{
             a.innerText="更多";
             td.rowSpan = 2;
             detailTd.rowSpan = 2;
             changeStyle('tabs',ele);
             if(div.style.display="block"){
                div.style.display="";
             }else{
                 div.style.display="block";
             }
        }

        for(var i=1;i<size;i++){
            var showDiv = document.getElementById("tr"+rowIndex+i);
            if(showDiv.style.display=="none"){
                   showDiv.style.display="";
                }else{
                   showDiv.style.display="none";
                }
        }

    }
/*经营异常展开、缩起*/
    var arr_excIn = new Array();
    var arr_excOut = new Array();
    /*展开内容*/
    doExpand_exc();
/*变更信息展开、缩起*/
    var arr_altBe = new Array();
    var arr_altAf = new Array();
    /*展开内容*/

/*行政处罚 内容展开、收起*/
    var arr_punBasis = new Array();
    var arr_punResult = new Array();
    var arr_punAlt = new Array();

</script>
""" # 股份有限公司(非上市、自然人投资或控股)

soup = bs4.BeautifulSoup(''.join(html),"lxml")
html = soup.body



def printl(s):
    for x in s:
        print x
# 按标准缩进格式输出
# print(soup.prettify())

# 打印第一个title标签及内部所有元素
# print(soup.title)
    # <title>全国企业信用信息公示系统</title>
# print(soup.head)

# 打印title标签的名称
# print(soup.title.name)
    # #title

# 打印title标签的内容
# print(soup.title.string)
    #  全国企业信用信息公示系统

# 打印title的父元素的名称
# print(soup.title.parent.name)
    # #head

# 打印有"class"属性的li元素的class属性
# print(soup.li["class"])
    # ['current']
# 打印li标签的所有属性，返回字典
# print(soup.li.attrs)
    # {'style': 'margin-bottom:2px;', 'class': ['current']}

# 从文档中找到所有<a>标签的链接:
# for link in soup.find_all('a'):
#     print(link.get('href'))
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie

# 从文档中获取所有文字内容:
# print(soup.get_text())
# The Dormouse's story
#
# The Dormouse's story
#
# Once upon a time there were three little sisters; and their names were
# ...

# 整个文档的标签为document
# soup.name
    # u'[document]'

# 打印所有的ul标签及内部元素
# print(soup.find_all("ul"))

# 以列表返回head的子元素
# print(soup.head.contents)
# 返回head子元素的生成器
# print(soup.head.children)
# 返回head子孙元素的生成器
# print(soup.head.descendants)
# print(soup.tr)
# print(soup.tr.next_sibling)

# print(soup.find("th"))
# print(soup.tr.th)
'''if soup.find(text=re.compile(u"^个体工商户")):
    print("个体工商户")

if soup.find(text=re.compile(u"^个人独资企业")):
    print("个人独资企业")

if soup.find(text=re.compile(u"^有限责任公司（自然人独资）")):
    print("有限责任公司（自然人独资）")

if soup.find(text=re.compile(u"^股份有限公司")):
    print("股份有限公司(非上市、自然人投资或控股)")
print soup.find_all("table")
'''
# print(soup.find(id="jibenxinxi"))
#for x in soup.find_all(re.compile('td')):
#    print x
#printl(soup.find_all(id = "jibenxinxi"))
#printl(soup.find_all(string="备案信息"))
#printl(soup.find_all(string=re.compile("411391616090340")))
#printl(soup.find_all("th"))
#printl(soup.find_all(re.compile('td'),{"width"="20%"}))
#printl(soup.find_all("div", id = "jibenxinxi"))
#printl(soup.find_all(attrs={"data-foo": "value"}))
#printl(soup.find_all(string=""))








"""
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class HnqyxySpider(scrapy.Spider):
    name = "hnqyxy"
    start_urls = [("http://222.143.24.157/exceptionInfoSelect.jspx?pageNo="+str(i)) for i in xrange(20)]

    rules = (
        Rule(LinkExtractor(allow=('businessPublicity\.jspx',),)))

    def parse(self, response):
        print response.headers()
"""