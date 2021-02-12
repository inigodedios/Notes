from tkinter import *

root=Tk()

opcion=IntVar()
def imprimir():
    print (opcion.get())

#Se les debe asignar una variable y un valor para que funcionen correctamente
Radiobutton (root, text="Masculino", variable=opcion, value=1, command=imprimir).pack()
Radiobutton (root, text = "Femenino", variable=opcion, value=2, command=imprimir).pack()

root.mainloop()