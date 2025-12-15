# Equipos(datosliga): Función que recibe la lista de diccionarios con los datos de la liga 
# y devuelve un conjunto con los equipos de la liga. (Fran)
def equipos(datosliga) -> list[str]:
    equipos = []
    for partido in datosliga:
        for i in [partido['local'], partido['visitante']]:
            if i in equipos:
                continue
            equipos.append(i)
    return equipos

# Puntos(info): Función que recibe una lista con los partidos ganados, empatados y
# perdidos y devuelve los puntos obtenidos. (Gabriela)
def puntos(lista_partidos):
    ganados = lista_partidos[0]
    empatados = lista_partidos[1]
    return 3 * ganados + empatados
