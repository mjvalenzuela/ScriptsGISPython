# Automatizar el cortado de capas
# Automating layer cutting

import arcpy

# Declarar las variables de las capas shp de entrada, recorte y salida
carpeta_entrada = r"C:\xxxx\xxxxx\SHP_Cortar" # Definir ruta local donde se encuentra los shp a cortar
shp_recorte = r"C:\xxxx\xxxxx\localidades_bogota.shp" # Definir ruta local donde se encuentra el shp cortador
carpeta_salida = r"C:\xxxx\xxxxx\SHP Resultados" # Definir ruta local donde se dejaran los shp cortados

arcpy.env.workspace = carpeta_entrada

listar_shp = arcpy.ListFeatureClasses()

for a in listar_shp:
    shp_entrada = carpeta_entrada + "//"+ a
    shp_salida = carpeta_salida + "//"+ a
    print("Procesando", a)
    arcpy.Clip_analysis(shp_entrada, shp_recorte, shp_salida)