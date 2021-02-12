from io import open

#EJEMPLO 1 - Solo escritura
#1,2 Abrimos el archivo. Si no existe, se crea
archivoTxt = open ("archivoDeTexto.txt", "w") #archivoTxt --> archivo en memoria; archivoDeTexto --> fichero en ordenador
#3. Manipular archivo
frase1 = "Primera linea de nuestro archivo txt"
frase2 = "\nSegunda linea de nuestro archivo txt"
archivoTxt.write(frase1)
archivoTxt.write(frase2)
#4. Cerrar archivo
archivoTxt.close()

#EJEMPLO 2 - Solo lectura
archivoTxt2 = open ("archivoDeTexto.txt", "r")
#texto1 = archivoTxt2.read() #Lee tod0
texto2 = archivoTxt2.readlines() #Almacena una cada linea en una lista
archivoTxt2.close()
#print(texto1)
"""
NO se pueden leer dos veces a la vez. 
Cuando abrimos un archivo el puntero se encuentra al comienzo por defecto, y cuando termina de leer en última posición. 
Por eso, si intentamos leer dos veces, como el puntero se va a encontrar en la última posición en la segunda lectura, no 
va a leer nada.
Podemos situar el puntero en la punto que queramos con el método seek() (seek(0) --> para situarlo en el caracter 0)
Descomentar la linea print(texto1) y la de texto1=... y comentar la de texto2 y las tres siguientes para hacer pruebas
"""
print(texto2)
print(texto2[0])
print(texto2[1])