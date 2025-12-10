import csv

# LeerPartidos(): Función que lee el fichero CSV y devuelve los datos del mismo en una lista de diccionarios. (Adrián)
def LeerPartidos(fichero):
    partidos = []
    try:
        with open(fichero, mode="r") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                partidos.append(fila)
    except:
        print("ERROR: Ha ocurrido un error al acceder/analizar el archivo CSV.")
    
    return partidos

