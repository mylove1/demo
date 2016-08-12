exporting.js/*
 Highcharts JS v4.1.5 (2015-04-13)
 Exporting module

 (c) 2010-2014 Torstein Honsi

 License: www.highcharts.com/license
*/
(function(f){
var z=f.Chart,s=f.addEvent,A=f.removeEvent,B=HighchartsAdapter.fireEvent,j=f.createElement,p=f.discardElement,u=f.css,l=f.merge,m=f.each,q=f.extend,E=f.splat,F=Math.max,k=document,C=window,G=f.isTouchDevice,H=f.Renderer.prototype.symbols,r=f.getOptions(),x;q(r.lang,{
printChart:&quot;Print chart&quot;,downloadPNG:&quot;Download PNG image&quot;,downloadJPEG:&quot;Download JPEG image&quot;,downloadPDF:&quot;Download PDF document&quot;,downloadSVG:&quot;Download SVG vector image&quot;,contextButtonTitle:&quot;Chart context menu&quot;
});r.navigation=
{
menuStyle:{
border:&quot;1px solid #A0A0A0&quot;,background:&quot;#FFFFFF&quot;,padding:&quot;5px 0&quot;
},menuItemStyle:{
padding:&quot;0 10px&quot;,background:&quot;none&quot;,color:&quot;#303030&quot;,fontSize:G?&quot;14px&quot;:&quot;11px&quot;
},menuItemHoverStyle:{
background:&quot;#4572A5&quot;,color:&quot;#FFFFFF&quot;
},buttonOptions:{
symbolFill:&quot;#E0E0E0&quot;,symbolSize:14,symbolStroke:&quot;#666&quot;,symbolStrokeWidth:3,symbolX:12.5,symbolY:10.5,align:&quot;right&quot;,buttonSpacing:3,height:22,theme:{
fill:&quot;white&quot;,stroke:&quot;none&quot;
},verticalAlign:&quot;top&quot;,width:24
}
};r.exporting={
type:&quot;image/png&quot;,url:&quot;http://export.highcharts.com/&quot;,
buttons:{
contextButton:{
menuClassName:&quot;highcharts-contextmenu&quot;,symbol:&quot;menu&quot;,_titleKey:&quot;contextButtonTitle&quot;,menuItems:[{
textKey:&quot;printChart&quot;,onclick:function(){
this.print()
}
},{
separator:!0
},{
textKey:&quot;downloadPNG&quot;,onclick:function(){
this.exportChart()
}
},{
textKey:&quot;downloadJPEG&quot;,onclick:function(){
this.exportChart({
type:&quot;image/jpeg&quot;
})
}
},{
textKey:&quot;downloadPDF&quot;,onclick:function(){
this.exportChart({
type:&quot;application/pdf&quot;
})
}
},{
textKey:&quot;downloadSVG&quot;,onclick:function(){
this.exportChart({
type:&quot;image/svg+xml&quot;
})
}
}]
}
}
};
f.post=function(b,a,e){
var c,b=j(&quot;form&quot;,l({
method:&quot;post&quot;,action:b,enctype:&quot;multipart/form-data&quot;
},e),{
display:&quot;none&quot;
},k.body);for(c in a)j(&quot;input&quot;,{
type:&quot;hidden&quot;,name:c,value:a[c]
},null,b);b.submit();p(b)
};q(z.prototype,{
sanitizeSVG:function(b){
return b.replace(/zIndex=&quot;[^&quot;]+&quot;/g,&quot;&quot;).replace(/isShadow=&quot;[^&quot;]+&quot;/g,&quot;&quot;).replace(/symbolName=&quot;[^&quot;]+&quot;/g,&quot;&quot;).replace(/jQuery[0-9]+=&quot;[^&quot;]+&quot;/g,&quot;&quot;).replace(/url\([^#]+#/g,&quot;url(#&quot;).replace(/&lt;svg /,'&lt;svg xmlns:xlink=&quot;http://www.w3.org/1999/xlink&quot; ').replace(/ (NS[0-9]+\:)?href=/g,
&quot; xlink:href=&quot;).replace(/\n/,&quot; &quot;).replace(/&lt;\/svg&gt;.*?$/,&quot;&lt;/svg&gt;&quot;).replace(/(fill|stroke)=&quot;rgba\(([ 0-9]+,[ 0-9]+,[ 0-9]+),([ 0-9\.]+)\)&quot;/g,'$1=&quot;rgb($2)&quot; $1-opacity=&quot;$3&quot;').replace(/&amp;nbsp;/g,&quot; &quot;).replace(/&amp;shy;/g,&quot;­&quot;).replace(/&lt;IMG /g,&quot;&lt;image &quot;).replace(/height=([^&quot; ]+)/g,'height=&quot;$1&quot;').replace(/width=([^&quot; ]+)/g,'width=&quot;$1&quot;').replace(/hc-svg-href=&quot;([^&quot;]+)&quot;&gt;/g,'xlink:href=&quot;$1&quot;/&gt;').replace(/ id=([^&quot; &gt;]+)/g,'id=&quot;$1&quot;').replace(/class=([^&quot; &gt;]+)/g,'class=&quot;$1&quot;').replace(/ transform /g,&quot; &quot;).replace(/:(path|rect)/g,
&quot;$1&quot;).replace(/style=&quot;([^&quot;]+)&quot;/g,function(a){
return a.toLowerCase()
})
},getSVG:function(b){
var a=this,e,c,g,y,h,d=l(a.options,b);if(!k.createElementNS)k.createElementNS=function(a,b){
return k.createElement(b)
};c=j(&quot;div&quot;,null,{
position:&quot;absolute&quot;,top:&quot;-9999em&quot;,width:a.chartWidth+&quot;px&quot;,height:a.chartHeight+&quot;px&quot;
},k.body);g=a.renderTo.style.width;h=a.renderTo.style.height;g=d.exporting.sourceWidth||d.chart.width||/px$/.test(g)&amp;&amp;parseInt(g,10)||600;h=d.exporting.sourceHeight||d.chart.height||/px$/.test(h)&amp;&amp;
parseInt(h,10)||400;q(d.chart,{
animation:!1,renderTo:c,forExport:!0,width:g,height:h
});d.exporting.enabled=!1;delete d.data;d.series=[];m(a.series,function(a){
y=l(a.options,{
animation:!1,enableMouseTracking:!1,showCheckbox:!1,visible:a.visible
});y.isInternal||d.series.push(y)
});b&amp;&amp;m([&quot;xAxis&quot;,&quot;yAxis&quot;],function(a){
m(E(b[a]),function(b,c){
d[a][c]=l(d[a][c],b)
})
});e=new f.Chart(d,a.callback);m([&quot;xAxis&quot;,&quot;yAxis&quot;],function(b){
m(a[b],function(a,d){
var c=e[b][d],g=a.getExtremes(),h=g.userMin,g=g.userMax;c&amp;&amp;
(h!==void 0||g!==void 0)&amp;&amp;c.setExtremes(h,g,!0,!1)
})
});g=e.container.innerHTML;d=null;e.destroy();p(c);g=this.sanitizeSVG(g);return g=g.replace(/(url\(#highcharts-[0-9]+)&amp;quot;/g,&quot;$1&quot;).replace(/&amp;quot;/g,&quot;'&quot;)
},getSVGForExport:function(b,a){
var e=this.options.exporting;return this.getSVG(l({
chart:{
borderRadius:0
}
},e.chartOptions,a,{
exporting:{
sourceWidth:b&amp;&amp;b.sourceWidth||e.sourceWidth,sourceHeight:b&amp;&amp;b.sourceHeight||e.sourceHeight
}
}))
},exportChart:function(b,a){
var e=this.getSVGForExport(b,a),b=l(this.options.exporting,
b);f.post(b.url,{
filename:b.filename||&quot;chart&quot;,type:b.type,width:b.width||0,scale:b.scale||2,svg:e
},b.formAttributes)
},print:function(){
var b=this,a=b.container,e=[],c=a.parentNode,g=k.body,f=g.childNodes;if(!b.isPrinting)b.isPrinting=!0,B(b,&quot;beforePrint&quot;),m(f,function(a,b){
if(a.nodeType===1)e[b]=a.style.display,a.style.display=&quot;none&quot;
}),g.appendChild(a),C.focus(),C.print(),setTimeout(function(){
c.appendChild(a);m(f,function(a,b){
if(a.nodeType===1)a.style.display=e[b]
});b.isPrinting=!1;B(b,&quot;afterPrint&quot;)
},
1E3)
},contextMenu:function(b,a,e,c,g,f,h){
var d=this,l=d.options.navigation,D=l.menuItemStyle,n=d.chartWidth,o=d.chartHeight,k=&quot;cache-&quot;+b,i=d[k],t=F(g,f),v,w,p,r=function(a){
d.pointer.inClass(a.target,b)||w()
};if(!i)d[k]=i=j(&quot;div&quot;,{
className:b
},{
position:&quot;absolute&quot;,zIndex:1E3,padding:t+&quot;px&quot;
},d.container),v=j(&quot;div&quot;,null,q({
MozBoxShadow:&quot;3px 3px 10px #888&quot;,WebkitBoxShadow:&quot;3px 3px 10px #888&quot;,boxShadow:&quot;3px 3px 10px #888&quot;
},l.menuStyle),i),w=function(){
u(i,{
display:&quot;none&quot;
});h&amp;&amp;h.setState(0);d.openMenu=
!1
},s(i,&quot;mouseleave&quot;,function(){
p=setTimeout(w,500)
}),s(i,&quot;mouseenter&quot;,function(){
clearTimeout(p)
}),s(document,&quot;mouseup&quot;,r),s(d,&quot;destroy&quot;,function(){
A(document,&quot;mouseup&quot;,r)
}),m(a,function(a){
if(a){
var b=a.separator?j(&quot;hr&quot;,null,null,v):j(&quot;div&quot;,{
onmouseover:function(){
u(this,l.menuItemHoverStyle)
},onmouseout:function(){
u(this,D)
},onclick:function(){
w();a.onclick&amp;&amp;a.onclick.apply(d,arguments)
},innerHTML:a.text||d.options.lang[a.textKey]
},q({
cursor:&quot;pointer&quot;
},D),v);d.exportDivElements.push(b)
}
}),d.exportDivElements.push(v,
i),d.exportMenuWidth=i.offsetWidth,d.exportMenuHeight=i.offsetHeight;a={
display:&quot;block&quot;
};e+d.exportMenuWidth&gt;n?a.right=n-e-g-t+&quot;px&quot;:a.left=e-t+&quot;px&quot;;c+f+d.exportMenuHeight&gt;o&amp;&amp;h.alignOptions.verticalAlign!==&quot;top&quot;?a.bottom=o-c-t+&quot;px&quot;:a.top=c+f-t+&quot;px&quot;;u(i,a);d.openMenu=!0
},addButton:function(b){
var a=this,e=a.renderer,c=l(a.options.navigation.buttonOptions,b),g=c.onclick,k=c.menuItems,h,d,m={
stroke:c.symbolStroke,fill:c.symbolFill
},j=c.symbolSize||12;if(!a.btnCount)a.btnCount=0;if(!a.exportDivElements)a.exportDivElements=
[],a.exportSVGElements=[];if(c.enabled!==!1){
var n=c.theme,o=n.states,p=o&amp;&amp;o.hover,o=o&amp;&amp;o.select,i;delete n.states;g?i=function(){
g.apply(a,arguments)
}:k&amp;&amp;(i=function(){
a.contextMenu(d.menuClassName,k,d.translateX,d.translateY,d.width,d.height,d);d.setState(2)
});c.text&amp;&amp;c.symbol?n.paddingLeft=f.pick(n.paddingLeft,25):c.text||q(n,{
width:c.width,height:c.height,padding:0
});d=e.button(c.text,0,0,i,n,p,o).attr({
title:a.options.lang[c._titleKey],&quot;stroke-linecap&quot;:&quot;round&quot;
});d.menuClassName=b.menuClassName||
&quot;highcharts-menu-&quot;+a.btnCount++;c.symbol&amp;&amp;(h=e.symbol(c.symbol,c.symbolX-j/2,c.symbolY-j/2,j,j).attr(q(m,{
&quot;stroke-width&quot;:c.symbolStrokeWidth||1,zIndex:1
})).add(d));d.add().align(q(c,{
width:d.width,x:f.pick(c.x,x)
}),!0,&quot;spacingBox&quot;);x+=(d.width+c.buttonSpacing)*(c.align===&quot;right&quot;?-1:1);a.exportSVGElements.push(d,h)
}
},destroyExport:function(b){
var b=b.target,a,e;for(a=0;a&lt;b.exportSVGElements.length;a++)if(e=b.exportSVGElements[a])e.onclick=e.ontouchstart=null,b.exportSVGElements[a]=e.destroy();for(a=
0;a&lt;b.exportDivElements.length;a++)e=b.exportDivElements[a],A(e,&quot;mouseleave&quot;),b.exportDivElements[a]=e.onmouseout=e.onmouseover=e.ontouchstart=e.onclick=null,p(e)
}
});H.menu=function(b,a,e,c){
return[&quot;M&quot;,b,a+2.5,&quot;L&quot;,b+e,a+2.5,&quot;M&quot;,b,a+c/2+0.5,&quot;L&quot;,b+e,a+c/2+0.5,&quot;M&quot;,b,a+c-1.5,&quot;L&quot;,b+e,a+c-1.5]
};z.prototype.callbacks.push(function(b){
var a,e=b.options.exporting,c=e.buttons;x=0;if(e.enabled!==!1){
for(a in c)b.addButton(c[a]);s(b,&quot;destroy&quot;,b.destroyExport)
}
})
})(Highcharts);