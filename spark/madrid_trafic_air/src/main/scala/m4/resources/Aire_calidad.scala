package m4.resources

import org.apache.log4j.{Level, Logger}
import org.apache.spark.sql._
import java.util

import org.apache.spark.sql.functions._
import com.mongodb.spark._
import org.apache.derby.iapi
import org.apache.hadoop.fs._
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.api.java.UDF2
import org.apache.spark.sql.types.DataTypes
import org.apache.spark.sql.types.StructField
import org.apache.spark.sql.functions.udf

import scala.collection.JavaConverters._
import scala.collection.immutable._
import scala.collection.mutable
import scala.util.parsing.json._
import org.apache.spark.sql.expressions.UserDefinedFunction



object Aire_calidad {

  def main(args: Array[String]): Unit = {

    val logger = Logger.getLogger("org.apache.spark")
    logger.setLevel(Level.ERROR)

    // Se inicializan las configuraciones necesarias junto con la conexión con la base de datos y colección de MongoDB
    val spark = SparkSession
      .builder()
      .appName("Processing_trafic_air_meteo")
      //.master("local[*]")
      //.enableHiveSupport()
      .getOrCreate()

    val fs = FileSystem.get(spark.sparkContext.hadoopConfiguration)


    val meteo_obv_raw = spark.read.option("header", "true").csv("/user/abalserio/tfm/datosSpark/aemet/observacion/")
    val meteo_pred_raw = spark.read.option("header", "true").csv("/user/abalserio/tfm/datosSpark/aemet/prediccion/")
    val trafico_raw = spark.read.option("header", "true").csv("/user/abalserio/tfm/datosSpark/trafico/")
    val aireMadrid_raw = spark.read.option("header", "true").csv("/user/abalserio/tfm/datosSpark/aireMadrid/")
    val aireMadrid_stations = spark.read.option("header", "true").csv("/user/abalserio/tfm/infodata/informacion_estaciones_red_calidad_aire.csv")
    val aireMadrid_magnitud = spark.read.option("header", "true").csv("/user/abalserio/tfm/infodata/codigo_magnitud.csv")
    val trafico_stations = spark.read.option("header", "true").csv("/user/abalserio/tfm/infodata/ubicacion_medidores_trafico.csv")



    // limpiar y unir los datos de calidad de aire con la ubicación de los centros de medición
    val aireMadrid_1 = aireMadrid_raw
      .withColumn("H01", when(col("V01") === "N", 0).otherwise(col("H01")) ).drop("V01")
      .withColumn("H02", when(col("V02") === "N", 0).otherwise(col("H02")) ).drop("V02")
      .withColumn("H03", when(col("V03") === "N", 0).otherwise(col("H03")) ).drop("V03")
      .withColumn("H04", when(col("V04") === "N", 0).otherwise(col("H04")) ).drop("V04")
      .withColumn("H05", when(col("V05") === "N", 0).otherwise(col("H05")) ).drop("V05")
      .withColumn("H06", when(col("V06") === "N", 0).otherwise(col("H06")) ).drop("V06")
      .withColumn("H07", when(col("V07") === "N", 0).otherwise(col("H07")) ).drop("V07")
      .withColumn("H08", when(col("V08") === "N", 0).otherwise(col("H08")) ).drop("V08")
      .withColumn("H09", when(col("V09") === "N", 0).otherwise(col("H09")) ).drop("V09")
      .withColumn("H10", when(col("V10") === "N", 0).otherwise(col("H10")) ).drop("V10")
      .withColumn("H11", when(col("V11") === "N", 0).otherwise(col("H11")) ).drop("V11")
      .withColumn("H12", when(col("V12") === "N", 0).otherwise(col("H12")) ).drop("V12")
      .withColumn("H13", when(col("V13") === "N", 0).otherwise(col("H13")) ).drop("V13")
      .withColumn("H14", when(col("V14") === "N", 0).otherwise(col("H14")) ).drop("V14")
      .withColumn("H15", when(col("V15") === "N", 0).otherwise(col("H15")) ).drop("V15")
      .withColumn("H16", when(col("V16") === "N", 0).otherwise(col("H16")) ).drop("V16")
      .withColumn("H17", when(col("V17") === "N", 0).otherwise(col("H17")) ).drop("V17")
      .withColumn("H18", when(col("V18") === "N", 0).otherwise(col("H18")) ).drop("V18")
      .withColumn("H19", when(col("V19") === "N", 0).otherwise(col("H19")) ).drop("V19")
      .withColumn("H20", when(col("V20") === "N", 0).otherwise(col("H20")) ).drop("V20")
      .withColumn("H21", when(col("V21") === "N", 0).otherwise(col("H21")) ).drop("V21")
      .withColumn("H22", when(col("V22") === "N", 0).otherwise(col("H22")) ).drop("V22")
      .withColumn("H23", when(col("V23") === "N", 0).otherwise(col("H23")) ).drop("V23")
      .withColumn("H24", when(col("V24") === "N", 0).otherwise(col("H24")) ).drop("V24")

    val aireMadrid_2 = aireMadrid_1.join(aireMadrid_stations, col("ESTACION")===col("CODIGO_CORTO")).drop("CODIGO_CORTO").join(aireMadrid_magnitud, col("MAGNITUD")===col("MAGNITUD_CODIGO")).drop("MAGNITUD_CODIGO")
    val aireMadrid_final = aireMadrid_2.withColumn("FECHA", to_date(concat(col("ANO"), col("MES"), col("DIA")), "yyyyMMdd")).drop("ANO", "MES", "DIA")



    // Limpiar y ordenar los datos de predicción de tiempo
    val fecha: String = meteo_pred_raw.first().getAs("fecha")
    val ocaso: String = meteo_pred_raw.first().getAs("ocaso")
    val orto: String = meteo_pred_raw.first().getAs("orto")

    val meteo_pred_1 = meteo_pred_raw.withColumnRenamed("estadoCielo_periodo", "periodo").drop("humedadRelativa_periodo", "nieve_periodo", "precipitacion_periodo", "probNieve_periodo", "sensTermica_periodo", "temperatura_periodo", "viento_periodo", "rachaMax_periodo", "fecha", "ocaso", "orto")
    val meteo_pred_final = meteo_pred_1.withColumn("fecha", lit(fecha)).withColumn("ocaso", lit(ocaso)).withColumn("orto", lit(orto))



    // Limpiar de errores los datos de trafico
    val trafico_1 = trafico_raw.where(col("error").isin("N")).drop("error")
    val trafico_2 = trafico_1.join(trafico_stations, col("idelem")===col("id")).drop("id", "st_x", "st_y")
    val trafico_final = trafico_2.withColumn("fecha_1", from_unixtime(unix_timestamp(col("fecha"), "dd/MM/yyyy HH:mm:ss"), "yyyy-MM-dd HH:mm:ss")).drop("fecha").withColumnRenamed("fecha_1", "fecha")














    //Escribir en las carpetas de las tablas donde lee Hive cada dataset
    val dateFormat = "yyyyMMdd"
    val ts = current_timestamp().expr.eval().toString.toLong
    val dateValue = new java.sql.Timestamp(ts/1000).toLocalDateTime.format(java.time.format.DateTimeFormatter.ofPattern(dateFormat))

    trafico_final.write.format("csv").mode("overwrite").save("/user/abalserio/tfm/hive/trafico/trafico_"+dateValue)
    aireMadrid_final.write.format("csv").mode("overwrite").save("/user/abalserio/tfm/hive/aireMadrid/aireMadrid_"+dateValue)

    meteo_pred_final.write.format("csv").mode("overwrite").save("/user/abalserio/tfm/hive/aemet_prediccion/meteo_pred"+dateValue)
    meteo_obv_raw.write.format("csv").mode("overwrite").save("/user/abalserio/tfm/hive/aemet_observacion/meteo_obv"+dateValue)







    // Se borra la carpeta donde se ha dejado una copia del csv una vez procesado
    fs.delete(new Path("/user/abalserio/tfm/datosSpark/"), true)




  }
}
