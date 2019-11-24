import http.client
import json
import pandas as pd
import requests
import time 

# Estaciones de Madrid y sus codigos: 3129 MADRID-BARAJAS, 3194U MADRID-CIUDAD UNIVERSITARIA, 3195 MADRID-RETIRO
estaciones = ['3129', '3194U', '3195']
dflist = []

while True:
	for i in estaciones:
	  conn = http.client.HTTPSConnection("opendata.aemet.es")

	  headers = {
	      'cache-control': "no-cache"
	      }

	  conn.request("GET", "/opendata/api/observacion/convencional/datos/estacion/%s?api_key=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhYmFsc2Vpcm8wMDFAZ21haWwuY29tIiwianRpIjoiNzliMGRiOTgtMWYwYS00YTIwLWEzMTktNDcyNjhkODI3MWJkIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE1NjIwOTU0MTIsInVzZXJJZCI6Ijc5YjBkYjk4LTFmMGEtNGEyMC1hMzE5LTQ3MjY4ZDgyNzFiZCIsInJvbGUiOiIifQ.1JTo_lVE-MU5KZR2LSjbQqML2qzWtXKRUEdj68jjQrg" % i, headers=headers)

	  res_obv = conn.getresponse()
	  data_obv = res_obv.read()
	  wjdata_obv = json.loads(data_obv)
	  url_obv = wjdata_obv['datos']
	  df_aemet_obv = pd.read_json(url_obv)
	  dflist.append(df_aemet_obv)
	  
	

	# Guardamos el fichero:
	aemet_obv_final = pd.concat(dflist, sort=False)
	eventTime = time.strftime("%Y%m%d%H%M")
	file_name = "aemetobv"+"_"+eventTime+'.csv'
	#aemet_obv_final.to_csv('/home/abalserio/tfm/rawData/aemet/observacion/'+file_name, sep=',',encoding='utf-8', index=False)
	aemet_obv_final.to_csv('/home/alex/Master/TFM/trafico-aire-madrid/raw/'+file_name, sep=',',encoding='utf-8', index=False)
	# Se ejecuta el while cada hora
	dflist = []
	time.sleep(3600)


