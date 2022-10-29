def InsertarDatos (nombreTabla, header) :
    
    salida = ("INSERT INTO " + nombreTabla + "({col}) VALUES ({val})".format(col=", ".join(header[0:len(header)]), val=", ".join("?" * len(header))))
    return salida
