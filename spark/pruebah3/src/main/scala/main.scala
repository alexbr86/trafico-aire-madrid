package main.scala

import com.uber.h3core.H3Core

object main {

  def main(args: Array[String]): Unit = {
    val h3 = H3Core.newInstance

    val lat = 37.775938728915946
    val lng = -122.41795063018799
    val res = 9
    val hexAddr = h3.geoToH3Address(lat, lng, res)
    println(hexAddr)
  }

}
