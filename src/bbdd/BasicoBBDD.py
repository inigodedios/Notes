import sqlite3

miConexion = sqlite3.connect("primeraBase") #1
miCursor=miConexion.cursor() #2
#Autoincrement --> gestiona automaticamente el ID, no hay que insertar ese valor
miCursor.execute("CREATE TABLE ALUMNOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_APELLIDO VARCHAR(50) UNIQUE, "
                 "EDAD INTEGER, DIRECCION VARCHAR(50))") #Comentar para que no de error, la tabla ya existe

miCursor.execute("INSERT INTO ALUMNOS VALUES (null, 'María García', 45, 'España')") #3 #Debemos poner null porque lo gestiona la propia base de datos el id
alumnos =[
    ("Mario García", 16, "España"),
    ("Maria Rodriguez", 16, "España"),
    ("Lucia Rodriguez", 16, "España")
]
miCursor.executemany("INSERT INTO ALUMNOS VALUES (null, ?,?,?)", alumnos) #Insertar tantos interrogantes como campos tiene la tabla

miCursor.execute("SELECT * FROM ALUMNOS")#3
infoBd= miCursor.fetchall() #Guarda en infoBd la consulta de la linea anterior
print(infoBd) #4
for alumno in infoBd:
    print(alumno)

miCursor.execute("DELETE FROM ALUMNOS ") #Cada vez que ejecutamos se insertan nuevos alumnos; para tener menos datos

miConexion.commit() #5
miCursor.close() #6
miConexion.close() #7


"""
Otra opción para cuando ejecutemos una sentencia es mediante la triple comilla (quitar espacio entre la tripe comilla, es 
para identifique bien el comentario

miCursor.execute(" ""
    CREATE TABLE ALUMNOS(
    NOMBRE_APELLIDO VARCHAR(50) PRIMARY KEY,
    EDAD INTEGER,
    DIRECCION VARCHAR(50))
" ""
"""