from tkinter import *
#TODO no funciona
root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu)

filemenu = Menu(barraMenu, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

editmenu = Menu(barraMenu, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu = Menu(barraMenu, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Archivo", menu=filemenu)
barraMenu.add_cascade(label="Editar", menu=editmenu)
barraMenu.add_cascade(label="Ayuda", menu=helpmenu)

root.mainloop()
