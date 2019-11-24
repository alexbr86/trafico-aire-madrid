import requests
import pandas as pd
import itertools
from bs4 import BeautifulSoup as b
import time 



# API request: 
url = "http://informo.munimadrid.es/informo/tmadrid/pm.xml"



while True:
	
	response = requests.get(url)

	soup = b(response.content, "lxml")

	idelem =  [ values.text for values in soup.findAll("idelem")]
	fecha =  [ values.text for values in soup.findAll("fecha_hora")]
	descripcion = [ values.text for values in soup.findAll("descripcion")]
	accesoAsociado =  [ values.text for values in soup.findAll("accesoasociado")]
	intensidad =  [ values.text for values in soup.findAll("intensidad")]
	ocupacion =  [ values.text for values in soup.findAll("ocupacion")]
	carga =  [ values.text for values in soup.findAll("carga")]
	nivelServicio =  [ values.text for values in soup.findAll("nivelservicio")]
	intensidadSat =  [ values.text for values in soup.findAll("intensidadsat")]
	error =  [ values.text for values in soup.findAll("error")]
	subarea =  [ values.text for values in soup.findAll("subarea")]
	st_x =  [ values.text for values in soup.findAll("st_x")]
	st_y =  [ values.text for values in soup.findAll("st_y")]


	data = [item for item in itertools.zip_longest(idelem, descripcion, accesoAsociado, intensidad, ocupacion, carga, nivelServicio, intensidadSat, error, subarea, st_x, st_y)] 
	df  = pd.DataFrame(data=data, columns = ["idelem", "descripcion", "accesoAsociado", "intensidad", "ocupacion", "carga", "nivelServicio", "intensidadSat", "error", "subarea", "st_x", "st_y"])
	df['fecha'] = fecha[0]



	
	# Guardamos el fichero:
	eventTime = time.strftime("%Y%m%d%H%M")
	file_name = "trafico_"+eventTime+'.csv'
	df.to_csv('/home/abalserio/tfm/rawData/trafico/'+file_name, sep=',',encoding='utf-8', index=False)
	#df.to_csv('/home/alex/Master/TFM/trafico-aire-madrid/'+file_name, sep=',',encoding='utf-8', index=False)


	# Se ejecuta el while cada hora
	time.sleep(300)


