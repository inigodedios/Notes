#Programacion Orientada a Objetos

#Creación de una clase, metodos (no funciones), constructor
class Coche():
    def __init__(self): #Constructor (__init__)
        self.largoChasis = 250
        self.anchoChasis = 100
        self.__ruedas = 4 #Estamos encapsulando la variable ruedas de tal forma que solo se puede acceder a ella en la propia clase
        self.enMarcha = False


    def  arrancar (self): #self es el this the Java. En Java estaba de forma implícita y no se ponia.
        check = self.__checkCoche()
        if check == True:
            self.enMarcha = True
        else:
            self.enMarcha = False

    def estado (self): #Esto es un método, no una funcion. Cuando un definimos "def" dentro de una clase, es un método, si los definimos fuera de la clase, es una función
        if self.enMarcha:
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
    def infoCoche (self):
        print ("El chasis mide", self.largoChasis, "y tiene ", self.__ruedas, "ruedas") #Debemo poner __ruedas porque esta encapsulado

    def __checkCoche (self): #Método encapsulado
        if self.largoChasis<100 and self.anchoChasis<50 and self.__ruedas<4:
            return False
        else:
            return True

#Aqui fuera de la clase
coche1 = Coche() #Instanciando una # clase
print("El largo del coche es: ", coche1.largoChasis)
print("El largo del coche es: " + str(coche1.largoChasis))
coche1.arrancar()
print(coche1.estado())

coche1.infoCoche()
coche1.ruedas =2 #Para python __ruedas ≠ ruedas
coche1.__ruedas =2
coche1.infoCoche() #No cambia el número de ruedas en la linea superior porque esta encapsulada la variable


"""
GESTIONAR IMPORTS

- Opción 1
from basico.Condicionales import eligeEdad
eligeEdad ("Marta")

- Opción 2
from basico.Condicionales import *
eligeEdad("Marta")
evaluacion(8)

- Opción 3
import basico.Condicionales
Condicionales.eligeEdad("Marta")

"""


"""
GESTIONAR PAQUETES
Cuando creamos un paquete, debemos indicarlo añadiendo un archivo que le llamaremos __init__.py

"""