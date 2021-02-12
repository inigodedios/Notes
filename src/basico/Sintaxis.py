"""
EN PYTHON TOD0 ES UN OBJETO
TIPOS
Numericos --> int, float, complejos
Textos
Booleanos

OPERADORES
Aritméticos --> +,-,*,/,%(resto),**(exponente),//(Division entera)
Comparacion --> ==,!=,<,>,<=,>=
Lógicos --> AND, OR, NOT
Asignación --> =,+=,-=,*=,/=,%=,**=,//=
Especiales --> IS, IS NOT, IN, NOT IN
"""
print(10%3)
print(10**3)
print(10//3)

nombre = "iñigo"
print(type(nombre))
nombre = 5
print(type(nombre))

#CREACION DE MÉTODOS
def imprimir_mensajes(): #Declaracion de método
    print("Método sin parametros")
imprimir_mensajes() #Llamada a la funcion

def imprimir_mensajes(mensaje):
    print(mensaje)
imprimir_mensajes("Prueba de metodo con parametros")

def suma(num1, num2):
    suma = num1 + num2
    return (suma)
resultado = suma(1,6)
print(resultado)