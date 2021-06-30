# Mapas de idoneidad de habitat

# importar lo modulos
import arcpy
from arcpy import env
from arcpy.sa import *

arcpy.env.overwriteOutput = True # Sobreescribir archivos de salida si los hay
arcpy.CheckOutExtension("Spatial") # Verificar licencia de Spatial

import sys
import csv

env.workspace = "data" # Establecer espacio de trabajo

def crear_habitat_especies(nombre_especie,codigo_habitat): # Funcion para la creacion de los mapas de idoneidad
    output_shp = 'results\\' + nombre_especie + '.shp'
    output_ras = 'results\\' + nombre_especie + '.tif'
    
    arcpy.MakeFeatureLayer_management('data\\cobertura.shp',"coberlyr") # Crear capa layer a partir del shp
    arcpy.SelectLayerByAttribute_management("coberlyr","NEW_SELECTION",'"ID_clase" in ('+ codigo_habitat +')') # Seleccionar los poligonos que contiene el habitat idoneo
    arcpy.Dissolve_management("coberlyr","temp\\dissolve.shp","","","SINGLE_PART","DISSOLVE_LINES") # Juntar los poligonos con area idonea geograficamente juntos
    arcpy.Buffer_analysis("temp\\dissolve.shp","temp\\buffer.shp","1.5 Meters","FULL","ROUND","ALL","") # Crear un buffer de 1.5 mtrs para definir los 3 mtrs continuos entre si
    arcpy.MultipartToSinglepart_management("temp\\buffer.shp","temp\\multi_to_single.shp") # Separar en varios poligonos que tienen menos de 3 mtrs entre si
    arcpy.AddField_management("temp\\multi_to_single.shp","buffer_ID","LONG","","","","","NON_NULLABLE","NON_REQUIRED","") # Agregar el campo buffer_id
    arcpy.CalculateField_management("temp\\multi_to_single.shp","buffer_ID","[FID]","VB","") # Calcular el nuevo campo para los poligonos
    arcpy.SpatialJoin_analysis("temp\\dissolve.shp","temp\\multi_to_single.shp","temp\\add_buffer_id.shp","JOIN_ONE_TO_ONE","KEEP_ALL") # Unir la informacion de los poligonos disueltos con la informacion de los poligonos separados
    arcpy.Dissolve_management("temp\\add_buffer_id.shp",output_shp,"buffer_ID","","MULTI_PART","DISSOLVE_LINES") # Juntar los poligonos que esten a menos de 3 mtrs entre si
    arcpy.PolygonToRaster_conversion(output_shp,"buffer_ID","temp\\ras.tif","MAXIMUM_AREA") # Convertir a Raster

    out_con = arcpy.sa.Con(IsNull(arcpy.Raster("temp\\ras.tif")),0,1) # Asignar valores 1 = habitat y 0 = no habitat
    out_con.save(output_ras)
    
    print("Mapa de idoneidad del hábitat creado para " + nombre_especie)
    
env.workspace = "data"

csvfile = open("data\\habitat_especies.csv") # Abrir el csv e iterar cada fila de las especies
reader = csv.reader(csvfile)
for row in reader:
    species = row[0]
    habitat = row[1]
    crear_habitat_especies(nombre_especie = species,codigo_habitat = habitat)
    
env.workspace = "results"
rasters = arcpy.ListRasters() # Lista todos los raster que estan en el workspace definido

# Iterar en los rasters y unirlos
i=0
for raster in rasters:
    if i==0: # Para el primer raster necesitamos asignarlo al archivo de salida
        out = Raster(raster)
        i+=1
    else: # Para los demas rasters los juntamos al objeto de salida
        out = out + Raster(raster)
        i+=1
        
print("Mapa de riqueza de especies generado")
out.save("riqueza_especies.tif")

