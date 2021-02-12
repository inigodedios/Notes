from tkinter import *
from tkinter import messagebox
#TODO comprobar que funcionan bien las ventanas emergentes
root = Tk()
miFrame = Frame(root, width = "700", height = "300", bg = "green").pack()

def abrirVentanaEmergente():
    messagebox.showinfo("ventana emergente")
    messagebox.showwarning("Atención")
    messagebox.showerror("Error")

Label(root, text="Pulsa el boton").place(x=50, y=20)
Button(root, text="Abrir ventana emergente", command=abrirVentanaEmergente).place(x=50, y=50)

root.mainloop()