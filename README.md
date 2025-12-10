# ProyectoPython-LigaClasificacion
Proyecto en la asignatura optativa Python con mis compañeros de clase Adrián Moreno Martos y Eliana Gabriela Alonso Amaya (Por cierto soy Francisco Tebar Muro)

# Planificación:
INSTRUCCIONES. Cada pareja o grupo debe repartir las 7 funciones a realizar entre cada
componente, se debe hacer seguimiento con repositorio en GitHub. En el fichero
README.md del repositorio debe aparecer el reparto de tareas a cada integrante. Una vez
creado el repositorio, invita como colaboradores al resto de participantes del grupo y al
profesor: cfergar586, con permisos de edición.
ENUNCIADO DEL PROYECTO. Partiendo del fichero csv liga.csv con los resultados de las
jornadas de liga 2015-2016, realizar un programa que muestre la tabla de clasificación al
final de la liga, en el que debe aparecer el orden en que ha quedado cada equipo, los
partidos ganados, los partidos empatados y los partidos perdidos, y por último los puntos
conseguidos. Para realizar este programa vamos a construir varias funciones:

● LeerPartidos(): Función que lee el fichero CSV y devuelve los datos del mismo en
una lista de diccionarios. (Adrián)

● impClasificacion(liga):Recibe la lista de diccionarios generado a partir de la función
anterior, genera los datos de la clasificación y los imprime por pantalla.
Esta función utiliza interna las siguientes funciones: (Fran)

● Equipos(datosliga): Función que recibe la lista de diccionarios con los datos de la liga
y devuelve un conjunto con los equipos de la liga. (Fran)

● InfoEquipos(datosliga,equipos): Función que recibe la lista de diccionarios con los
datos de la liga y el conjunto de equipos y devuelve una lista de tuplas, en cada tupla
se guarda un equipo con los partidos ganados, empatados y perdidos y los puntos
obtenidos.
Esta función utiliza internamente: (Adrián)

● QuienGana(resultado): Función que recibe un resultado y devuelve un 0 si es
un empate, un 1 si gana el equipo de casa y -1 si gana el equipo visitante. (Adrián)

● Puntos(info): Función que recibe una lista con los partidos ganados,
empatados y perdidos y devuelve los puntos obtenidos. (Gabriela)

● Clasificacion(datos): Recibe la lista generada con la función anterior y la ordena
según el número de puntos.(Gabriela)

Las funciones deben incluir comentarios para que aparezcan con comando help(function). 
