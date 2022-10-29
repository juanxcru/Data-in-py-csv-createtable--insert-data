import csv
import os
import sqlite3
import datetime

from creartabla import CrearTabla, CrearTablaID
from insertardatos import InsertarDatos

#aclarar que id integer, primer campo de csv y demas text.

logFile = open ("log.txt","at")

logFile.write("Fecha Ejecucion : {fecha}\n".format( fecha =datetime.datetime.now()))

#ingreso del path de donde esta el archivo de la db  ejemplo : carpeta/carpeta2/archivo.db 
bdPath = input ("Ingrese nombre/ruta a partir de este directorio, de la db (archivo.db) :/")


try :
    conn = sqlite3.connect(bdPath)
except Exception as err:
    print("Error: ", str(err)) #deberia ser en el log
    logFile.write("Error : {e}\n".format(e=str(err)))
c = conn.cursor()

absolutePath = os.getcwd()

#ingreso del path de donde esta el archivo de csv  ejemplo : carpeta/carpeta2/archivo.db 

relativePath = input("Ingrese nombre/ruta a partir de este directorio, de su .csv :/")
try:
    csvPath = open(absolutePath + "/" + relativePath,"r")
except Exception as err:
    print("Error: ", str(err)) #deberia ser en el log
    logFile.write("Error : {e}\n".format(e=str(err)))
    
delim = input("Ingrese delimitador de csv : ")

try :
    lista = csv.reader(csvPath, delimiter=delim)
    logFile.write("Se abrio el siguiente archivo {path}\n".format(path=csvPath))
except Exception as err:
    print("Error: ", str(err)) #deberia ser en el log
    logFile.write("Error : {e}\n".format(e=str(err)))
    
nombreTabla = input("Ingrese nombre de la tabla : ")
#para crear si no existe (nombre tabla)
queryTabla = CrearTablaID (nombreTabla, lista)
#pasar csvPath por argumento, y seekear al 0 del file, adentro.

try :
    c.execute(queryTabla)
    logFile.write("Se creo una tabla\n")
    logFile.write("Se hizo la siguiente query {query}\n".format(query=queryTabla))
except Exception as err:
    print("Error: ", str(err)) #deberia ser en el log
    logFile.write("Error : {e}\n".format(e=str(err)))
    
conn.commit()

#para insertar
#para volver atras el "puntero" despues de los next() de la funcion
csvPath.seek(0)
header = next(lista)
queryDato = InsertarDatos(nombreTabla, header)
try :
    c.executemany(queryDato,lista);
    logFile.write("Se hizo la siguiente query {query}\n".format(query=queryDato))
except Exception as err:
    print("Error: ", str(err)) #deberia ser en el log
    logFile.write("Error : {e}\n".format(e=str(err)))
        
conn.commit()

c.close()
conn.close()
logFile.close()





