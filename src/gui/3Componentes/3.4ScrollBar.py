from tkinter import *
root = Tk()
miFrame = Frame(root, width = "1200", height = "1200", bg = "green")
miFrame.pack()

cuadroComentario = Text (miFrame, width ="100", height = "5")
miScrollBar = Scrollbar (miFrame, command = cuadroComentario.yview)
cuadroComentario.place(x=50, y=50)
miScrollBar.place(x=10, y=50)
cuadroComentario.config(yscrollcommand = miScrollBar.set)

root.mainloop()