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

# QuienGana(resultado): Función que recibe un resultado y devuelve un 0 si
# es un empate, un 1 si gana el equipo de casa y -1 si gana el equipo visitante. (Adrián)
def quienGana(resultado) -> int:
    if resultado[0] > resultado[1]:
        return 1
    elif resultado[0] < resultado[1]:
        return -1
    else:
        return 0

# Puntos(info): Función que recibe una lista con los partidos ganados, empatados y
# perdidos y devuelve los puntos obtenidos. (Gabriela)
def puntos(lista_partidos):
    ganados = lista_partidos[0]
    empatados = lista_partidos[1]
    return 3 * ganados + empatados
