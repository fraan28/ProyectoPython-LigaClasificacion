import partidos

parts = partidos.LeerPartidos("liga.csv")
for parte in parts:
    print(parte['FT']) # Prueba