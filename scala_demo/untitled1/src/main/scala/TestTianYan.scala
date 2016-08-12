import java.net.URL

import com.gargoylesoftware.htmlunit._
import com.gargoylesoftware.htmlunit.html.HtmlPage
import com.gargoylesoftware.htmlunit.util.FalsifyingWebConnection
/**
  * Created by cooper on 2016/8/12.
  */
object TestTianYan {
  class SimpleFalsifyingWebConnection(webClient: WebClient) extends FalsifyingWebConnection(webClient) {
    override def getResponse(request: WebRequest): WebResponse = {
      val rs = super.getResponse(request)
      println(request.getUrl.toString)
//      if (request.getUrl.toString == "http://www.tianyancha.com:80/company/78957398.json") {
      if (request.getUrl.toString == "http://www.tianyancha.com:80/search/%E6%9D%AD%E5%B7%9E%E9%93%B6%E8%A1%8C%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8.json?&pn=1") {
        val targetJson = rs.getContentAsString
        println(targetJson)
      }
      rs
    }
  }

  def main(args: Array[String]): Unit = {
//    关闭htmlunit的日志，这两行设置之后不提示一些警告和信息
    java.util.logging.Logger.getLogger("com.gargoylesoftware.htmlunit").setLevel(java.util.logging.Level.OFF)
    java.util.logging.Logger.getLogger("org.apache.http").setLevel(java.util.logging.Level.OFF)

    val webClient = new WebClient(BrowserVersion.CHROME)
    new SimpleFalsifyingWebConnection(webClient)
    webClient.getCookieManager.setCookiesEnabled(true)
    webClient.getOptions.setCssEnabled(false)
    webClient.getOptions.setRedirectEnabled(true)
    webClient.getOptions.setJavaScriptEnabled(true)
    webClient.getOptions.setThrowExceptionOnFailingStatusCode(false)
    webClient.setAjaxController(new NicelyResynchronizingAjaxController())
    webClient.getOptions.setThrowExceptionOnScriptError(false)
//    val url = new URL("http://www.tianyancha.com/company/78957398")
    val url = new URL("http://www.tianyancha.com/search/%E6%9D%AD%E5%B7%9E%E9%93%B6%E8%A1%8C%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8?checkFrom=searchBox")
    val requestSetting = new WebRequest(url, HttpMethod.GET)

    val page: HtmlPage = webClient.getPage(requestSetting)
//    println(page.asText())
//    println(page.asXml())
  }
}
