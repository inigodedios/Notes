from tkinter import *
#Cuadro de texto/comentario. El texto en una o más lineas

root = Tk()
miFrame = Frame(root, width = "1200", height = "1200", bg = "green")
miFrame.pack()

cuadroComentario = Text (miFrame, width ="100", height = "5").place(x=50, y=100)

root.mainloop()