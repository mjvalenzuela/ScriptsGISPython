# Alistamiento de elementos para exportar

mxd = arcpy.mapping.MapDocument("current")
df = arcpy.mapping.ListDataFrames(mxd,"Layers")[0]
lyr = arcpy.mapping.ListLayers(mxd,"PNC",df)[0]
titulo = arcpy.mapping.ListLayoutElements(mxd,"TEXT_ELEMENT","titulo")[0]
leyenda = arcpy.mapping.ListLayoutElements(mxd,"LEGEND_ELEMENT","Legend")[0]
capas = ["Ecorregiones","Geologia","Uso de tierra","Zonas de vida"]

# Exportacion del mapa en formato JPG

for capa in capas:
    filename = "C:/AJohanna/Cursos/ArcGIS/MasterGIS/Exportar Mapas Python/Resultados/mapas/" + capa + ".jpg"
    lyr_capa = arcpy.mapping.ListLayers(mxd,capa,df)[0]
    lyr_capa.visible = True
    titulo.text = "PARQUE NACIONAL DE CUTERVO" + "\n" + "Mapa de " + capa
    titulo.elementPositionX = 5
    titulo.elementPositionY = 25
    if leyenda.elementHeight > 6:
        leyenda.elementHeight = 6
    else: pass
    arcpy.RefreshActiveView()
    arcpy.mapping.ExportToJPEG(mxd,filename,"page_layout")
    lyr_capa.visible = False
    print "Mapa listo de " + capa
    

