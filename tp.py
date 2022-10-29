import csv
import os
import sqlite3


from creartabla import CrearTabla, CrearTablaID
from insertardatos import InsertarDatos

#aclarar que id integer, primer campo de csv y demas text.


#ingreso del path de donde esta el archivo de la db  ejemplo : carpeta/carpeta2/archivo.db 
bdPath = input ("Ingrese nombre/ruta a partir de este directorio, de la db (archivo.db) :/")
conn = sqlite3.connect(bdPath)
c = conn.cursor()

abPath = os.getcwd()

#ingreso del path de donde esta el archivo de csv  ejemplo : carpeta/carpeta2/archivo.db 

rePath = input("Ingrese nombre/ruta a partir de este directorio, de su .csv :/")
csvPath = open(abPath + "/" + rePath,"r")

delim = input("Ingrese delimitador de csv : ")
nombreTabla = input("Ingrese nombre de la tabla : ")
lista = csv.reader(csvPath, delimiter=delim)

#para crear si no existe (nombre tabla)
queryTabla = CrearTablaID (nombreTabla, lista)
c.execute(queryTabla)
conn.commit()

#para insertar
#para volver atras el "puntero" despues de los next() de la funcion
csvPath.seek(0)
header = next(lista)
queryDato = InsertarDatos(nombreTabla, header)
c.executemany(queryDato,lista);

    
        
conn.commit()








