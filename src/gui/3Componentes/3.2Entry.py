from tkinter import *
#Cuadro de texto. El texto en una sola linea

root = Tk()
miFrame = Frame (root, width = "1200", height = "1200", bg = "green")
miFrame.pack()
lNombre = Label(miFrame, text = "Nombre:")
cuadroTexto = Entry(miFrame)

lNombre.grid(row = 0, column = 0, padx = 500, pady = 30) #Si usamos grid() no podemos usar .place()
cuadroTexto.grid(row = 0, column = 1)

root.mainloop()