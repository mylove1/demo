import scala.io.Source.fromURL
/**
  * Created by cooper on 2016/8/10.
  */
object FileIO {
  def OpenHtml(url: String): String = {
    fromURL(url).mkString
  }

  def main(args: Array[String]): Unit = {
    println("start")

    println(OpenHtml("http://httpbin.org/headers"))

    println("stop")

  }
}
