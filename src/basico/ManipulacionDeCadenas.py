nombre = "Pedro"
print(
    nombre.upper(),#Tod0 mayusculas
    nombre.lower(), #Tod0 minusculas
    nombre.capitalize(), #Mayuscula la primera letra, minusuculas las demas
    nombre.count('e'), #Cuenta cuantas "e"
    nombre.find('e'), #Cuenta la primera "e"
    nombre.isdigit(), #Devuelve True si es una cadena de solo digitos
    nombre.isalnum(), #Devuelve True si es una cadena alphanumerica
    nombre.isalpha(), #Devuelve True si todos los caracteres son alfabéticos
    nombre.split(), #Devuelve una lista de palabras, usando como separador los espacios
    nombre.split('e') ##Devuelve una lista de palabras, usando como separador la e
    )

"""
Más métodos en https://docs.python.org/es/3/library/stdtypes.html#text-sequence-type-str 
Apartado --> Cadenas de caracteres - str
"""

