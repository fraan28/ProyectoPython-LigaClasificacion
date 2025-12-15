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
    """Función que recibe por parámetros una lista de partidos y devuelve los puntos obtenidos"""
    ganados = lista_partidos[0]
    empatados = lista_partidos[1]
    return 3 * ganados + empatados

# InfoEquipos(datosliga,equipos): Función que recibe la lista de diccionarios con los datos de
# la liga y el conjunto de equipos y devuelve una lista de tuplas, en cada tupla se guarda un equipo
# con los partidos ganados, empatados y perdidos y los puntos obtenidos. Esta función utiliza internamente: (Adrián)
def infoEquipos(datosliga, equipos):
    informacionEquipos = {}
    for equipo in equipos:
        informacionEquipos.update({
            equipo: [0, 0, 0]
        })

    for p in datosliga:
        local = p['local']
        visitante = p['visitante']
        resultado = [p['goles_local'], p['goles_visitante']]

        gana = quienGana(resultado)

        if gana == 1:
            informacionEquipos[local][0] += 1
            informacionEquipos[visitante][2] += 1
        elif gana == -1:
            informacionEquipos[visitante][0] += 1
            informacionEquipos[local][2] += 1
        else:
            informacionEquipos[local][1] += 1
            informacionEquipos[visitante][1] += 1

    lista = []
    for equipo, datos in informacionEquipos.items():
        lista.append([equipo, datos[0], datos[1], datos[2], puntos(datos)])

    return lista

# impClasificacion(liga):Recibe la lista de diccionarios generado a partir de la función anterior,
# genera los datos de la clasificación y los imprime por pantalla. Esta función utiliza interna las siguientes funciones: (Fran)
def impClasificacion(liga):
    """ 
    Mostrar la clasificación de la liga

    Parameters:
        liga (list): Lista obtenida de "partidos.py" en la función "leerPartidos"
    """
    eqs = equipos(liga)
    info = infoEquipos(liga, eqs)
    clasif = clasificacion(info)

    print("CLASIFICACIÓN FINAL LIGA")
    print("# ------ #")
    print("- | Equipo | Ganados | Empatados | Perdidos | Puntos")

    pos = 0
    for equipo, ganados, empatados, perdidos, puntos in clasif:
        pos += 1
        print(f"{pos} | {equipo} | {ganados} | {empatados} | {perdidos} | {puntos}")

    print("# ------ #")
