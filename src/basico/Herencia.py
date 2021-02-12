#Leer antes la clase Poo.py
class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar (self):
        self.enMarcha = True

    def acelerar (self):
        self.acelera = True

    def frenar (self):
        self.frena = True

    def toString (self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
              self.enMarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena)

class Moto (Vehiculo): #Para heredar, se para por parametro la clase padre
    permisoMoto = ""
    def permisoMoto (self):
        self.permisoMoto = "A2"
    def toString(self): #Sobreescribimos el metodo toString de la clase vehiculo
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
              self.enMarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena, "\nPermiso moto: ", self.permisoMoto)

class motoPersonalizada(Vehiculo):
    def __init__(self, matricula, marca, modelo):
        super().__init__(marca, modelo)  #Hemos llamado al constructor que hereda de la clase Vehiculo
        self.matricula = matricula


class VeElectrico():
    def __init__(self):
        self.autonomia = 600

class biciElectrica (Vehiculo, VeElectrico): #Herencia multiple
    pass

moto1 = Moto("Tesla", "X")
moto1.permisoMoto()
moto1.toString()

#Hereda el constructor de la primera clase que hemos indicado al definir la clase biciElectrica (Vehiculo)
miBiciElectrica = biciElectrica("MarcaX", "ModeloX")