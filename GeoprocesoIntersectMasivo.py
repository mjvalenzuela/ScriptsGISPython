# Automatizar la interseccion de dos capas

import arcpy

arcpy.env.overwriteOutput = True
path = 'C:/AJohanna/Cursos/ArcGIS/MasterGIS/Automatizacion_Geoprocesos/Practica1.mxd'
mxd = arcpy.mapping.MapDocument(path)
df = arcpy.mapping.ListDataFrames(mxd,'Layers')[0] # primer elemento de la lista de DF
ly_eco = arcpy.mapping.ListLayers(mxd,'Ecorregiones',df)[0] # primer elemento con ese nombre de la lista de layers
ly_cp = arcpy.mapping.ListLayers(mxd,'Centro_Poblados',df)[0] # primer elemento con ese nombre de la lista de layers

# Crear Lista de ecorregiones

lista_eco = []
cursor = arcpy.da.SearchCursor(ly_eco,["Cod_ecorre"]) # Definir cursor en el layer Ecorregiones y en la columna Cod_ecorre
for row in cursor:
    lista_eco.append(row[0]) # Se va agregando en el array lista_eco cada uno de los registros del layer Ecorregiones el contenido de la columna Cod_ecorre
print lista_eco

# Geoprocesar los dos layer para aplicar la interseccion
i=1
for eco in lista_eco:
    # Definir el nombre del archivo de salida para cada interseccion creada
    name_eco = 'Eco_' + str(i)
    print name_eco

    # Definir el query para cada Ecorregion a intersectar
    queryStr = '"Cod_ecorre"' + '=' + "'" + eco + "'"
    ly_eco.definitionQuery = queryStr
    arcpy.RefreshActiveView()
    print 'Query...listo!'

    # Aplicar la interseccion entre la Ecorregion generada del query anterior con el layer de Centros Poblados
    in_features = [ly_cp, ly_eco]
    dir_shape = 'C:/AJohanna/Cursos/ArcGIS/MasterGIS/Automatizacion_Geoprocesos/resultados_shp'
    out_feature = dir_shape + '//' + name_eco + '.shp'

    arcpy.Intersect_analysis(in_features, out_feature)
    i = i+1
    print 'Interseccion...listo!'

