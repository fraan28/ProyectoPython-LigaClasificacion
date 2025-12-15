import csv

# LeerPartidos(): Función que lee el fichero CSV y devuelve los datos del mismo en una lista de diccionarios. (Fran)
def leerPartidos(fichero):
    """ 
    Leer los partidos del fichero pasado por parámetro

    Parameters:
        fichero (str): Fichero de la liga en CSV

    Returns:
        list: Lista de los partidos
    """
    partidos = []
    try:
        with open(fichero, mode="r") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                goles = fila['FT'].split('-')
                golesParte2 = fila['HT'].split('-')
                partidos.append({
                    'local': fila['Team 1'],
                    'visitante': fila['Team 2'],
                    'goles_local': int(goles[0]) + int(golesParte2[0]),
                    'goles_visitante': int(goles[1]) + int(golesParte2[1])
                })
    except:
        print("ERROR")
    
    return partidos
