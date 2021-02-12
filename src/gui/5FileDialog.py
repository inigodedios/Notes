from tkinter import *
from tkinter import filedialog
#TODO comprobar que funciona bien
root = Tk()

def abrirFichero():
    fichero = filedialog.askopenfilename(title = "Abrir", initialdir = "/Users/inii/Desktop",
        filetypes = (("Ficheros de Excel", "*.xlsx"), ("Ficheros de Texto", "*.txt"), ("Todos los ficheros", "*.*")))
    print(fichero)

Button (root, text="Abrir archivo", command=abrirFichero).pack()

root.mainloop()