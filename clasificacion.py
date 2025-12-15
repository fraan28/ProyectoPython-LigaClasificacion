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
