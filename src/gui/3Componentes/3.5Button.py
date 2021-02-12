from tkinter import *

root = Tk()
miFrame = Frame(root, width = "500", height = "500", bg = "green")
miFrame.pack()

texto = StringVar()
miLabel = Label(miFrame, textvariable = texto, fg = "grey")
miLabel.place(x=10, y=50)

def pulsarBoton():
    texto.set(texto.get() + "Has pulsado el botón ")
miBoton = Button(miFrame, text="Aceptar", command = pulsarBoton)
miBoton.place(x=50, y=130)

root.mainloop()