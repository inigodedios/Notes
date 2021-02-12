from tkinter import *
"""
Debemos meter los Frames en la Raiz. La Raiz se adapará al tamaño del Frame,
aunque la Raiz puede ser más grande que el Frame
"""

raiz = Tk() #1
miFrame = Frame(raiz) #2
miFrame.pack() #3
miFrame.config (width="650", height="350") #4
#Decorados

miFrame.config(cursor="spider",bg="lightblue") #Configuración del marco
miFrame.pack(side="top", anchor="w") #Empaqueta el elemento en la raíz, si no, no se puede mostrar; paramestros para posición
# frame.pack(fill='x' o 'y' o 'both', expand=1 o 0) rellenar y expandir (se usan con fill=y 0 both) a las dimenciones del padre

raiz.geometry("700x700")
raiz.config(bg = "green")

raiz.mainloop()