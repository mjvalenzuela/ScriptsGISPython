# Calculo del area de una circunferencia con interfaz grafica
# Calculation of the area of a circumference with graphical interface

import math
import tkinter # Libreria para crear ventanas ejecutables

def radio():
    radio = float(caja_input.get())
    resultado = round(((radio**2)*math.pi),4)
    return var.set(resultado)

# Creacion y configuracion de la ventana
ventana = tkinter.Tk()
ventana.title("Area Circunferencia")
ventana.geometry("400x150")

# Variable para mostrar en la pantalla el resultado
var = tkinter.DoubleVar()

# Creación del texto para la descripcion
text_description = tkinter.Label(ventana, text="Ventana para el cálculo del area de una circunferencia", bg='blue', fg='white')
text_description.pack()

# Creación del texto para obtener del usuario el Radio
text_input = tkinter.Label(ventana, text="Ingrese el Radio de la circunferencia: ")
text_input.pack()

# Creación de la caja de texto para obtener del usuario el Radio
caja_input = tkinter.Entry(ventana)
caja_input.pack()

# Creación del botón para iniciar el cálculo
btn_calculate = tkinter.Button(ventana, text="Calcular área", command=radio)
btn_calculate.pack()

# Creación del texto que mostrará el resultado
caja_result = tkinter.Label(ventana, textvariable=var)
caja_result.pack()

# Llamado de la función
ventana.mainloop()