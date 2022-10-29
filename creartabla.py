def CrearTabla (nombreTabla, header) :
 
    salida = 'CREATE TABLE IF NOT EXISTS ' + nombreTabla + '( ' + header[0] + ' INTEGER PRIMARY KEY , '  + ', '.join("{col} TEXT ".format(col=col) for col in header[1:])  + ')'
    return salida

def CrearTablaID (nombreTabla, lista) :
    
    header = next(lista)
    priCelda = next(lista)[0]
    
    for char in priCelda:
       if(char.isalpha()) :
            salida = 'CREATE TABLE IF NOT EXISTS ' + nombreTabla + '( ' + header[0] + ' TEXT PRIMARY KEY , '  + ', '.join("{col} TEXT ".format(col=col) for col in header[1:])  + ')'
            return salida
    salida = 'CREATE TABLE IF NOT EXISTS ' + nombreTabla + '( ' + header[0] + ' TEXT PRIMARY KEY , '  + ', '.join("{col} TEXT ".format(col=col) for col in header[1:])  + ')'
    
    return salida