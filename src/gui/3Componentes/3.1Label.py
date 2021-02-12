
from tkinter import *
"""
Sintaxis --> nombreLabel = Label (contenedor, opciones)
"""

root = Tk()
miFrame = Frame(root, width = 1000, height = 1000)
miFrame.pack()

miLabel = Label(miFrame, text = "Prueba label 1")
miLabel.place(x=50, y=50) #miLabel.pack()
#No le damos nombre al label, pero luego no podemos hacer referencia a él
Label(miFrame, text = "Prueba label 2", fg = "red", font = ("Comic Sans MS" , 21)).place(x=50, y=100)

imagenCara = PhotoImage (file = "gifHomer.gif") #Solo gif o PPM/PGM
miLabel2 = Label (miFrame, image = imagenCara, ).place(x=100, y = 300)

root.mainloop()