from tkinter import *
ventana = Tk()
ancho = 650
alto = 400
ventana.geometry(str(ancho)+'x'+str(alto))
ventana.title("Examen Final ISC-B-Lily")


#etiqueta de bienvenida
bienvenido =Label(ventana, text ="BIENVENIDO",font = ("Exotc350 Bd BT",25)).place(x=250,y=10)

#los entry son los botones 
nombre= Label(ventana, text ="Nombre",font = ("Exotc350 Bd BT",15)).place(x=150,y=60)
apellido= Label(ventana, text ="Apellido",font = ("Exotc350 Bd BT",15)).place(x=150,y=90)
dia= Label(ventana, text ="Día",font = ("Exotc350 Bd BT",15)).place(x=150,y=120)
mes= Label(ventana, text ="Mes",font = ("Exotc350 Bd BT",15)).place(x=150,y=150)
Año= Label(ventana, text ="Año",font = ("Exotc350 Bd BT",15)).place(x=150,y=180)

cajanombre= Entry(ventana).place(x=300,y=60)
cajaapellido= Entry(ventana).place(x=300,y=90)
dia=StringVar()
cajadia= Entry(ventana, textvariable=dia).place(x=300,y=120)
mes= StringVar()
cajames=Entry(ventana, textvariable= mes).place(x=300,y=150)
Año=StringVar()
cajaaño= Entry(ventana, textvariable = Año).place(x=300,y=180)

#botones
funcion1= Button (ventana, text = "Funcion1", padx= 15, pady= 10,font=("Exotc350 Bd BT",15)).place(x=50,y=230)
funcion2= Button (ventana, text = "Funcion2", padx= 15, pady= 10,font=("Exotc350 Bd BT",15)).place(x=170,y=230)
funcion3= Button (ventana, text = "Funcion3", padx= 15, pady= 10,font=("Exotc350 Bd BT",15)).place(x=280,y=230)
funcion4= Button (ventana, text = "Funcion4", padx= 15, pady= 10,font=("Exotc350 Bd BT",15)).place(x=395,y=230)
Funcion5= Button (ventana, text = "Funcion5", padx= 15, pady= 10,font=("Exotc350 Bd BT",15)).place(x=500,y=230)
resultado= Label(ventana).place(x=300,y=300)

ventana.mainloop()