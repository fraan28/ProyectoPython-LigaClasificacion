import partidos
import clasificacion

if __name__ == "__main__":
    liga = partidos.leerPartidos("liga.csv")
    clasificacion.impClasificacion(liga)
