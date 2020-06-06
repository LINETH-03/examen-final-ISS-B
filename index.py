from tkinter import *
from datetime import date
from datetime import datetime
ventana = Tk()
ancho = 475
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
cajanombre.grid(row=2, column=3, columnspan=3, sticky= W + E)
#_____________________________________________________________________________
##CAJA DE TEXTO PARA EL APELLIDO Y ETIQUETA
etiApellido = Label(text="Apellido:",font=("Exotc350 Bd BT", 14))
etiApellido.grid(row=3, column=1, columnspan=2)

cajaapellido = Entry(ventana)
cajaapellido.grid(row=3, column=3, columnspan=3, sticky= W + E)
#_____________________________________________________________________________
##CAJA DE TEXTO PARA EL DIA Y ETIQUETA
etiDia = Label(text="Día:",font=("Exotc350 Bd BT", 14))
etiDia.grid(row=4, column=1, columnspan=2)

cajadia = Entry(ventana)
cajadia.grid(row=4, column=3, columnspan=3, sticky= W + E)
#_____________________________________________________________________________
#CAJA DE TEXTO PARA EL MES Y ETIQUETA
etiMes = Label(text="Mes:",font=("Exotc350 Bd BT", 14))
etiMes.grid(row=5, column=1, columnspan=2)

cajames = Entry(ventana)
cajames.grid(row=5, column=3, columnspan=3, sticky= W + E)
#___________________________________________________________________________
#CAJA DE TEXTO PARA EL AÑO Y ETIQUETA
etiAño = Label(text="Año:",font=("Exotc350 Bd BT", 14))
etiAño.grid(row=6, column=1, columnspan=2)

cajaaño = Entry(ventana)
cajaaño.grid(row=6, column=3, columnspan=3, sticky= W + E)
#_____________________________________________________________________________
#binario funcion 1 
def binaa():
        d=int(cajadia.get())
        m=int(cajames.get())
        a=int(cajaaño.get())
        bd=format(d, '0b' )
        bm=format(m, '0b')
        ba=format(a, '0b')

        Resultado['text'] = 'La fecha es: {}/{}/{} y  en binario es:{}/{}/{}'.format(d,m,a,bd,bm,ba)

   

#FUNCION 2 PARA MOSTRAR AL REVES EL TEXTO
def Diasvividos():
    fechaString = f"{cajaaño.get()}-{cajames.get()}-{cajadia.get()}"
    dato = datetime.strptime(fechaString, '%Y-%m-%d')

    today= datetime.today()
    
    dat1 = today
    dat2 = dato
    answer = abs(dat1-dat2).days 

    resp = f"Usted nació el {dato} y ha vivido {answer} días."

    Resultado.configure(text = resp)

#FUNCION 3 PARA MOSTRAR SI EL NOMBRE ES PAR O IMPAR
def PARIMPAR():
    name1 = f"{cajanombre.get()}"
    surname = f"{cajaapellido.get()}"

    contname = len(name1)
    contsurmame = len(surname)


  
#--Validaciones para nombre y apellido 
    if contname % 2 == 0:
        NB = f"su Nombre {name1} es número Par  "
    else:
        NB = f"su Nombre {name1} es número Inpar  "

    if contsurmame % 2 == 0:
        PLL = f"su Apellido {surname} es número Par ."
    else:
        PLL = f"su Apellido {surname} es número Inpar ."

    resp = f"{NB} y  {PLL} "

    Resultado.configure(text =resp )

#FUNCION 4 MOSTRAR LA CANTIDAD DE VOCALES Y CONSONANTES EN EL TEXTO
def vocalconson():
        navi=str(cajanombre.get())
        api=str(cajaapellido.get())
        cuen = 0
        for carac in navi:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuen += 1
        for carac in api:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuen += 1
        c1=len(navi)
        c12=len(api)
        consta=c1+c12-cuen

        Resultado['text'] = 'Su nombre y apellido tienen {} vocales y {} consonantes'.format(cuen,consta)
     

#FUNCION 5 PARA MOSTRAR AL REVES EL TEXTO
def ALREVES():
    reva = cajanombre.get()+" "+cajaapellido.get()
    reva = reva[::-1]
    Resultado["text"] = cajanombre.get() + " " + cajaapellido.get() + " al revés es: " + reva


#BOTONES
#_________________________________________________________________________________________
funcion1 = Button(ventana, text = "Función 1", command=binaa, font=("Exotc350 Bd BT", 10), padx= 10, pady=8)
funcion1.grid(row=7, column=1)
funcion2 = Button(ventana, text = "Función 2", command=Diasvividos ,font=("Exotc350 Bd BT", 10),padx= 10, pady=8)
funcion2.grid(row=7, column=2)
funcion3 = Button(ventana, text = "Función 3",command= PARIMPAR,font=("Exotc350 Bd BT", 10), padx= 10, pady=8)
funcion3.grid(row=7, column=3)
funcion4 = Button(ventana, text = "Función 4", command=vocalconson, font=("Exotc350 Bd BT", 10),padx= 10, pady=8)
funcion4.grid(row=7, column=4)
funcion5 = Button(ventana, text = "Función 5",command=ALREVES,font=("Exotc350 Bd BT", 10),padx= 10, pady=8)
funcion5.grid(row=7, column=5)
#_____________________________________________________________________________________________
#ETIQUETA PARA MOSTRAR RESULTADO
Resultado = Label(ventana, font=("Exotc350 Bd BT", 14))
Resultado.grid(row=8, column=1, columnspan=6)
ventana.mainloop()