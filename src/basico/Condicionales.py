
#nota = input() #IMPORTANTE tod0 lo que introduzcamos mediante el input lo coge como string

def evaluacion(nota):
    if nota>= 5 and nota<=10 :
        valoracion  = "Apto"
    elif 0<nota<5:
        valoracion = "No apto"
    else:
        valoracion = "Dato no correcto"
    return print(valoracion)

evaluacion(int(input("Introduce la nota \n"))) #Hacemos casting por input()

def eligeEdad (nombre):
    if nombre in ("Pedro", "Marta", "Lucas", "Maria"):
        print("Tu nombre esta en la lista")
    else:
        print("Tu nombre no esta en la lista")

eligeEdad(input("¿Cuál es tu nombre \n"))