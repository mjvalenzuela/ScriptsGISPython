# Creacion de campo y calculo de sus valores
# Field creation and calculation of their values

from PyQt5.QtCore import QVariant #para definir tipo de campo
from qgis.core import  *

shp = r"C:\xxxx\xxxxx\Water.shp" # Colocar la ruta local donde se encuentre el shp
layer = QgsVectorLayer(shp,'water','ogr')

campos = layer.dataProvider()
campos.addAttributes([QgsField('AreaHa',QVariant.Double)])

print("Campos creados correctamente!!")

expression = QgsExpression('$area/10000')
context = QgsExpressionContext()
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(layer))

with edit(layer):
    for i in layer.getFeatures():
        context.setFeature(i)
        i['AreaHa'] = expression.evaluate(context)
        layer.updateFeature(i)

print("Area calculada correctamente!!")

total_area = 0

for water in layer.getFeatures():
    area = water['AreaHa']
    total_area += area

print("El area total de los cuerpos de agua es: ", str(total_area), " hectareas")