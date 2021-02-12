Un archivo lo podemos abrir en distintos modos:
- Lectura --> "r" --> Solo lectura
- Lectura en binario --> "rb" --> Solo lectura en binario
- Lectura y escritura --> "r+" --> Solo leer y escribir y escribir
- Lectura y escritura en binario --> "rb+" --> Solo leer y escribir y escribir en binario
- Escritura --> "w" --> Sobreescribe el archivo si existe. Crea el archivo si no existe
- Escritura en binario --> "wb" --> Sobreescribe el archivo si existe. Crea el archivo si no existe
- Escitura y lectura --> "w+" --> Sobreescribe el archivo si existe. Crea el archivo si no existe
- Escitura y lectura en binario --> "wb+" --> Sobreescribe el archivo si existe. Crea el archivo si no existe
- Añadir --> "a" --> Si el archivo existe, añade contenido al final, si no existe, lo crea y lo añade (a = append / concatenar)
- Añadir en binario --> "ab" --> Si el archivo existe, añade contenido al final, si no existe, lo crea y lo añade
- Añadir y lectura --> "a+" --> Si el archivo existe, añade contenido al final, si no existe, lo crea y lo añade. Permite leer
- Añadir y lectura en binario --> "a+" --> Si el archivo existe, añade contenido al final, si no existe, lo crea y lo añade. Permite leer

Pasos para guardar información en cualquiert tipo de archivo
1. Crear archivo
2. Abrir archivo
3. Manipular archivo
4. Cerrar archivo


SERIALIZACIÓN --> Ficheros binarios
El objetivo de la serialización es codificar en binario para que sea más cómodo a la hora de tratar con bbdd, de almacenar,
 para distribuirlo más facilmente...