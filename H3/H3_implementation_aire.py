import pandas as pd
from h3 import h3
import json
import requests, os
from requests import Session
from requests.auth import HTTPBasicAuth
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index
from datetime import datetime, timedelta
from elasticsearch.exceptions import ConflictError
from pyhive import hive

# definición de funciones

# función para aplicar la cuadrícula de H3 a cada punto en base a su localización
def counts_by_hexagon(df, resolution):
    
    df["hex_id"] = df.apply(lambda row: h3.geo_to_h3(row["LATITUD"], row["LONGITUD"], resolution), axis = 1)
    
    df["GEOM"] =  df.hex_id.apply(lambda x: {"type" : "polygon",
                                             "coordinates": [h3.h3_to_geo_boundary(h3_address=x,geo_json=True)]})
    
    return df  




# función para pivotar las columnas a filas para obtener fila por medición de cada contaminante. Además se incluyen algunas adaptaciones para Elastic.
def pivot_aireMadrid (df):
    columnas = ['PROVINCIA', 'MUNICIPIO', 'ESTACION', 'MAGNITUD', 'PUNTO_MUESTREO', 'NOMBRE_ESTACION', 'DIRECCION',
       'LONGITUD', 'LATITUD', 'MAGNITUD_NOMBRE', 'FECHA']
    df_index = df.set_index(columnas)
    df_pivot = df_index.stack().reset_index()
    df_final = df_pivot.rename(columns={"level_11" : "HORA", 0: "VALOR"})
    df_final["HORA"] = df_final["HORA"].str[1:]
    df_final['FECHA'] = df_final.apply(lambda row: row.FECHA+"T"+row.HORA, axis = 1)
    
    return df_final


# Convertir el dataframe en un json para Elastic
def df_to_json(df):
    df_as_json = df.to_json(orient='records')
    json_df = json.loads(df_as_json)
    
    return json_df


# Llamada al Hive del cluster para obtener los datos del dia anterior
host_name = "35.242.251.186"
port = 10000
user = "abalserio"
password = "bx4Nmqon8E4NyUKsQu3UC7Sa"
database="abalseiro_trafico_aire_Madrid"
ayer = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
query = "SELECT * FROM abalseiro_trafico_aire_Madrid.aireMadrid WHERE airemadrid.fecha = '%s'" % ayer
conn = hive.Connection(host=host_name, port=port, username=user, password=password, auth="LDAP", database=database)
aireMadrid = pd.read_sql(query, conn)
aireMadrid.columns = ['PROVINCIA', 'MUNICIPIO', 'ESTACION', 'MAGNITUD', 'PUNTO_MUESTREO', 'H01', 'H02', 'H03', 'H04', 'H05', 'H06', 'H07', 'H08',
 'H09', 'H10', 'H11', 'H12', 'H13', 'H14', 'H015', 'H16', 'H17', 'H18', 'H19', 'H20', 'H21', 'H22', 'H23', 'H24',
 'NOMBRE_ESTACION', 'DIRECCION','LONGITUD', 'LATITUD', 'MAGNITUD_NOMBRE', 'FECHA']


# aplicar funcion de pivotar
aireMadrid_final = pivot_aireMadrid(aireMadrid)

# aplicar la cuadrícula de H3
aireMadrid_h3 = counts_by_hexagon(aireMadrid_final, 9)

# Generar un punto de ubicación geográfica para Elastic
aireMadrid_h3['LOCALIZACION'] = aireMadrid_h3.apply(lambda row: [row.LONGITUD, row.LATITUD], axis = 1 )

# Convertir el dataframe en json
aireMadrid_json = df_to_json(aireMadrid_h3)

# ingestarlo en Elastic
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])
for i in aireMadrid_json:
    es.index(index="airemadrid", ignore=400, body=i) 

