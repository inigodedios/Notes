
"""
LISTAS
Las listas sí se pueden modificar
El indice empieza desde la posición 0
"""
from src.notes.estructurasDeDatos import Tuplas

lista1 = [1,5,6,7,8,3]
lista2 = [True,False,2,"prueba"]

print(lista1)
print(lista1[2])
print(lista1[-4])
print(lista1[0:3])#Imprime desde la posición 0 a la 3 sin incluir la 3
print(lista1[2:5])
print(lista1[:3]) #Imprime desde la posición 0 a la 3 sin incluir la 3
print(lista1[3:]) #Imprime desde la posición 3 a la última

lista1.append("nuevo_ elemento") #Añade al final
lista1.insert(4,"nuevo_elemento") #Añade elemento en la posicion 4
lista1.extend([11,12,13,14,15]) #Añadimos elementos al final de la lista
lista1.remove(6)#Elimina de la lista el valor 6
lista1.pop()#Elimina de la lista el ultimo valor
print(lista1.index("nuevo_elemento")) #Devuelve el indice del primer elemento que encuentra
print("Pedro" in lista1) #Devulve true o false si esta Pedro en la lista
print(lista1)

lista3 = lista1+lista2
print(lista3)

valor1,valor2, valor3,valor4 = lista2
print(lista1)

lista = list(Tuplas.tupla1) #Convierte una tupla en una lista
tupla = tuple(lista) #Convierte una lista en una tupla

print(tupla.count(3)) #Cuenta el numero de veces que esta el valor 3