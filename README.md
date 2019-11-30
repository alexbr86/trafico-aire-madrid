# Análisis y predicción del tráfico y la calidad del aire en Madrid

## [GitHub del proyecto](https://github.com/alexbr86/trafico-aire-madrid)

## Instrucciones

### Contenido de las carpetas:
- **elasticsearch**: contiene la configuración de cada uno de los indices generados.
- **flume**: contiene una carpeta por tipo de dato. Cada una tiene una carpeta conf con la configuración y un execute flume para ejecutarlo.
- **H3**: contiene los procesos python del tráfico y aire que se utilizan para incluir la cuadricula de H3 y enviarlos a Elastic.
- **hive**: contiene un archivo con el código generado para crear la configuración de cada tabla por tipo de dato en Hive.
- **modelado**: contiene un notebook donde se ha realizado el analisis y modelado en formato notebook y .pdf. Ademas tiene un documento de texto explicando las variables del dataset y el dataset en .csv empleado en el notebook.
- **pyScript**: contiene los cuatro procesos de python que se utilizan para la ingesta de cada tipo de dato.
- **spark**: contiene el proyecto completo del procesamiento utilizado. Además dentro en la ruta ./spark/madrid_trafic_air/target/scala-2.11/madrid_trafico_aire-assembly-0.1.jar se encuentra el ejecutable. El comando para ejecutarlo se ubica en ./spark/spark_execute.txt
- **Análisis y predicción de la contaminación del aire en Madrid en base al tráfico y meteorología**: documento de la memoria del proyecto en .pdf.
- **Análisis y predicción de la contaminación del aire en Madrid en base al tráfico y meteorología_presentacion.pptx**: presentación ejecutiva del proyecto en powerpoint
- **Análisis y predicción de la contaminación del aire en Madrid en base al tráfico y meteorología_presentacion.pdf**: presentación ejecutiva del proyecto en .pdf
- **videos**: contiene cuatro vídeos mostrando el funcionamiento de los diferentes procesos. Ingesta-procesamiento, aplicación de la cuadrícula H3 en terminal, aplicación de la cuadrícula H3 en notebook y visualización.

### Pasos a seguir para ejecutar.
1. Acceder al cluster en el perfil abalserio en /home/abalserio/.
2. Acceder a la ruta /home/abalserio/tfm/source/flume. Ahi se encontrarán 4 carpetas. Acceder a cada una y ejecutar el comando ./executeFlume.sh para activar cada uno de los flumes de las tipologías de datos.
3. Acceder a la ruta /home/abaserio/source/pyScript/ y ejecutar cada uno de los archivos python con python3 nombre_archivo.py.
4. Una vez ejecutados los scripts acceder a la ruta /home/abalserio/tfm/source/spark/ y ejecutar el comando de Spark que se encuentra en el documento de esta carpeta /spark/spark_execute.txt
5. En local levantar Elasticsearch y Kibana. (Teniendo en cuenta que ya está configurado los indices que hay en la carpeta ./elasticsearch/)
6. Ejecutar en local los dos procesos de python ubicados en esta carpeta en ./H3/ . Con el comando python nombre_proceso.py
7. Acceder a Kibana, en la zona de mapa y acceder a la visualización. Si no esta configurada añadir los indices y generar las visualizaciones.
=======
>>>>>>> 63dfd3630130e42e93b2c6c09f0d890f8b0bd943
