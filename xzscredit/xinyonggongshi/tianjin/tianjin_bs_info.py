#!/usr/bin/env python
# coding:utf-8
'''
天津市信用信息公示系统
企业详情页面解析
'''

import re
from bs4 import BeautifulSoup
import requests




if __name__ == '__main__':
    # url = "http://tjcredit.gov.cn/platform/saic/baseInfo.json?entId=349DDA405B5E0231E04400306EF52828&departmentId=scjgw&infoClassId=dj"
    # r = requests.get(url)
    # a = r.text
    a = '''      <table cellspacing="0" cellpadding="0" class="result-table" >
      	<tr><td colspan="4" class="bg title" style="text-align:center;">基本信息 </td></tr>
        <tr>
          <td class="bg" width="22%">营业执照注册号</br>统一社会信用代码</td>
          <td class="" width="30%">
          120000000001439<br/>
          91120116722950227Y
          </td>
          <td class="bg" >名称</td>
          <td class="" width="30%">海洋石油工程股份有限公司</td>
        </tr>
        <tr>
          <td class="bg" >类型</td>
        <td class="" >股份有限公司(上市)    </td>
          <td class="bg" width="20%">法定代表人</td>
           <td class="" >周学仲</td>
		</tr>
        <tr>
          <td class="bg" >注册资本</td>
          <td class="" >442135.48万人民币</td>
		  <td class="bg" width="20%">成立日期</td>
          <td class="" >20000420</td>
        </tr>
        <tr>
          <td class="bg" >住所</td>
          <td class="" colspan="3">天津空港经济区西二道82号丽港大厦裙房二层202-F105室</td>
        </tr>
        <tr>
        	<td class="bg" >营业期限自</td>
            <td class="" >20000420</td>
          <td class="bg" >营业期限至</td>
          <td class="" >20500419</td>
        </tr>
        <tr>
      <td class="bg" >经营范围<br/></td>
      <td class="" colspan="3">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输；自有房屋租赁；钢材、管件、电缆、阀门、仪器仪表、五金交电销售；电仪自动化产品的研发、制造及销售。（依法须经批准的项目，经相关部门批准后方可开展经营活动）</td>
        </tr>
        <tr>
			<td class="bg" >登记机关</td>
			<td class="" >天津市自由贸易试验区市场和质量监督管理局</td>
			<td class="bg" >核准日期</td>
			<td class="" > 20150213</td>
		</tr>
		  <tr>
			<td class="bg" >登记状态</td>
			<td class="" >存续</td>
			<td class="" ></td>
			<td class="" ></td>
        </tr>
      </table><table cellspacing="0" cellpadding="0" class="result-table"  id="touziren" >
	<tr>
		<td class="bg title"  colspan="5" style="text-align:center;">
			股东信息<br>
			<span style="text-align:center;font-weight:normal;font-size:12px;">
				股东的出资信息截止2014年2月28日。2014年2月28日之后工商只公示股东姓名，其他出资信息由企业自行公示。
			</span>
		</td>
	</tr>
	<tbody id="table2">
		<tr width="95%">
			<td class="bg title"  width="20%" style="text-align:center;">股东类型</td>
			<td class="bg title"  width="20%" style="text-align:center;">股东</td>
			<td class="bg title"  width="20%" style="text-align:center;">证照/证件类型</td>
			<td class="bg title"  width="20%" style="text-align:center;">证照/证件号码</td>
			<td class="bg title"  width="20%" style="text-align:center;">详情</td>
		</tr>
	    					<tr>
						<td width="20%" style="text-align:center;">企业法人</td>
						<td width="20%" style="text-align:center;">中国海洋石油渤海公司</td>
						<td width="20%" style="text-align:center;">  企业法人营业执照(非公司)</td>
						<td width="20%" style="text-align:center;">1200001001019</td>
						<td width="20%" style="text-align:center;">
							<a style="cursor:pointer;color:blue;" href="javascript:void(0);" onclick="CheckDetail.getShareHolder('8171dbd953ee8a3c002dde67303c6548','349DDA405B5E0231E04400306EF52828')">
							详情
							</a>
						</td>
					</tr>
					<tr>
						<td width="20%" style="text-align:center;">企业法人</td>
						<td width="20%" style="text-align:center;">中国海洋石油总公司</td>
						<td width="20%" style="text-align:center;">  企业法人营业执照(非公司)</td>
						<td width="20%" style="text-align:center;">1000001000104</td>
						<td width="20%" style="text-align:center;">
							<a style="cursor:pointer;color:blue;" href="javascript:void(0);" onclick="CheckDetail.getShareHolder('8171dc0153ee8a3c0086e6f75ebaf807','349DDA405B5E0231E04400306EF52828')">
							详情
							</a>
						</td>
					</tr>
					<tr>
						<td width="20%" style="text-align:center;">企业法人</td>
						<td width="20%" style="text-align:center;">中国海洋石油南海西部公司</td>
						<td width="20%" style="text-align:center;">  企业法人营业执照(非公司)</td>
						<td width="20%" style="text-align:center;">4400001006166</td>
						<td width="20%" style="text-align:center;">
							<a style="cursor:pointer;color:blue;" href="javascript:void(0);" onclick="CheckDetail.getShareHolder('8171dba453ee8a3c00add8cd58bf7b87','349DDA405B5E0231E04400306EF52828')">
							详情
							</a>
						</td>
					</tr>
					<tr>
						<td width="20%" style="text-align:center;">其他投资者</td>
						<td width="20%" style="text-align:center;">社会公众股</td>
						<td width="20%" style="text-align:center;">其他</td>
						<td width="20%" style="text-align:center;">无</td>
						<td width="20%" style="text-align:center;">
							<a style="cursor:pointer;color:blue;" href="javascript:void(0);" onclick="CheckDetail.getShareHolder('8171dbed53ee8a3c019050c403261292','349DDA405B5E0231E04400306EF52828')">
							详情
							</a>
						</td>
					</tr>
	</tbody>
</table><table  class="result-table">
	<tr>
		<td class="bg title" style="text-align:center;" colspan="4">变更信息</td>
	</tr>
	<tr>
		<td class="bg title" style="text-align:center;">变更事项</td>
		<td class="bg title" style="text-align:center;">变更前内容</td>
		<td class="bg title" style="text-align:center;">变更后内容</td>
		<td class="bg title" style="text-align:center;">变更日期</td>
		</tr>
		<tr>
			<td style="text-align:center;">经营范围</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输；自有房屋租赁；钢材、管件、电缆、阀门、仪器仪表、五金交电销售。（以上经营范围涉及行业许可的凭许可证件，在有效期内经营，国家有专项专营规定的按规定办理）</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输；自有房屋租赁；钢材、管件、电缆、阀门、仪器仪表、五金交电销售；电仪自动化产品的研发、制造及销售。（依法须经批准的项目，经相关部门批准后方可开展经营活动）</td>
			<td style="text-align:center;">20140926</td>
		</tr>
		<tr>
			<td style="text-align:center;">一般经营项目</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员；自有房屋租赁；钢材、管件、电缆、阀门、仪器仪表、五金交电销售。</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员；自有房屋租赁；钢材、管件、电缆、阀门、仪器仪表、五金交电销售；电仪自动化产品的研发、制造及销售。（依法须经批准的项目，经相关部门批准后方可开展经营活动）。</td>
			<td style="text-align:center;">20140926</td>
		</tr>
		<tr>
			<td style="text-align:center;">登记机关</td>
			<td style="text-align:center;">天津市滨海新区工商行政管理局</td>
			<td style="text-align:center;">天津市自由贸易试验区市场和质量监督管理局</td>
			<td style="text-align:center;">20150213</td>
		</tr>
		<tr>
			<td style="text-align:center;">管辖单位</td>
			<td style="text-align:center;">天津市滨海新区工商行政管理局</td>
			<td style="text-align:center;">天津市自由贸易试验区市场和质量监督管理局</td>
			<td style="text-align:center;">20150213</td>
		</tr>
		<tr>
			<td style="text-align:center;">许可信息</td>
			<td style="text-align:center;">空</td>
			<td style="text-align:center;">许可证名称: 国际海上运输船舶备案证明书</td>
			<td style="text-align:center;">20101124</td>
		</tr>
		<tr>
			<td style="text-align:center;">经营范围</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输（以上范围内国家有专营专项规定的按规定办理）。</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输（以上范围内国家有专营专项规定的按规定办理）。</td>
			<td style="text-align:center;">20101124</td>
		</tr>
		<tr>
			<td style="text-align:center;">实收资本</td>
			<td style="text-align:center;">324120.0</td>
			<td style="text-align:center;">388944.0</td>
			<td style="text-align:center;">20101124</td>
		</tr>
		<tr>
			<td style="text-align:center;">许可经营项目</td>
			<td style="text-align:center;">国内沿海普通货船运输</td>
			<td style="text-align:center;">国内沿海普通货船运输；国际航线普通货物运输</td>
			<td style="text-align:center;">20101124</td>
		</tr>
		<tr>
			<td style="text-align:center;">注册资金（万元）</td>
			<td style="text-align:center;">324120.0</td>
			<td style="text-align:center;">388944.0</td>
			<td style="text-align:center;">20101124</td>
		</tr>
		<tr>
			<td style="text-align:center;">经营范围</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输；自有房屋租赁（以上经营范围涉及行业许可的凭许可证件，在有效期内经营，国家有专项专营规定的按规定办理）</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输；自有房屋租赁；钢材、管件、电缆、阀门、仪器仪表、五金交电销售。（以上经营范围涉及行业许可的凭许可证件，在有效期内经营，国家有专项专营规定的按规定办理）</td>
			<td style="text-align:center;">20130325</td>
		</tr>
		<tr>
			<td style="text-align:center;">一般经营项目</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员；自有房屋租赁。</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员；自有房屋租赁；钢材、管件、电缆、阀门、仪器仪表、五金交电销售。</td>
			<td style="text-align:center;">20130325</td>
		</tr>
		<tr>
			<td style="text-align:center;">住所或经营场所信息</td>
			<td style="text-align:center;">住所(经营场所)：天津港保税区海滨十五路199号；场所(经营场所)产权：自有；</td>
			<td style="text-align:center;">住所(经营场所)：天津空港经济区西二道82号丽港大厦裙房二层202-F105室；场所(经营场所)产权：租赁单位产权房；</td>
			<td style="text-align:center;">20110810</td>
		</tr>
		<tr>
			<td style="text-align:center;">登记机关</td>
			<td style="text-align:center;">天津市工商行政管理局</td>
			<td style="text-align:center;">天津市滨海新区工商行政管理局</td>
			<td style="text-align:center;">20120117</td>
		</tr>
		<tr>
			<td style="text-align:center;">经营范围</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输（以上经营范围涉及行业许可的凭许可证件，在有效期内经营，国家有专项专营规定的按规定办理）</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输；自有房屋租赁（以上经营范围涉及行业许可的凭许可证件，在有效期内经营，国家有专项专营规定的按规定办理）</td>
			<td style="text-align:center;">20111125</td>
		</tr>
		<tr>
			<td style="text-align:center;">管辖单位</td>
			<td style="text-align:center;">天津市工商行政管理局</td>
			<td style="text-align:center;">天津市滨海新区工商行政管理局</td>
			<td style="text-align:center;">20120117</td>
		</tr>
		<tr>
			<td style="text-align:center;">一般经营项目</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员。</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员；自有房屋租赁。</td>
			<td style="text-align:center;">20111125</td>
		</tr>
		<tr>
			<td style="text-align:center;">住所</td>
			<td style="text-align:center;">天津港保税区海滨十五路199号</td>
			<td style="text-align:center;">天津空港经济区西二道82号丽港大厦裙房二层202-F105室</td>
			<td style="text-align:center;">20110810</td>
		</tr>
		<tr>
			<td style="text-align:center;">出资方式(实收资本)</td>
			<td style="text-align:center;">其他</td>
			<td style="text-align:center;">货币;其他</td>
			<td style="text-align:center;">20131014</td>
		</tr>
		<tr>
			<td style="text-align:center;">实收资本</td>
			<td style="text-align:center;">388944.0</td>
			<td style="text-align:center;">442135.48</td>
			<td style="text-align:center;">20131014</td>
		</tr>
		<tr>
			<td style="text-align:center;">出资方式(注册资本)</td>
			<td style="text-align:center;">其他</td>
			<td style="text-align:center;">货币;其他</td>
			<td style="text-align:center;">20131014</td>
		</tr>
		<tr>
			<td style="text-align:center;">注册资金（万元）</td>
			<td style="text-align:center;">388944.0</td>
			<td style="text-align:center;">442135.48</td>
			<td style="text-align:center;">20131014</td>
		</tr>
		<tr>
			<td style="text-align:center;">实收资本</td>
			<td style="text-align:center;">324120.0</td>
			<td style="text-align:center;">388944.0</td>
			<td style="text-align:center;">20101124</td>
		</tr>
		<tr>
			<td style="text-align:center;">许可信息</td>
			<td style="text-align:center;">空</td>
			<td style="text-align:center;">许可证名称: 国际海上运输船舶备案证明书</td>
			<td style="text-align:center;">20101124</td>
		</tr>
		<tr>
			<td style="text-align:center;">注册资金（万元）</td>
			<td style="text-align:center;">324120.0</td>
			<td style="text-align:center;">388944.0</td>
			<td style="text-align:center;">20101124</td>
		</tr>
		<tr>
			<td style="text-align:center;">管辖单位</td>
			<td style="text-align:center;">天津市滨海新区工商行政管理局</td>
			<td style="text-align:center;">天津市自由贸易试验区市场和质量监督管理局</td>
			<td style="text-align:center;">20150213</td>
		</tr>
		<tr>
			<td style="text-align:center;">一般经营项目</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员；自有房屋租赁；钢材、管件、电缆、阀门、仪器仪表、五金交电销售。</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员；自有房屋租赁；钢材、管件、电缆、阀门、仪器仪表、五金交电销售；电仪自动化产品的研发、制造及销售。（依法须经批准的项目，经相关部门批准后方可开展经营活动）。</td>
			<td style="text-align:center;">20140926</td>
		</tr>
		<tr>
			<td style="text-align:center;">注册资金（万元）</td>
			<td style="text-align:center;">388944.0</td>
			<td style="text-align:center;">442135.48</td>
			<td style="text-align:center;">20131014</td>
		</tr>
		<tr>
			<td style="text-align:center;">出资方式(注册资本)</td>
			<td style="text-align:center;">其他</td>
			<td style="text-align:center;">货币;其他</td>
			<td style="text-align:center;">20131014</td>
		</tr>
		<tr>
			<td style="text-align:center;">实收资本</td>
			<td style="text-align:center;">388944.0</td>
			<td style="text-align:center;">442135.48</td>
			<td style="text-align:center;">20131014</td>
		</tr>
		<tr>
			<td style="text-align:center;">出资方式(实收资本)</td>
			<td style="text-align:center;">其他</td>
			<td style="text-align:center;">货币;其他</td>
			<td style="text-align:center;">20131014</td>
		</tr>
		<tr>
			<td style="text-align:center;">经营范围</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输；自有房屋租赁（以上经营范围涉及行业许可的凭许可证件，在有效期内经营，国家有专项专营规定的按规定办理）</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输；自有房屋租赁；钢材、管件、电缆、阀门、仪器仪表、五金交电销售。（以上经营范围涉及行业许可的凭许可证件，在有效期内经营，国家有专项专营规定的按规定办理）</td>
			<td style="text-align:center;">20130325</td>
		</tr>
		<tr>
			<td style="text-align:center;">一般经营项目</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员；自有房屋租赁。</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员；自有房屋租赁；钢材、管件、电缆、阀门、仪器仪表、五金交电销售。</td>
			<td style="text-align:center;">20130325</td>
		</tr>
		<tr>
			<td style="text-align:center;">登记机关</td>
			<td style="text-align:center;">天津市滨海新区工商行政管理局</td>
			<td style="text-align:center;">天津市自由贸易试验区市场和质量监督管理局</td>
			<td style="text-align:center;">20150213</td>
		</tr>
		<tr>
			<td style="text-align:center;">经营范围</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输（以上范围内国家有专营专项规定的按规定办理）。</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输（以上范围内国家有专营专项规定的按规定办理）。</td>
			<td style="text-align:center;">20101124</td>
		</tr>
		<tr>
			<td style="text-align:center;">许可经营项目</td>
			<td style="text-align:center;">国内沿海普通货船运输</td>
			<td style="text-align:center;">国内沿海普通货船运输；国际航线普通货物运输</td>
			<td style="text-align:center;">20101124</td>
		</tr>
		<tr>
			<td style="text-align:center;">住所</td>
			<td style="text-align:center;">天津港保税区海滨十五路199号</td>
			<td style="text-align:center;">天津空港经济区西二道82号丽港大厦裙房二层202-F105室</td>
			<td style="text-align:center;">20110810</td>
		</tr>
		<tr>
			<td style="text-align:center;">住所或经营场所信息</td>
			<td style="text-align:center;">住所(经营场所)：天津港保税区海滨十五路199号；场所(经营场所)产权：自有；</td>
			<td style="text-align:center;">住所(经营场所)：天津空港经济区西二道82号丽港大厦裙房二层202-F105室；场所(经营场所)产权：租赁单位产权房；</td>
			<td style="text-align:center;">20110810</td>
		</tr>
		<tr>
			<td style="text-align:center;">管辖单位</td>
			<td style="text-align:center;">天津市工商行政管理局</td>
			<td style="text-align:center;">天津市滨海新区工商行政管理局</td>
			<td style="text-align:center;">20120117</td>
		</tr>
		<tr>
			<td style="text-align:center;">登记机关</td>
			<td style="text-align:center;">天津市工商行政管理局</td>
			<td style="text-align:center;">天津市滨海新区工商行政管理局</td>
			<td style="text-align:center;">20120117</td>
		</tr>
		<tr>
			<td style="text-align:center;">一般经营项目</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员。</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员；自有房屋租赁。</td>
			<td style="text-align:center;">20111125</td>
		</tr>
		<tr>
			<td style="text-align:center;">经营范围</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输（以上经营范围涉及行业许可的凭许可证件，在有效期内经营，国家有专项专营规定的按规定办理）</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输；自有房屋租赁（以上经营范围涉及行业许可的凭许可证件，在有效期内经营，国家有专项专营规定的按规定办理）</td>
			<td style="text-align:center;">20111125</td>
		</tr>
		<tr>
			<td style="text-align:center;">经营范围</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输；自有房屋租赁；钢材、管件、电缆、阀门、仪器仪表、五金交电销售。（以上经营范围涉及行业许可的凭许可证件，在有效期内经营，国家有专项专营规定的按规定办理）</td>
			<td style="text-align:center;">工程总承包；石油天然气（海洋石油工程、石油机械制造与修理工程、管道输送工程、油气处理加工工程、油气化工及综合利用工作）及建筑工程的设计；承担各类海洋石油建设工程的施工和其它海洋工程施工；承担各种类型的钢结构、网架工程的制作与安装；压力容器制造；经营本企业自产产品及技术的出口业务；经营本企业生产所需的原辅材料、仪器仪表、机械设备、零配件及技术的进口业务；经营进料加工和“三来一补”业务；承包境外海洋石油工程和境内国际招标工程；承包上述境外工程的勘测、咨询、设计和监理项目；上述境外工程所需的设备、材料出口；对外派遣实施上述境外工程所需的劳务人员、国内沿海普通货船运输；国际航线普通货物运输；自有房屋租赁；钢材、管件、电缆、阀门、仪器仪表、五金交电销售；电仪自动化产品的研发、制造及销售。（依法须经批准的项目，经相关部门批准后方可开展经营活动）</td>
			<td style="text-align:center;">20140926</td>
		</tr>
	</tr>
</table>'''
    print '1'
    soup = BeautifulSoup(a, 'lxml')
    print '2'
    print soup.table.tr
    for x in soup.find_all("td"):
        print x.string