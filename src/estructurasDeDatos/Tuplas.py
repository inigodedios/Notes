"""
TUPLAS
Las listas no se pueden modificar, son inmutables. No se puede añadir, eleminar, mover elementos...
Si permite extraer partes como una nueva tupla, busquedas, comprobar si un elemento se encuentra en la tupla
El indice empieza desde la posición 0

Tuplas vs listas
Las tuplas son mas rapidas, ocupan menos espacio, formatean Strings, pueden utilizarse como claves en un diccionario
Listas entre corchetes
Tuplas entre parentesis (opcionales)

En lo demas funciona igual que una lista
"""
tupla1 = 2,3,3,3,3,True, "ejemplo"
tupla2 = (4,5,False, "ejemplo2")
tupla_unitaria = ("Pedro",)

num1, num2, premium, ejemplo = tupla2
print(num1, num2, premium,ejemplo)

lista = list(tupla1) #Convierte una tupla en una lista
tupla = tuple(lista) #Convierte una lista en una tupla
print(lista,tupla)
print(tupla1.count(3)) #Cuenta el numero de veces que tiene ese valor en la tupla/lista
print(len(tupla1))