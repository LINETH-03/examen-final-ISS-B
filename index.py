from tkinter import*
root = Tk()
ancho = 550
alto = 300
root.geometry(str(ancho)+ "x"+str(alto))
root.title("Examen Final Lily Pérez")
Saludo = Label(text="Bienvenidos",font=("Exotc350 Bd BT",25)).place(x=190,y=8)
lblname=Label(text="Nombre",font=("Bahnschrift SemiLight Condensed",11)).place(x=80,y=40)
entrada=StringVar()
entrada.set("")
txtnombre=Entry(root,textvariable=entrada).place(x=135,y=50)

lblape=Label(text="Apellido",font=("Bahnschrift SemiLight Condensed",11)).place(x=80,y=60)
entrada=StringVar()
entrada.set("")
txtape=Entry(root,textvariable=entrada).place(x=135,y=70)

lbldia=Label(text="Día ",font=("Bahnschrift SemiLight Condensed",11)).place(x=80,y=90)
entrada=StringVar()
entrada.set("")
txtdia=Entry(root,textvariable=entrada).place(x=135,y=100)

lblmes=Label(text="Mes",font=("Bahnschrift SemiLight Condensed",11)).place(x=80,y=120)
entrada=StringVar()
entrada.set("")
txtmes=Entry(root,textvariable=entrada).place(x=135,y=130)

lblaño=Label(text="Año",font=("Bahnschrift SemiLight Condensed",11)).place(x=80,y=150)
entrada=StringVar()
entrada.set("") 
txtaño=Entry(root,textvariable=entrada).place(x=135,y=160)
btnFuncion1 = Button(root, text= "Función  1",font=("Bahnschrift SemiLight Condensed",10),width=12).place(x=20,y=190)
btnFuncion1 = Button(root, text= "Función 2",font=("Bahnschrift SemiLight Condensed",10),width=12).place(x=115 ,y=190)
btnFuncion1 = Button(root, text= "Función 3",font=("Bahnschrift SemiLight Condensed",10),width=12).place(x=211,y=190)
btnFuncion1 = Button(root, text= "Función 4",font=("Bahnschrift SemiLight Condensed",10),width=12).place(x=305,y=190)
btnFuncion1 = Button(root, text= "Función 5",font=("Bahnschrift SemiLight Condensed",10),width=12).place(x=400,y=190)
root.mainloop()