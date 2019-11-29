import pandas as pd
from h3 import h3
import json
import requests, os
from requests import Session
from requests.auth import HTTPBasicAuth
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index
import utm
from datetime import datetime, timedelta
from pyhive import hive


# definición de funciones

# función para aplicar la cuadrícula de H3 a cada punto en base a su localización
def counts_by_hexagon(df, resolution):
    
    df["hex_id"] = df.apply(lambda row: h3.geo_to_h3(row["latitud"], row["longitud"], resolution), axis = 1)
  
    df["GEOM"] =  df.hex_id.apply(lambda x: {"type" : "polygon",
                                             "coordinates": [h3.h3_to_geo_boundary(h3_address=x,geo_json=True)]})
    
    return df  


# función para formatear la fecha y localización en apta para Elastic
def elastic_format (df):
    df['localizacion'] = df.apply(lambda row: [row.longitud, row.latitud], axis = 1 )
    df['fecha'] = df.apply(lambda row: row.fecha.replace(" ", "T"), axis = 1)
    
    return df


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
query = "SELECT * FROM abalseiro_trafico_aire_Madrid.trafico WHERE trafico.fecha like '%s'" % ayer
conn = hive.Connection(host=host_name, port=port, username=user, password=password, auth="LDAP", database=database)
trafico = pd.read_sql(query, conn)
trafico.columns = ['idelem', 'descripcion', 'accesoasociado', 'intensidad', 'ocupacion', 'carga',
       'nivelservicio', 'intensidadsat', 'subarea', 'longitud', 'latitud', 'fecha']

# aplicar la función del formato para Elastic
trafico_format = elastic_format(trafico)

# aplicar la cuadrícula de H3
trafico_h3 = counts_by_hexagon(trafico_format, 9)

# Convertir el dataframe en json
trafico_json = df_to_json(trafico_h3)

# ingestarlo en Elastic
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])
for i in trafico_json:
    es.index(index="trafico", ignore=400, body=i) 

