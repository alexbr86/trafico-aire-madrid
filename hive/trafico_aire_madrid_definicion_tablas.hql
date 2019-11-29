CREATE DATABASE abalseiro_trafico_aire_Madrid

CREATE EXTERNAL TABLE IF NOT EXISTS abalseiro_trafico_aire_Madrid.aemet_observacion
(idema STRING, lon FLOAT, fint STRING, prec INT, alt INT, vmax FLOAT, vv FLOAT, dv INT, lat FLOAT, dmax INT, ubi STRING, pres FLOAT,
	hr FLOAT, stdvv FLOAT, ts FLOAT, pres_nmar FLOAT, tamin FLOAT, ta FLOAT, tamax FLOAT, tpr FLOAT, vis FLOAT, stddv FLOAT, inso FLOAT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/abalserio/tfm/hive/aemet_observacion/'

CREATE EXTERNAL TABLE IF NOT EXISTS abalseiro_trafico_aire_Madrid.aemet_prediccion
(estadoCielo_value STRING, periodo STRING , estadoCielo_descripcion STRING, humedadRelativa_value INT, nieve_value INT, precipitacion_value INT,
	probNieve_value FLOAT, probPrecipitacion_value FLOAT, probPrecipitacion_periodo STRING  , probTorment_value FLOAT, probTormenta_periodo STRING,
	sensTermica_value INT, temperatura_value INT, viento_direccion STRING, viento_velocidad STRING, rachaMax_value INT, fecha STRING, ocaso STRING, orto STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/abalserio/tfm/hive/aemet_prediccion/'

CREATE EXTERNAL TABLE IF NOT EXISTS abalseiro_trafico_aire_Madrid.aireMadrid
	(PROVINCIA INT, MUNICIPIO INT, ESTACION INT,MAGNITUD INT, PUNTO_MUESTREO STRING, H01 FLOAT, H02 FLOAT, H03 FLOAT, H04 FLOAT, H05 FLOAT, H06 FLOAT, H07 FLOAT, 
	H08 FLOAT, H09 FLOAT, H10 FLOAT, H11 FLOAT, H12 FLOAT, H13 FLOAT, H14 FLOAT, H15 FLOAT, H16 FLOAT, H17 FLOAT, H18 FLOAT, H19 FLOAT, H20 FLOAT, H21 FLOAT,
	H22 FLOAT, H23 FLOAT, H24 FLOAT, NOMBRE_ESTACION STRING, DIRECCION STRING, LONGITUD FLOAT, LATITUD FLOAT, MAGNITUD_NOMBRE STRING, FECHA STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/abalserio/tfm/hive/aireMadrid/'

CREATE EXTERNAL TABLE IF NOT EXISTS abalseiro_trafico_aire_Madrid.trafico
(idelem INT, descripcion STRING, accesoAsociado FLOAT,intensidad INT, ocupacion INT, carga INT, nivelServicio FLOAT, intensidadSat FLOAT, subarea FLOAT, longitud FLOAT, 
	latitud FLOAT, fecha STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/abalserio/tfm/hive/trafico/'


