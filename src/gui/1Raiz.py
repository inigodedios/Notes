from tkinter import *

raiz = Tk()

#Algunas propiedades
raiz.title("Ventana Python") # Título de la ventana
raiz.resizable(0,0) #Poder cambiar el tamaño
raiz.iconbitmap('X-Wing_-_02_35411.ico') #Icono de la ventana (.ico)
raiz.geometry('300x300') #Medida de la ventana
raiz.config(cursor="pirate",bg="beige",bd=10,relief="ridge") #Configuración de la raíz

raiz.mainloop()