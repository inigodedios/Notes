#Distintas formas de bucles
#FOR
for i in range(2):
    print("Valor de la variable" + str(i))
    print (f"valor de la variable {i}") #Otra forma. Fijarse en la f y las {}

for i in range(5,10): #10 no incluido
    print("Valor de la variable" + str(i))

for i in range(5,36,6): #Comienza en 5, acabe en 36 y va de 6 en 6
    print("Valor de la variable" + str(i))

nombre = "pedro"
for i in range(len(nombre)): #len devuelve el numero de caracteres de la variable nombre
    print("Número de caracteres" + str(i))


for i in ["Enero", "Febrero", "Marzo"]:
    print("Mes: " + i) #Imprime el mes por cada uno de los elementos de la lista

for i in ["Enero", "Febrero", "Marzo"]:
     print("Mes2: " + i, end= " ") #Establecemos como acaba el print
print("") #Ignorar

for i in "correo@gmail.com":
     print("hola", end= " ") #Imprime hola tantas veces como el número de caracteres
     print(i)

for i in "correo@gmail.com":
    if i == "@" or i == ".com":
        correcto = True
        print(correcto)
    else:
        correcto = False


#WHILE
i = 3
while i<25:
    print("Hola" + str(i))
    i+=1 #Para que no sea un bucle infinito
    if i == 20:
        break