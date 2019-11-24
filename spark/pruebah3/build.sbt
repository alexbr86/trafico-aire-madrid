name := "madrid_trafic_air_meteo"
organization := "abalseiro"
version := "1.0.0"

scalaVersion := "2.11.10"

val sparkVersion = "2.4.0"
/*
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % sparkVersion % "provided",
  "org.apache.spark" %% "spark-sql" % sparkVersion % "provided",
  "org.apache.spark" %% "spark-streaming" % sparkVersion % "provided",
  "org.apache.spark" %% "spark-hive" % sparkVersion % "provided"
)
*/
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % sparkVersion,
  "org.apache.spark" %% "spark-sql" % sparkVersion,
  "org.apache.spark" %% "spark-streaming" % sparkVersion,
  "org.apache.spark" %% "spark-hive" % sparkVersion
)
// https://mvnrepository.com/artifact/com.uber/h3
libraryDependencies += "com.uber" % "h3" % "3.0.4"
