# coding:utf-8
import re
a = '''<!DOCTYPEHTML><html><head><metahttp-equiv="X-UA-Compatible"content="IE=EmulateIE8;IE=EmulateIE9"><metaname="renderer"content="webkit|ie-comp|ie-stand"><metahttp-equiv="Content-Type"content="text/html;charset=utf-8"><metaname="viewport"content="width=device-width"><metaname="Keywords"content="招标采购信息,招标公告,求购信息,采购商,中国国际招标网，国际招标"/><metaname="Description"content="中国国际招标网是中国最大的电子招投标行政监督和公共服务平台，经国家商务部授权的电子招投标平台。提供国际招标、采购信息和网上交易以及相关的专业咨询服务。"/><title>招标项目-中国国际招标网</title><metahttp-equiv="X-UA-Compatible"content="IE=EmulateIE8"/><linkrel="stylesheet"href="http://staticfile.chinabidding.com/css/search/searchBidProject.css"type="text/css"/></head><body><script>varstaticContextPath='http://staticfile.chinabidding.com';varcontextPath='http://www.chinabidding.com';</script><divclass="wraper"><!--topheaderbar--><metahttp-equiv="content-script-type"content="text/javascript"><linkrel="stylesheet"href="http://staticfile.chinabidding.com/css/common.css"type="text/css"/><linkrel="stylesheet"href="http://staticfile.chinabidding.com/css/ui-dialog.css"type="text/css"><divid="top-header"class="top-headerspan-all"><ulclass="info-list"><liclass="list-itemfirst"><dlclass="horizontal"><dtclass="welcome"><spanclass="welcome-info"id="topName">您好，欢迎来到中国国际招标网</span></dt><ddclass="top-login"id="topLogin"><spanclass=""><ahref="http://www.chinabidding.com/bid/index/loginIndex.htm"title="请登录">请登录</a></span><spanclass=""><ahref="http://register.chinabidding.com/simple/webRegister/index.view"target="_blank"title="请注册">免费注册</a></span></dd></dl></li><liclass="list-itemlast"><dlclass="horizontal"><dtclass="top-language"><spanclass=""><ahref="http://www.chinabidding.com"title="中国际招标网">首页</a><i>|</i><ahref="http://enicb.ebnew.com/emain.jhtml"target="_blank"title="English">English</a></span></dt><ddclass="top-tell"><span>客服：</span>010-58851111-606</dd><ddclass="top-tell"><span>投诉：</span>010-58851111-618/887</dd><ddclass="top-tell"><span><aclass="as-report"href="#"company-name=""id="reportTop"title="举报信箱"><spanclass="welcome-info">举报信箱</span></a></span></dd></dl></li></ul></div><scripttype="text/javascript"src="http://staticfile.chinabidding.com/js/plugin/jquery/jquery.js"></script><scripttype="text/javascript"src="http://staticfile.chinabidding.com/js/plugin/dialog/dialog-min.js"></script><scripttype="text/javascript"src="http://staticfile.chinabidding.com/js/common/top.js"></script><script>document.write('<scr'+'ipttype="text/javascript"src="http://www.chinabidding.com/bid/login/loginTop.htm"></scr'+'ipt>');window.onerror=function(){;returntrue;}</script><!--topheaderbarend--><!--header-areaincludelogo,search--><divid="header"class="header"><dlclass="horizontal"><dt><ahref="http://www.chinabidding.com"class="site-logo">中国国际招标网</a></dt><ddclass="site-search"><divclass="as-tab"><ulclass="as-tab-navs"><liclass="as-tab-nav-itemon"><ahref="">招标项目<spanclass="icon"></span></a></li><liclass="as-tab-nav-item"><ahref="">资讯<spanclass="icon"></span></a></li><liclass="as-tab-nav-item"><ahref="">招标机构<spanclass="icon"></span></a></li></ul><divclass="as-tab-conts"><divclass="as-tab-cont-itemon"><divclass="search-boxwell"><fieldset><legendclass="none">项目名称搜索</legend><formname="projSearchForm"id="projSearchForm"action="http://www.chinabidding.com/search/proj.htm"method="POST"onsubmit="returnsubmitCheck(this);"><inputtype="text"name="fullText"id="fullText"placeholder="请输入项目名称，产品或企业名称"maxlength="50"class="bdsearch"><inputtype="hidden"name="poClass"value="BidNotice"/><buttonclass=""type="sbumit">搜索</button></form></fieldset></div></div><divclass="as-tab-cont-item"><divclass="search-boxwell"><fieldset><legendclass="none">资讯信息搜索</legend><formname="infoSearchForm"action="http://www.chinabidding.com/bid/info/search.htm"method="POST"onsubmit="returnsubmitCheck(this);"><inputtype="text"name="fullText"id="fullText"placeholder="请输入信息关键字"maxlength="50"class="bdsearch"><buttonclass=""type="sbumit">搜索</button></form></fieldset></div></div><divclass="as-tab-cont-item"><divclass="search-boxwell"><fieldset><legendclass="none">机构名称搜索</legend><formname="govSearchForm"action="http://www.chinabidding.com/bid/tool/bidorglist.htm"method="POST"onsubmit="returnsubmitCheck(this);"><inputtype="text"name="queryword"id="fullText"placeholder="请输入招标机构名称"maxlength="50"class="bdsearch"><buttonclass=""type="sbumit">搜索</button></form></fieldset></div></div></div><dlclass="horizontalhot-word-list"><spanstyle="float:left;padding-right:4px;padding-left:2px;color:#777">热门搜索：</span><dd><ahref="javascript:void(0);"onclick="projSearchSubmit('锅炉');"title="锅炉">锅炉</a></dd><dd><ahref="javascript:void(0);"onclick="projSearchSubmit('起重机');"title="起重机">起重机</a></dd><dd><ahref="javascript:void(0);"onclick="projSearchSubmit('CT');"title="CT">CT</a></dd><dd><ahref="javascript:void(0);"onclick="projSearchSubmit('医疗设备');"title="医疗设备">医疗设备</a></dd><dd><ahref="javascript:void(0);"onclick="projSearchSubmit('电梯');"title="电梯">电梯</a></dd></dl><scripttype="text/javascript">functionprojSearchSubmit(key){$("#projSearchForm").find("#fullText").val(key);$("#projSearchForm").submit();}functionsubmitCheck(sform){varfullText=$(sform).find("#fullText").val();varplaceholder=$(sform).find("#fullText").attr("placeholder");//解决ie8兼容性问题if(fullText==""||fullText==placeholder){returnfalse;}else{returntrue;}}</script></div></dd></dl></div><!--header-areaincludelogo,searchend--><!--sitenavigator--><divid="navigator"class="span-all"><dlclass="horizontal"><dt><ulclass="nav-list"><liclass="nav-item"><ahref="http://www.chinabidding.com">首页</a></li><liclass="nav-item"><ahref="http://www.chinabidding.com/gov">政务大厅</a></li><liclass="nav-item"><ahref="http://www.chinabidding.com/tender">业务大厅</a></li><liclass="nav-item"><ahref="http://www.chinabidding.com/server">实务大厅</a></li><liclass="nav-item"><ahref="http://www.chinabidding.com/info">服务大厅</a></li><liclass="nav-item"><ahref="http://bbs.chinabidding.com/"target="_blank">互动大厅</a></li><liclass="nav-itemlast"><ahref="http://www.chinabidding.com/bid/jump/aboutUs.htm">关于我们</a></li></ul></dt><dd><ulclass="quick-link"><liclass="quick-item"><ahref="http://www.chinabidding.com/bid/login/forward.htm"target="_blank">招标机构</a></li><liclass="quick-item"><ahref="http://www.chinabidding.com/bid/login/forward.htm"target="_blank">招标人</a></li><liclass="quick-item"><ahref="http://www.chinabidding.com/bid/login/forward.htm"target="_blank">投标人</a></li></ul></dd></dl></div><!--sitenavigatorend--><!--site-Content-area--><divid="site-content"class="cont-render"><divid="lab-show"class="lab-show"><divclass="site-bread">您的当前位置:<ahref="http://www.chinabidding.com">首页</a><span>></span>招标项目搜索</div><divclass="as-floor-normal"><divclass="as-md"><h3class="as-tit"><spanclass="txt">按条件选择</span><divclass="as-tit-panel"><ulclass="tag-list"><liclass="on">共找到<spanclass="red">118</span>条相关信息</li></ul></div><spanclass="icon-r-line"></span></h3><divclass="as-md-panel"><divclass="table-list"><divclass="table-list-panel"><fieldset><legendclass="none">政策法规搜索表单</legend><formaction="http://www.chinabidding.com/search/proj.htm"method="post"id="searchBidProjForm"onsubmit="returncheckValueSubmit(this);"><inputtype="hidden"name="poClass"id="poClass"value="BidNotice"/><inputtype="hidden"name="infoClassCodes"id="infoClassCodes"value="0105"/><inputtype="hidden"name="pubDate"id="pubDate"value=""/><inputtype="hidden"name="rangeType"id="rangeType"value=""/><ulclass="table-list-itemsas-index-list"><li><spanclass="as-index-tit">项目范围：</span><ahref="javascript:void(0);"onclick="searchRangeType('');"class="tag-lion">全部</a><ahref="javascript:void(0);"onclick="searchRangeType('1');"class="tag-li">国际招标</a><ahref="javascript:void(0);"onclick="searchRangeType('2');"class="tag-li">国内招标</a></li><li><spanclass="as-index-tit">项目分类：</span><ahref="javascript:void(0);"onclick="searchProjBidByProjType('0105','BidNotice');"class="tag-lion">招标公告</a><ahref="javascript:void(0);"onclick="searchProjBidByProjType('0106','BidChange');"class="tag-li">招标变更公告</a><ahref="javascript:void(0);"onclick="searchProjBidByProjType('0107','BidResult');"class="tag-li">评标结果公示</a><ahref="javascript:void(0);"onclick="searchProjBidByProjType('0108','BidResult');"class="tag-li">中标结果公告</a></li><li><spanclass="as-index-tit">发布时间：</span><ahref="javascript:void(0);"onclick="searchProjTime('');"class="tag-lion">全部</a><ahref="javascript:void(0);"onclick="searchProjTime('1');"class="tag-li">今天</a><ahref="javascript:void(0);"onclick="searchProjTime('2');"class="tag-li">近三天</a><ahref="javascript:void(0);"onclick="searchProjTime('3');"class="tag-li">近一周</a><ahref="javascript:void(0);"onclick="searchProjTime('4');"class="tag-li">近一月</a><ahref="javascript:void(0);"onclick="searchProjTime('5');"class="tag-li">近一年</a></li><liclass="last"><spanclass="first"><divclass="as-sele-box"name="tempS"><spanclass="as-sele-view"style="overflow:hidden;"></span><i></i></div><selectname="normIndustry"id="normIndustry"onchange="searchProjChange();"style="display:none"><optionselected="selected"value="">所有行业</option><optionvalue="01">农产品</option><optionvalue="02">能源(石油/石化/煤炭/新能源)</option><optionvalue="03">食品饮料烟草</option><optionvalue="04">纺织服装皮革</option><optionvalue="05">包装</option><optionvalue="06">工艺礼品玩具</option><optionvalue="07">化工</option><optionvalue="08">医药</option><optionvalue="09">五金</option><optionvalue="10">电子</option><optionvalue="11">机械设备</option><optionvalue="12">交通运输</option><optionvalue="13">办公用品</option><optionvalue="14">仪器仪表</option><optionvalue="15">IT、通讯及信息技术</option><optionvalue="16">工程建筑行业</option><optionvalue="17">安全防护</option><optionvalue="18">传媒、广电</option><optionvalue="19">家居行业</option><optionvalue="20">橡胶塑胶</option><optionvalue="21">印刷</option><optionvalue="22">冶金矿产</option><optionvalue="23">家用电器</option><optionvalue="24">电气</option><optionvalue="25">建筑建材</option><optionvalue="26">电力</option><optionvalue="27">运动、休闲</option><optionvalue="28">居民服务和其它服务业</option><optionvalue="29">商业贸易(综合类企业)</option><optionvalue="30">纸业</option><optionvalue="31">物流运输</option><optionvalue="32">通信及信息服务</option><optionvalue="33">批发零售、住宿餐饮</option><optionvalue="34">金融保险</option><optionvalue="35">房产物业</option><optionvalue="36">租赁和商务服务</option><optionvalue="37">科研技术和地质勘查护</option><optionvalue="38">水利、环境和公共设施管理</option><optionvalue="39">文化、教育、体育、娱乐服务</option><optionvalue="40">卫生、社会保障福利</option><optionvalue="41">国际、社会组织与公共管理</option><optionvalue="42">出版印刷</option><optionvalue="43">软件服务</option><optionvalue="44">咨询培训</option><optionvalue="45">维护清洗</option><optionvalue="46">会展服务</option><optionvalue="47">代理经营</option><optionvalue="48">网络通信</option><optionvalue="49">其他服务</option><optionvalue="50">环保设备</option></select><!--<iclass="iconicon-gray-ss"></i>--></span><span><divclass="as-sele-box"name="tempS"><spanclass="as-sele-view"></span><i></i></div><selectname="zoneCode"id="zoneCode"onchange="searchProjChange();"style="display:none"><optionselected="selected"value="">所有地区</option><optionvalue="11*12*13*14*15*">华北地区</option><optionvalue="11*">--北京</option><optionvalue="12*">--天津</option><optionvalue="13*">--河北</option><optionvalue="14*">--山西</option><optionvalue="15*">--内蒙古</option><optionvalue="21*22*23*">东北地区</option><optionvalue="21*">--辽宁</option><optionvalue="22*">--吉林</option><optionvalue="23*">--黑龙江</option><optionvalue="31*32*33*34*35*37*">华东地区</option><optionvalue="31*">--上海</option><optionvalue="32*">--江苏</option><optionvalue="33*">--浙江</option><optionvalue="34*">--安徽</option><optionvalue="35*">--福建</option><optionvalue="37*">--山东</option><optionvalue="36*41*42*43*">华中地区</option><optionvalue="36*">--江西</option><optionvalue="41*">--河南</option><optionvalue="42*">--湖北</option><optionvalue="43*">--湖南</option><optionvalue="44*45*46*">华南地区</option><optionvalue="44*">--广东</option><optionvalue="45*">--广西</option><optionvalue="46*">--海南</option><optionvalue="50*51*52*53*54*">西南地区</option><optionvalue="50*">--重庆</option><optionvalue="51*">--四川</option><optionvalue="52*">--贵州</option><optionvalue="53*">--云南</option><optionvalue="54*">--西藏</option><optionvalue="61*62*63*64*65*">西北地区</option><optionvalue="61*">--陕西</option><optionvalue="62*">--甘肃</option><optionvalue="63*">--青海</option><optionvalue="64*">--宁夏</option><optionvalue="65*">--新疆</option><optionvalue="71*81*82*">特别行政地区</option><optionvalue="71*">--台湾</option><optionvalue="81*">--香港</option><optionvalue="82*">--澳门</option></select><!--<iclass="iconicon-gray-ss"></i>--></span><span><divclass="as-sele-box"name="tempS"><spanclass="as-sele-view"></span><i></i></div><selectname="fundSourceCodes"id="fundSourceCodes"onchange="searchProjChange();"style="display:none"><optionselected="selected"value="">所有资金来源</option><optionvalue="010201">世行项目</option><optionvalue="010203">亚行项目</option><optionvalue="03">国债技改</option><optionvalue="0101*">外国政府贷款</option><optionvalue="07">现汇项目</option></select><!--<iclass="iconicon-gray-ss"></i>--></span><labelfor="keyword">关键字：</label><inputtype="text"name="fullText"id="fullText"placeholder="请输入搜索关键字"value="华为技术有限公司"maxlength="50"class="bdsearch"/><buttontype="submit"style="cursor:pointer;">搜索</button></li></ul></form><scripttype="text/javascript">functioncheckValueSubmit(sform){varfullText=$(sform).find("#fullText").val();varplaceholder=$(sform).find("#fullText").attr("placeholder");//解决ie8兼容性问题if(fullText==placeholder){$(sform).find("#fullText").val("");}returntrue;}</script></fieldset></div></div></div></div><divclass="span-f"><divclass="as-pager"><ulclass="as-pager-body"><li><aclass="as-pager-item"href="http://www.chinabidding.com/bidDetail/228819386.html"target="_blank"><h5class="as-p-tit"><spanclass="tag">[招标公告]</span><spanclass="txt"title="云浮新区管理委员会云浮市云计算数据中心一期工程PPP项目资格预审公告">云浮新区管理委员会云浮市云计算数据中心一期工程PPP项目资格预...</span><spanclass="time">发布时间：2016-07-22</span></h5><pclass="as-p-desc">根据《中华人民共和国政府采购法》等有关规定，经政府采购管理部门批准，将对云浮市云计算数据中心...</p><divclass="as-p-ft"><dlclass="horizontal"><dtclass="none">信息属性</dt><dd><spanclass="tag-attr">所属行业：<strong>建筑工程;网络工程</strong></span><spanclass="tag-attr">所属地区：<strong>广东省</strong></span></dd></dl></div></a></li><li><aclass="as-pager-item"href="http://www.chinabidding.com/bidDetail/228631415.html"target="_blank"><h5class="as-p-tit"><spanclass="tag">[招标公告]</span><spanclass="txt"title="山西省贸易学校实训基地建设中标公告">山西省贸易学校实训基地建设中标公告</span><spanclass="time">发布时间：2016-06-22</span></h5><pclass="as-p-desc">？我中心受采购人的委托，于****年*月**日组织了实训基地建设采购项目的国内公开招标，项目编号为...</p><divclass="as-p-ft"><dlclass="horizontal"><dtclass="none">信息属性</dt><dd><spanclass="tag-attr">所属行业：<strong>集成电路;电声器件;其它仪器仪表;传感器</strong></span><spanclass="tag-attr">所属地区：<strong>山西省</strong></span></dd></dl></div></a></li><li><aclass="as-pager-item"href="http://www.chinabidding.com/bidDetail/228610375.html"target="_blank"><h5class="as-p-tit"><spanclass="tag">[招标公告]</span><spanclass="txt"title="2016年山东联通客服系统硬件设备及应用软件维保服务采购项目招标公告（二次）">2016年山东联通客服系统硬件设备及应用软件维保服务采购项目招标...</span><spanclass="time">发布时间：2016-06-20</span></h5><pclass="as-p-desc">****年山东联通客服系统硬件设备及应用软件维保服务采购项目招标公告（二次）****年山东联通客服系...</p><divclass="as-p-ft"><dlclass="horizontal"><dtclass="none">信息属性</dt><dd><spanclass="tag-attr">所属行业：<strong>网络工程</strong></span><spanclass="tag-attr">所属地区：<strong>山东省</strong></span></dd></dl></div></a></li><li><aclass="as-pager-item"href="http://www.chinabidding.com/bidDetail/228603675.html"target="_blank"><h5class="as-p-tit"><spanclass="tag">[招标公告]</span><spanclass="txt"title="2016年山东联通客服系统硬件设备及应用软件维保服务采购项目招标公告（二次）">2016年山东联通客服系统硬件设备及应用软件维保服务采购项目招标...</span><spanclass="time">发布时间：2016-06-20</span></h5><pclass="as-p-desc">****年山东联通客服系统硬件设备及应用软件维保服务采购项目招标公告（二次）招标编号：鲁联通〔**...</p><divclass="as-p-ft"><dlclass="horizontal"><dtclass="none">信息属性</dt><dd><spanclass="tag-attr">所属行业：<strong>网络工程</strong></span><spanclass="tag-attr">所属地区：<strong>山东省</strong></span></dd></dl></div></a></li><li><aclass="as-pager-item"href="http://www.chinabidding.com/bidDetail/228566348.html"target="_blank"><h5class="as-p-tit"><spanclass="tag">[招标公告]</span><spanclass="txt"title="深圳供电局有限公司2016年深圳供电局统一通信高级应用建设工程项目华为eSpace统一通信系统终端用户永久授权（Licence）单一来源采购前公示">深圳供电局有限公司2016年深圳供电局统一通信高级应用建设工程项...</span><spanclass="time">发布时间：2016-06-15</span></h5><pclass="as-p-desc">一、采购人：深圳供电局有限公司二、采购项目名称：****年深圳供电局统一通信高级应用建设工程项目...</p><divclass="as-p-ft"><dlclass="horizontal"><dtclass="none">信息属性</dt><dd><spanclass="tag-attr">所属行业：<strong>其它设备</strong></span><spanclass="tag-attr">所属地区：<strong>广东省</strong></span></dd></dl></div></a></li><li><aclass="as-pager-item"href="http://www.chinabidding.com/bidDetail/228563444.html"target="_blank"><h5class="as-p-tit"><spanclass="tag">[招标公告]</span><spanclass="txt"title="2016年中国联通上海光纤交换机设备采购比选失败公告">2016年中国联通上海光纤交换机设备采购比选失败公告</span><spanclass="time">发布时间：2016-06-15</span></h5><pclass="as-p-desc">****年中国联通上海光纤交换机设备采购比选失败公告招标编号：SHLTGG-BJ-****-***-LB发布时间：***...</p><divclass="as-p-ft"><dlclass="horizontal"><dtclass="none">信息属性</dt><dd><spanclass="tag-attr">所属行业：<strong>计算机周边</strong></span><spanclass="tag-attr">所属地区：<strong>上海市</strong></span></dd></dl></div></a></li><li><aclass="as-pager-item"href="http://www.chinabidding.com/bidDetail/228519818.html"target="_blank"><h5class="as-p-tit"><spanclass="tag">[招标公告]</span><spanclass="txt"title="陕西SJQ视频会议系统建设项目（第四次）招标公告">陕西SJQ视频会议系统建设项目（第四次）招标公告</span><spanclass="time">发布时间：2016-06-12</span></h5><pclass="as-p-desc">陕西SJQ视频会议系统建设项目（第四次）招标公告招标编号：SXMX-Z-WZ-**-***-C发布时间：****-**-*...</p><divclass="as-p-ft"><dlclass="horizontal"><dtclass="none">信息属性</dt><dd><spanclass="tag-attr">所属行业：<strong>网络工程</strong></span><spanclass="tag-attr">所属地区：<strong>陕西省</strong></span></dd></dl></div></a></li><li><aclass="as-pager-item"href="http://www.chinabidding.com/bidDetail/228510662.html"target="_blank"><h5class="as-p-tit"><spanclass="tag">[招标公告]</span><spanclass="txt"title="广州供电局2016年第二批次通信设备类物资单一来源采购公示">广州供电局2016年第二批次通信设备类物资单一来源采购公示</span><spanclass="time">发布时间：2016-06-08</span></h5><pclass="as-p-desc">一、项目信息项目名称：广州供电局****年第二批次通信设备类物资单一来源采购招标编号：*******招...</p><divclass="as-p-ft"><dlclass="horizontal"><dtclass="none">信息属性</dt><dd><spanclass="tag-attr">所属行业：<strong>通讯产品</strong></span><spanclass="tag-attr">所属地区：<strong>广东省</strong></span></dd></dl></div></a></li><li><aclass="as-pager-item"href="http://www.chinabidding.com/bidDetail/228493296.html"target="_blank"><h5class="as-p-tit"><spanclass="tag">[招标公告]</span><spanclass="txt"title="2016年山东联通客服系统硬件设备及应用软件维保服务采购项目招标公告">2016年山东联通客服系统硬件设备及应用软件维保服务采购项目招标...</span><spanclass="time">发布时间：2016-06-07</span></h5><pclass="as-p-desc">****年山东联通客服系统硬件设备及应用软件维保服务采购项目招标公告招标编号：鲁联通〔****〕**号...</p><divclass="as-p-ft"><dlclass="horizontal"><dtclass="none">信息属性</dt><dd><spanclass="tag-attr">所属行业：<strong>网络工程</strong></span><spanclass="tag-attr">所属地区：<strong>山东省</strong></span></dd></dl></div></a></li><li><aclass="as-pager-item"href="http://www.chinabidding.com/bidDetail/228492882.html"target="_blank"><h5class="as-p-tit"><spanclass="tag">[招标公告]</span><spanclass="txt"title="2016年山东联通客服系统硬件设备及应用软件维保服务采购项目">2016年山东联通客服系统硬件设备及应用软件维保服务采购项目</span><spanclass="time">发布时间：2016-06-07</span></h5><pclass="as-p-desc">****年山东联通客服系统硬件设备及应用软件维保服务采购项目****年山东联通客服系统硬件设备及应用...</p><divclass="as-p-ft"><dlclass="horizontal"><dtclass="none">信息属性</dt><dd><spanclass="tag-attr">所属行业：<strong>网络工程</strong></span><spanclass="tag-attr">所属地区：<strong>山东省</strong></span></dd></dl></div></a></li></ul><divclass="as-pager-pagation"><formid="pagerSubmitForm"method="post"action="http://www.chinabidding.com/search/proj.htm"><inputtype="hidden"name="fullText"value="华为技术有限公司"/><inputtype="hidden"name="pubDate"value=""/><inputtype="hidden"name="infoClassCodes"value="0105"/><inputtype="hidden"name="normIndustry"value=""/><inputtype="hidden"name="zoneCode"value=""/><inputtype="hidden"name="fundSourceCodes"value=""/><inputtype="hidden"name="poClass"value="BidNotice"/><inputtype="hidden"name="rangeType"id="rangeType"value=""/><aclass="current"href="#">1</a><ahref="javascript:void(0)"onClick="searchSubmit(2)">2</a><ahref="javascript:void(0)"onClick="searchSubmit(3)">3</a><ahref="javascript:void(0)"onClick="searchSubmit(4)">4</a><ahref="javascript:void(0)"onClick="searchSubmit(5)">5</a><ahref="javascript:void(0)"onClick="searchSubmit(6)">6</a><ahref="#">...</a><ahref="javascript:void(0)"onClick="searchSubmit(12)">12</a><aclass="next"href="javascript:void(0)"onClick="searchSubmit(2)">下一页<iclass="icon"></i></a><inputtype="hidden"name="currentPage"id="currentPage"value="1"/><!--<spanclass=""><i>共12页&nbsp;&nbsp;</i><i>到第</i><inputtype="text"id="pageCount"/><i>页</i><buttontype="button"class="gobtn"onclick="doPage()">确定</button></span>--><scripttype="text/javascript">functionsearchSubmit(currentPage){$("#currentPage").val(currentPage);$("#pagerSubmitForm").submit();}</script></form></div></div></div><divclass="span-side"><divclass="label-boxtags-listt-b-bidder"><divclass="label-icon"><spanclass="icon"></span><spanclass="icon-xxx-txt">投标人</span></div><divclass="label-panel"><ulclass="t-t-o-list"><liclass="itemfirst"><ahref="http://www.chinabidding.com/bid/login/goto.htm?u=g"target="_blank">我要投标</a></li><liclass="itemsecend"><ahref="http://www.chinabidding.com/bid/login/goto.htm?u=g"target="_blank">我的投诉</a></li><liclass="itemthird"><ahref="http://www.chinabidding.com/bid/login/goto.htm?u=g"target="_blank">中标项目</a></li><liclass="item"><ahref="http://www.chinabidding.com/bid/login/goto.htm?u=g"target="_blank">未中标项目</a></li></ul></div></div><divclass="label-boxtags-listz-b-tenderee"><divclass="label-icon"><spanclass="icon"></span><spanclass="icon-xxx-txt">招标人</span></div><divclass="label-panel"><ulclass="t-t-o-list"><liclass="itemfirst"><ahref="http://www.chinabidding.com/bid/login/goto.htm?u=c"target="_blank">我要招标</a></li><liclass="itemsecend"><ahref="http://www.chinabidding.com/bid/login/goto.htm?u=c"target="_blank">项目进度</a></li><liclass="itemthird"><ahref="http://www.chinabidding.com/bid/login/goto.htm?u=c"target="_blank">中标项目</a></li><liclass="item"><ahref="http://www.chinabidding.com/bid/tool/bidorglist.htm?u=c"target="_blank">搜索代理</a></li></ul></div></div><divid="g-d-z-b"><h3class="as-tit-3"><iclass="iconicon-zhaobiao"></i><spanclass="tit">各地招标</span></h3><ul><li><dlclass="horizontal"><dtclass="state-tag-location"><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=11*12*13*14*15*"target="_blank">华北</a></dt><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=11*"target="_blank">北京</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=12*"target="_blank">天津</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=13*"target="_blank">河北</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=14*"target="_blank">山西</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=15*"target="_blank">内蒙古</a></dd></dl></li><li><dlclass="horizontal"><dtclass="state-tag-location"><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=21*22*23*"target="_blank">东北</a></dt><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=22*"target="_blank">吉林</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=21*"target="_blank">辽宁</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=23*"target="_blank">黑龙江</a></dd></dl></li><li><dlclass="horizontal"><dtclass="state-tag-location"><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=61*62*63*64*65*"target="_blank">西北</a></dt><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=61*"target="_blank">陕西</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=62*"target="_blank">甘肃</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=64*"target="_blank">宁夏</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=63*"target="_blank">青海</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=65*"target="_blank">新疆</a></dd></dl></li><li><dlclass="horizontal"><dtclass="state-tag-location"><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=31*32*33*34*35*37*"target="_blank">华东</a></dt><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=37*"target="_blank">山东</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=34*"target="_blank">安徽</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=31*"target="_blank">上海</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=32*"target="_blank">江苏</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=33*"target="_blank">浙江</a></dd></dl></li><li><dlclass="horizontal"><dtclass="state-tag-location"><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=36*41*42*43*"target="_blank">华中</a></dt><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=41*"target="_blank">河南</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=42*"target="_blank">湖北</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=43*"target="_blank">湖南</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=36*"target="_blank">江西</a></dd></dl></li><li><dlclass="horizontal"><dtclass="state-tag-location"><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=44*45*46*"target="_blank">华南</a></dt><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=44*"target="_blank">广东</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=45*"target="_blank">广西</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=46*"target="_blank">海南</a></dd></dl></li><li><dlclass="horizontal"><dtclass="state-tag-location"><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=50*51*52*53*54*"target="_blank">西南</a></dt><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=53*"target="_blank">云南</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=52*"target="_blank">贵州</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=51*"target="_blank">四川</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=50*"target="_blank">重庆</a></dd><dd><ahref="http://www.chinabidding.com/search/proj.htm?zoneCode=54*"target="_blank">西藏</a></dd></dl></li></ul></div></div></div></div></div><!--site-footer-area--><divid="site-footer"class="span-all"><divclass="site-info"><ulclass="service-link"><!--<li><ahref="http://www.chinabidding.com/bid/jump/aboutUs.htm"title="关于我们">关于我们</a></li><li><ahref="http://www.chinabidding.com/bid/jump/termsOfService.htm"title="服务条款">服务条款</a></li><li><ahref="http://www.chinabidding.com/bid/jump/legalNotices.htm"title="法律声明">法律声明</a></li><li><ahref="http://www.chinabidding.com/bid/jump/contactUs.htm"title="联系我们">联系我们</a></li>--></ul><divclass="copy-right"><p>©2001--2016&nbsp;&nbsp;<ahref="http://www.chinabidding.com"title="中国国际招标网">中国国际招标网</a>&nbsp;&nbsp;<ahref="http://www.miitbeian.gov.cn/publish/query/indexFirst.action"target="_blank"title="京ICP备12040737号-1">京ICP备12040737号-1</a>&nbsp;&nbsp;<span>京公网安备11010802015427号</span><br><ahref="http://www.mofcom.gov.cn/"target="_blank"title="中华人民共和国商务部授权">中华人民共和国商务部授权</a><ahref="http://bbs.chinabidding.com"style="color:#fff;">中国招标采购社区</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p></div><divclass="Certificate-bar"><ul><li><ahref="http://fzp.bjhd.gov.cn/tabid/179/Default.aspx"target="_blank"title="海淀分局防诈骗网"><iclass="iconicon-hdfj"></i></a></li><li><ahref="http://www.bj.cyberpolice.cn/index.do"target="_blank"title="网络110报警服务"><iclass="iconicon-wlbjfw"></i></a></li><li><ahref="http://www.hd315.gov.cn/"target="_blank"title="经营性网站备案信息"><iclass="iconicon-jyxwz"></i></a></li><scriptsrc="http://kxlogo.knet.cn/seallogo.dll?sn=e13031311010039503875e000000&amp;size=0"></script><li><ahref="https://ss.knet.cn/verifyseal.dll?sn=e13031311010039503875e000000&amp;ct=df&amp;a=1&amp;pa=0.20944633474573493"target="_blank"title="可信网站身份认证"><iclass="iconicon-kxwz"></i></a></li><li><ahref="http://www.ectrustprc.org.cn/certificate.id/certificater.php?id=10006716"target="_blank"title="中国电子商务诚信单位"><iclass="iconicon-dzswcxdw"></i></a></li><li><ahref="http://www.itrust.org.cn/yz/pjwx.asp?wm=1784803798"target="_blank"title="中国信用企业电子证书"><iclass="iconicon-dzzs"></i></a></li><li><aid="___szfw_logo___"href="https://search.szfw.org/cert/l/CX20140828005007005078"target="_blank"title="诚信网站"><iclass="iconicon-cxwz"></i></a></li><scripttype='text/javascript'>(function(){document.getElementById('___szfw_logo___').oncontextmenu=function(){returnfalse;}})();</script></ul></div></div><!--流量统计<script>varuserid_tjebnew='';vartype_tjebnew='a7ed016b16034defba31e00308ac1737';if(location.href.indexOf('chinabidding.com')!=-1){(function(){vara=document.createElement('script');a.type='text/javascript';a.async=true;a.src='http://cjjs.ebnew.com/cjjs/analysis.min.js';vars=document.getElementsByTagName('script')[0];s.parentNode.insertBefore(a,s);})();}</script>--><script>var_hmt=_hmt||[];(function(){varhm=document.createElement("script");hm.src="//hm.baidu.com/hm.js?5e642b7ea86f82ce1f7baa021d9b8809";vars=document.getElementsByTagName("script")[0];s.parentNode.insertBefore(hm,s);})();</script></div><!--site-footer-areaend--></div><scripttype="text/javascript"src="http://staticfile.chinabidding.com/js/plugin/require/require.js"data-main="http://staticfile.chinabidding.com/js/search/searchBidProject.js"></script></body></html>
'''
# ree = re.compile('title="(.*?)"><em>(.*?)</em>.*?</span><spanclass="time">发布时间：(.*?)</span></h5>.*?行业：<strong>(.*?)</strong></span><spanclass="tag-attr">所属地区：<strong>(.*?)</strong>')
ree = re.compile('class="tag">\[招标公告\]</span><spanclass="txt"title="(.*?)">.*?发布时间：(.*?)</span></h5><pclass="as-p-desc">(.*?)</p>.*?所属行业：<strong>(.*?)</strong></span>.*?所属地区：<strong>(.*?)</strong>')
list = ree.findall(a)
for x in list:
    print x