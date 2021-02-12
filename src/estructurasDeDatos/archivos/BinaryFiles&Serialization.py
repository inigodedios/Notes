import pickle
from src.notes.basico.Herencia import Vehiculo
#Leer antes la clase TextFiles.py

"""
dump() --> volcar datos al fichero binario externo
load() --> carga datos del fichero binario externo
"""

coche1 = Vehiculo("BMW", "Serie 6")
coche2 = Vehiculo("BMW", "Serie 7")
coche3 = Vehiculo("BMW", "Serie 8")
cochesLista = [coche1, coche2, coche3]

#Guardamos datos en fichero binario
ficheroGuardar = open("ficheroBinario", "wb")
pickle.dump(cochesLista, ficheroGuardar) #Guardamos la lista cochesLista en ficheroGuardar
ficheroGuardar.close()

#Abriendo fichero binario
ficheroApertura = open("ficheroBinario", "rb")
misCoches = pickle.load(ficheroApertura)
ficheroApertura.close()
for  i in misCoches:
    print (i)
    print (i.toString())