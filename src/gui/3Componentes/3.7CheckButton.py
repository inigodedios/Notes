from tkinter import *

root = Tk()
estacion = StringVar()
ocio = StringVar()

def seleccionado():
    print("----------" + estacion.get() + ocio.get() + "----------")


Checkbutton(root, text="Primavera", variable=estacion, onvalue="Primavera", offvalue="No primavera", command=seleccionado).pack()
Checkbutton(root, text="Verano", variable=estacion ,onvalue="Verano", offvalue="No verano", command=seleccionado).pack()
Checkbutton(root, text="Otoño", variable=estacion, onvalue="Otoño", offvalue="No otoño", command=seleccionado).pack()
Checkbutton(root, text="Invierno", variable=estacion, onvalue="Invierno", offvalue="No Invierno", command=seleccionado).pack()

Checkbutton(root, text="Playa", variable=ocio, onvalue="Playa", offvalue="No playa", command=seleccionado).pack()
Checkbutton(root, text="Piscina", variable=ocio, onvalue="Piscina", offvalue="No piscina", command=seleccionado).pack()
Checkbutton(root, text="Rio", variable=ocio, onvalue="Rio", offvalue="No rio", command=seleccionado).pack()

"""
Si nos fijamos, solo podemos seleccionar dos, ya que solo hemos usado dos variables en el CheckButton: estacion y ocio. Por 
eso salen las lineas. Si queremos que se puedan seleccionar todas, debemos crear una variable por cada CheckButton
"""

root.mainloop()
