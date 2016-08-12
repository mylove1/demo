import scala.collection.mutable.ArrayBuffer

/**
  * Created by cooper on 2016/8/9.
  */
object HelloWorld {
  lazy val worlds = scala.io.Source.fromFile("C:\\Users\\cooper\\Desktop\\nihao.txt").mkString

  def signum(args: Int) = {
    if (args < 0) -1 else (if (args > 0) 1 else 0)
  }

  def signum2(args: Int) = {
    if (args < 0) -1
    else if (args == 0) 0
    else 1
  }

  def cake (pers: Float) = {
    if (pers == 0){
      throw new IllegalArgumentException("Persons number count eq 0!!!")
    }
    1/pers
  }

  def printnum(args: Int*) {
    for (arg <- args) println (arg)
  }

  def decorate(str: String, left:String = "[", right: String = "]") = left + str + right

  def fac(n: Int) = {
    var r = 1
    for (i <- 1 to n) r = r * i
    r
  }

  def main(args:Array[String]): Unit =
  {
    println(signum2(3))
    println(signum2(-3))
    println(signum2(0))
    val b = ArrayBuffer[Int]()
    b += 3
    b += 4
    b += 5
    b.trimEnd(2)
    println(b)


  }
}
