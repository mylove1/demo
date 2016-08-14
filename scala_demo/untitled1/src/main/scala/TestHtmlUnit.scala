import java.net.URL
import com.gargoylesoftware.htmlunit._
import com.gargoylesoftware.htmlunit.html.HtmlPage
import com.gargoylesoftware.htmlunit.html.HtmlForm
import com.gargoylesoftware.htmlunit.html.HtmlSubmitInput
import com.gargoylesoftware.htmlunit.html.HtmlTextInput

import scala.io.Source
/**
  * Created by cooper on 2016/8/10.
  */
object TestHtmlUnit {

  def main(args: Array[String]): Unit = {
    println("start")

//    设置代理IP
//    val webClient = new WebClient(BrowserVersion.CHROME, "119.6.136.122", 83)

    val webClient = new WebClient(BrowserVersion.CHROME)


//    val request = WebRequest
//    request.setProxyHost("")

//    试着去设置代理IP
//    val proxyconfig = ProxyConfig
//    webClient.getOptions.setProxyConfig(proxyconfig)
    webClient.getOptions.setCssEnabled(false)

//    webClient.getOptions().setJavaScriptEnabled(true); //启用JS解释器，默认为true
//    webClient.getOptions().setCssEnabled(false); //禁用css支持
//    webClient.getOptions().setThrowExceptionOnScriptError(false); //js运行错误时，是否抛出异常
//    webClient.getOptions().setTimeout(10000); //设置连接超时时间 ，单位毫秒，这里是10S。如果为0，则无限期等待





    println("start get html")
//    val page: HtmlPage = webClient.getPage("http://nailcui.com/")
    val page: HtmlPage = webClient.getPage("http://www.ip181.com/")
//    val page: HtmlPage = webClient.getPage("http://www.csszengarden.com/")
//    val page: HtmlPage = webClient.getPage("http://192.168.100.55:9999/")

//     构造请求
//    val url = new URL("http://httpbin.org/ip")
//    val requestSetting = new WebRequest(url, HttpMethod.GET)
//    requestSetting.setProxyHost("119.6.136.122")
//    requestSetting.setProxyPort(83)



//    对于非标准html格式的页面进行获取
//    val page: Page = webClient.getPage(requestSetting)
//    println("ok")
//    println(page.getWebResponse.getContentAsString())
//    println(page.isHtmlPage)


//<<<<<<<<<<<<<<< 页面解析 >>>>>>>>>>>>>>>>>>>

//    val pageXml = page.asXml(); //以xml的形式获取响应文本
//    println(pageXml)


//    通过XPath获取网页元素
//    val tdtext = page.getByXPath("//td/text()")
//    for (td <- 0 until tdtext.size()) println(tdtext.get(td))

//    运行出错
//    val div1 = page.getByXPath("//tr").get(0)
//    println(div1.asXml())



//    val domNodeList = page.getElementsByName("head")
//    val domElement = domNodeList.get(0)
//    println(domElement.asText())

//    for (i <- 0 to domNodeList.size()){
//      val domElement = domNodeList.get(i)
//      println(domElement.asText())
//    }

//    println(page.getUrl)    //返回网页的地址
//    page.getTitleText    //返回网页title内容
//    val pagetext = page.asText()  //返回网页的可打印字符，包括title
//    val pageBody = page.getBody()   //返回body头标签，例：HtmlBody[<body id="css-zen-garden">]
//    val pagea = page.getDocumentElement   //返回html头标签，例：HtmlHtml[<html lang="en">]
//    val pageb = page.getBaseURL   //返回网页的地址
//    val pagec = page.getDocumentURI   //暂时异常page.getDocumentURI暂时未实现
//    val paged = page.getDomConfig
//    println(paged)
//    println(pagetext)
//    println(pageBody)
//    println("------")
//    println(pagea)
//    println(pageb)
//    println(pagec)
    println("stop")
    webClient.close()

  }
}
