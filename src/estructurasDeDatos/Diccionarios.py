"""
DICCIONARIOS
Estructura de datos que nos permite almacenar valores como enteros, strings, decimales, listas... (alternando tambien)
Los dastos se almacenan asociados a una clave única. Se crea una asociacion clave:valor
Los elementos no estan ordenados
"""

#clave:valor
diccionario1 = {"España":"Madrid", "Provincias":17, "Pais Vasco": ["Bizkaia", "Gipuzkoa", "Alava"]}
print(diccionario1)
print(diccionario1["España"])

diccionario1["Italia"] = "Lisboa" #Añadir elemento (Error hecho adrede)
print(diccionario1)
diccionario1["Italia"] = "Roma" #Sobreescribir elemento. Una única clave
print(diccionario1)
del diccionario1["Italia"] #Eliminar elemento
print(diccionario1)

#Métodos
print(diccionario1.keys())
print(diccionario1.values())
print(len(diccionario1))