import requests
import time
import numpy as np
import io
import pandas as pd
import csv
import time 


while True:
	# Hacemos la llamada a la API y elegimos el separador del csv
	s=requests.get("http://www.mambiente.madrid.es/opendata/horario.csv").content
	c = pd.read_csv(io.StringIO(s.decode('utf-8')), sep=';')


	
	# Guardamos el fichero en formato csv:
	eventTime = time.strftime("%Y%m%d%H%M")
	file_name = "aireMadrid_"+eventTime+'.csv'
	c.to_csv('/home/abalserio/tfm/rawData/aireMadrid/'+file_name, sep=',',encoding='utf-8', index=False)

	# Se ejecuta el while cada hora
	time.sleep(3600)


