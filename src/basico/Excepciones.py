
def division(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError: #Si intentamos dividir entre 0
        print("No se puede dividir entre 0")


while True: #Bucle infinito. Si se meten datos correcto, el bucle se para, si no, sigue pidiendo datos de forma infinita
    try:
        num1 = int (input("Introduce un número: "))
        num2 = int (input("Introduce un número: "))
        break
    except ValueError:
        print("Debes introducir un número")

print (division(num1, num2))


#Otra opción sería enlazando excepciones
def division2 (num1, num2):
    try:
        num1 = int(input("Introduce un número2: "))
        num2 = int(input("Introduce un número2: "))
        return num1/num2
    except ValueError:
        return "Debes introducir un número"
    except ZeroDivisionError ("No puedes dividir entre 0") as DivisionError:
        return DivisionError + "No puedes dividir entre 0 x2"
    except: #Error general
        print("Ha ocurrido un error desconocido")
    finally:
        return "Mensaje final"

print(division2(num1,num2))


def division3 ():
    try:
       operacion = 4/5
       return operacion
    finally:
        return "Se ha dividido de forma correcta 4/5"

print(division3())

#Lanzar excep
def division4 (num1,num2):
    if num2<=0:
        raise ZeroDivisionError("NO se puede dividir entre 0")
    else: 
        return num1/num2

division4(1,0)
print(division4(2,2))