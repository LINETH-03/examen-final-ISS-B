from tkinter import *

ventana = Tk()

ancho = 400
alto = 300

ventana.geometry(str(ancho)+'x'+str(alto))
ventana.title('Examen Final ISC-LILY')


etibienvenido= Label(text="Bienvenido",font=("Exotc350 Bd BT",35))
etibienvenido.grid(row=1, column=2, columnspan=6)

etiNombre = Label(text="Nombre:",font=("Exotc350 Bd BT", 14))
etiNombre.grid(row=2, column=1, columnspan=2)
##CAJA DE TEXTO PARA EL NOMBRE
cajanombre = Entry(ventana)
cajanombre.grid(row=2, column=3, columnspan=4, sticky= W + E)

etiApellido = Label(text="Apellido:",font=("Exotc350 Bd BT", 14))
etiApellido.grid(row=3, column=1, columnspan=2)
##CAJA DE TEXTO PARA EL APELLIDO
cajaapellido = Entry(ventana)
cajaapellido.grid(row=3, column=3, columnspan=4, sticky= W + E)

etiDia = Label(text="Día:",font=("Exotc350 Bd BT", 14))
etiDia.grid(row=4, column=1, columnspan=2)
##CAJA DE TEXTO PARA EL DIA
cajadia = Entry(ventana)
cajadia.grid(row=4, column=3, columnspan=4, sticky= W + E)

etiMes = Label(text="Mes:",font=("Exotc350 Bd BT", 14))
etiMes.grid(row=5, column=1, columnspan=2)
#CAJA DE TEXTO PARA EL MES
cajames = Entry(ventana)
cajames.grid(row=5, column=3, columnspan=4, sticky= W + E)

etiAño = Label(text="Año:",font=("Exotc350 Bd BT", 14))
etiAño.grid(row=6, column=1, columnspan=2)
#CAJA DE TEXTO PARA EL AÑO
cajaaño = Entry(ventana)
cajaaño.grid(row=6, column=3, columnspan=4, sticky= W + E)
#_____________________________________________________________________________

#FUNCION PARA MOSTRAR AL REVES EL TEXTO
def ALREVES():
    reva = cajanombre.get()+" "+cajaapellido.get()
    reva = reva[::-1]
    Resultado["text"] = cajanombre.get() + " " + cajaapellido.get() + " al revés es: " + reva


#BOTONES
#_________________________________________________________________________________________
funcion1 = Button(ventana, text = "Función 1",font=("Exotc350 Bd BT", 8), width=10)
funcion1.grid(row=7, column=1)
funcion2 = Button(ventana, text = "Función 2",font=("Exotc350 Bd BT", 8), width=10)
funcion2.grid(row=7, column=2)
funcion3 = Button(ventana, text = "Función 3",font=("Exotc350 Bd BT", 8), width=10)
funcion3.grid(row=7, column=3)
funcion4 = Button(ventana, text = "Función 4", font=("Exotc350 Bd BT", 8), width=10)
funcion4.grid(row=7, column=4)
funcion5 = Button(ventana, text = "Función 5",command=ALREVES,font=("Exotc350 Bd BT", 8), width=10)
funcion5.grid(row=7, column=5)
#_____________________________________________________________________________________________
#ETIQUETA PARA MOSTRAR RESULTADO
Resultado = Label(ventana,text="RESULTADO",font=("Exotc350 Bd BT", 14))
Resultado.grid(row=8, column=1, columnspan=6)

ventana.mainloop()