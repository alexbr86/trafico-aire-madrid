import httplib
import json
import pandas as pd
import requests
from io import StringIO, BytesIO
import ast


while True:
	



	conn = httplib.HTTPSConnection("opendata.aemet.es")

	headers = {
	    'cache-control': "no-cache"
	    }

	conn.request("GET", "/opendata/api/prediccion/especifica/municipio/horaria/28079?api_key=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhYmFsc2Vpcm8wMDFAZ21haWwuY29tIiwianRpIjoiNzliMGRiOTgtMWYwYS00YTIwLWEzMTktNDcyNjhkODI3MWJkIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE1NjIwOTU0MTIsInVzZXJJZCI6Ijc5YjBkYjk4LTFmMGEtNGEyMC1hMzE5LTQ3MjY4ZDgyNzFiZCIsInJvbGUiOiIifQ.1JTo_lVE-MU5KZR2LSjbQqML2qzWtXKRUEdj68jjQrg", headers=headers)

	res_pred = conn.getresponse()
	data_pred = res_pred.read()
	wjdata_pred = json.loads(data_pred)

	url_pred = wjdata_pred['datos']
	raw_data_pred = requests.get(url_pred).text
	jj = ast.literal_eval(raw_data_pred)
	tt = jj[0]
	json_pred = tt.get("prediccion")

	df_pred = pd.DataFrame.from_dict(json_pred.get("dia"))
	df_pred = pd.DataFrame(df_pred.iloc[0, :])
	df_pred = df_pred.transpose()

	df1_pred = pd.DataFrame(df_pred['estadoCielo'].values.tolist()).transpose()
	df1_pred.columns = ['estadoCielo']
	df1_predj = pd.DataFrame()
	for i in range (0, len(df1_pred.index)):
	  df1_predi = pd.DataFrame(df1_pred.iloc[i,].values.tolist())
	  df1_predj = pd.concat([df1_predj,df1_predi], axis=0, ignore_index=True)
	df1_predj.columns=['estadoCielo.descripcion', 'estadoCielo.periodo', 'estadoCielo.value']
	df1_pred = df1_predj

	df2_pred = pd.DataFrame(df_pred['fecha'].values.tolist()).transpose()
	df2_pred.columns = ['fecha']


	df3_pred = pd.DataFrame(df_pred['humedadRelativa'].values.tolist()).transpose()
	df3_pred.columns = ['humedadRelativa']
	df3_predj = pd.DataFrame()
	for i in range (0, len(df3_pred.index)):
	  df3_predi = pd.DataFrame(df3_pred.iloc[i,].values.tolist())
	  df3_predj = pd.concat([df3_predj,df3_predi], axis=0, ignore_index=True)   
	df3_predj.columns=['humedadRelativa.periodo', 'humedadRelativa.value']
	df3_pred = df3_predj

	df4_pred = pd.DataFrame(df_pred['nieve'].values.tolist()).transpose()
	df4_pred.columns = ['nieve']
	df4_predj = pd.DataFrame()
	for i in range (0, len(df4_pred.index)):
	  df4_predi = pd.DataFrame(df4_pred.iloc[i,].values.tolist())
	  df4_predj = pd.concat([df4_predj,df4_predi], axis=0, ignore_index=True)   
	df4_predj.columns=['nieve.periodo', 'nieve.value']
	df4_pred = df4_predj


	df5_pred = pd.DataFrame(df_pred['ocaso'].values.tolist()).transpose()
	df5_pred.columns = ['ocaso']

	df6_pred = pd.DataFrame(df_pred['orto'].values.tolist()).transpose()
	df6_pred.columns = ['orto']

	df7_pred = pd.DataFrame(df_pred['precipitacion'].values.tolist()).transpose()
	df7_pred.columns = ['precipitacion']
	df7_predj = pd.DataFrame()
	for i in range (0, len(df7_pred.index)):
	  df7_predi = pd.DataFrame(df7_pred.iloc[i,].values.tolist())
	  df7_predj = pd.concat([df7_predj,df7_predi], axis=0, ignore_index=True)   
	df7_predj.columns=['precipitacion.periodo', 'precipitacion.value']
	df7_pred = df7_predj

	df8_pred = pd.DataFrame(df_pred['probNieve'].values.tolist()).transpose()
	df8_pred.columns = ['probNieve']
	df8_predj = pd.DataFrame()
	for i in range (0, len(df8_pred.index)):
	  df8_predi = pd.DataFrame(df8_pred.iloc[i,].values.tolist())
	  df8_predj = pd.concat([df8_predj,df8_predi], axis=0, ignore_index=True)   
	df8_predj.columns=['probNieve.periodo', 'probNieve.value']
	df8_pred = df8_predj

	df9_pred = pd.DataFrame(df_pred['probPrecipitacion'].values.tolist()).transpose()
	df9_pred.columns = ['probPrecipitacion']
	df9_predj = pd.DataFrame()
	for i in range (0, len(df9_pred.index)):
	  df9_predi = pd.DataFrame(df9_pred.iloc[i,].values.tolist())
	  df9_predj = pd.concat([df9_predj,df9_predi], axis=0, ignore_index=True)   
	df9_predj.columns=['probPrecipitacion.periodo', 'probPrecipitacion.value']
	df9_pred = df9_predj

	df10_pred = pd.DataFrame(df_pred['probTormenta'].values.tolist()).transpose()
	df10_pred.columns = ['probTormenta']
	df10_predj = pd.DataFrame()
	for i in range (0, len(df10_pred.index)):
	  df10_predi = pd.DataFrame(df10_pred.iloc[i,].values.tolist())
	  df10_predj = pd.concat([df10_predj,df10_predi], axis=0, ignore_index=True)   
	df10_predj.columns=['probTormenta.periodo', 'probTormenta.value']
	df10_pred = df10_predj

	df11_pred = pd.DataFrame(df_pred['sensTermica'].values.tolist()).transpose()
	df11_pred.columns = ['sensTermica']
	df11_predj = pd.DataFrame()
	for i in range (0, len(df11_pred.index)):
	  df11_predi = pd.DataFrame(df11_pred.iloc[i,].values.tolist())
	  df11_predj = pd.concat([df11_predj,df11_predi], axis=0, ignore_index=True)   
	df11_predj.columns=['sensTermica.periodo', 'sensTermica.value']
	df11_pred = df11_predj

	df12_pred = pd.DataFrame(df_pred['temperatura'].values.tolist()).transpose()
	df12_pred.columns = ['temperatura']
	df12_predj = pd.DataFrame()
	for i in range (0, len(df12_pred.index)):
	  df12_predi = pd.DataFrame(df12_pred.iloc[i,].values.tolist())
	  df12_predj = pd.concat([df12_predj,df12_predi], axis=0, ignore_index=True)   
	df12_predj.columns=['temperatura.periodo', 'temperatura.value']
	df12_pred = df12_predj

	df13_pred = pd.DataFrame(df_pred['vientoAndRachaMax'].values.tolist()).transpose()
	df13_pred.columns = ['vientoAndRachaMax']
	dfj = pd.DataFrame()
	dfk = pd.DataFrame()
	for i in range (0, len(df13_pred.index)):
	  dfi = pd.DataFrame(df13_pred.iloc[i,].values.tolist())
	  if i%2 == 0:
	    dfj = pd.concat([dfj,dfi], axis=0, ignore_index=True)
	  else:
	    dfk = pd.concat([dfk,dfi], axis=0, ignore_index=True)
	    
	df13_pred = pd.concat([dfj,dfk], axis=1, ignore_index=True)
	df13_pred.columns=['vientoAndRachaMax.direccion',	'vientoAndRachaMax.periodo',	'vientoAndRachaMax.velocidad', 'vientoAndRachaMax.periodo_delete',	'vientoAndRachaMax.value']
	df13_pred.drop('vientoAndRachaMax.periodo_delete', axis=1)

	
	df_aemet_pred = pd.concat([df1_pred, df2_pred, df3_pred, df4_pred, df5_pred, df6_pred, df7_pred, df8_pred, df9_pred, df10_pred, df11_pred, df12_pred, df13_pred],axis=1)


	# Guardamos el fichero:
	eventTime = time.strftime("%Y%m%d%H%M")
	file_name = "aemetpred_"+eventTime+'.csv'
	df_aemet_pred.to_csv(r'./rawData/aemet/prediccion/'+file_name, sep='\t',encoding='utf-8', index=False)

	# Se ejecuta el while cada hora
	time.sleep(3600)


