import partidos
import clasificacion

liga = partidos.leerPartidos("liga.csv")
eqs = clasificacion.equipos(liga)
print(eqs)
info = clasificacion.infoEquipos(liga, eqs)
print(info)
clasificacion.impClasificacion(liga)