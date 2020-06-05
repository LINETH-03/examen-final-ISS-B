from tkinter import *
from datetime import date
from datetime import datetime
ventana = Tk()
ancho = 400
alto = 300
ventana.geometry(str(ancho)+'x'+str(alto))
ventana.title('Examen Final ISC-LILY')


etibienvenido= Label(text="Bienvenido",font=("Exotc350 Bd BT",35))
etibienvenido.grid(row=1, column=2, columnspan=6)
#_____________________________________________________________________________
##CAJA DE TEXTO PARA EL NOMBRE Y ETIQUETA
etiNombre = Label(text="Nombre:",font=("Exotc350 Bd BT", 14))
etiNombre.grid(row=2, column=1, columnspan=2)

cajanombre = Entry(ventana)
cajanombre.grid(row=2, column=3, columnspan=4, sticky= W + E)
#_____________________________________________________________________________
##CAJA DE TEXTO PARA EL APELLIDO Y ETIQUETA
etiApellido = Label(text="Apellido:",font=("Exotc350 Bd BT", 14))
etiApellido.grid(row=3, column=1, columnspan=2)

cajaapellido = Entry(ventana)
cajaapellido.grid(row=3, column=3, columnspan=4, sticky= W + E)
#_____________________________________________________________________________
##CAJA DE TEXTO PARA EL DIA Y ETIQUETA
etiDia = Label(text="Día:",font=("Exotc350 Bd BT", 14))
etiDia.grid(row=4, column=1, columnspan=2)

cajadia = Entry(ventana)
cajadia.grid(row=4, column=3, columnspan=4, sticky= W + E)
#_____________________________________________________________________________
#CAJA DE TEXTO PARA EL MES Y ETIQUETA
etiMes = Label(text="Mes:",font=("Exotc350 Bd BT", 14))
etiMes.grid(row=5, column=1, columnspan=2)

cajames = Entry(ventana)
cajames.grid(row=5, column=3, columnspan=4, sticky= W + E)
#___________________________________________________________________________
#CAJA DE TEXTO PARA EL AÑO Y ETIQUETA
etiAño = Label(text="Año:",font=("Exotc350 Bd BT", 14))
etiAño.grid(row=6, column=1, columnspan=2)

cajaaño = Entry(ventana)
cajaaño.grid(row=6, column=3, columnspan=4, sticky= W + E)
#_____________________________________________________________________________
#FUNCION 2 PARA MOSTRAR AL REVES EL TEXTO
def Diasvividos():
    fechaString = f"{cajaaño.get()}-{cajames.get()}-{cajadia.get()}"
    dato = datetime.strptime(fechaString, '%Y-%m-%d')

    today= datetime.today()
    
    dat1 = today
    dat2 = dato
    answer = abs(dat1-dat2).days 

    respuesta = f"Usted nacio el {dato} y ha vivido {answer} días."

    Resultado.configure(text = respuesta)


#FUNCION 5 PARA MOSTRAR AL REVES EL TEXTO
def ALREVES():
    reva = cajanombre.get()+" "+cajaapellido.get()
    reva = reva[::-1]
    Resultado["text"] = cajanombre.get() + " " + cajaapellido.get() + " al revés es: " + reva




#BOTONES
#_________________________________________________________________________________________
funcion1 = Button(ventana, text = "Función 1",font=("Exotc350 Bd BT", 8), width=10)
funcion1.grid(row=7, column=1)
funcion2 = Button(ventana, text = "Función 2", command=Diasvividos ,font=("Exotc350 Bd BT", 8), width=10)
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