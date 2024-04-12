def crear_estructura(names, goals, goals_avoided, assists):
    
    listaEstadisticas = []

    for name, goal, goal_avoided, assist in zip(names, goals, goals_avoided, assists):
        listaEstadisticas.append({
            "Nombre": name,
            "Goles": goal,
            "Goles evitados": goal_avoided,
            "Asistencias": assist
        }) 
    return listaEstadisticas


def mas_goles(listaJugadores):

    max_diccionario = max(listaJugadores, key=lambda x: x["Goles"])
    nombre_max = max_diccionario["Nombre"]
    goles_max = max_diccionario["Goles"]

    goleador = [nombre_max,goles_max]

    return goleador


def calcular_puntaje(jugador):
    
    puntaje = jugador["Goles"] * 1.5 + jugador["Goles evitados"] * 1.25 + jugador["Asistencias"] * 1
    
    return puntaje


def mas_influyente(listaJugadores):

    puntajes_ponderados = [calcular_puntaje(jugador)for jugador in listaJugadores]
    maximo = puntajes_ponderados.index(max(puntajes_ponderados))
    jugadorInfluyente = listaJugadores[maximo] ["Nombre"]

    return jugadorInfluyente


def promedio(total,cant):
    
    prom = total / cant

    return prom


def promGoleador(goleador,partidos):
    
    promg = promedio(goleador[1],partidos)

    return promg

def cantidad(listaJugadores):

    goles = 0
    for jugador in listaJugadores:
        goles = goles + jugador["Goles"] 

    return goles

def promEquipo(listaJugadores,partidos):
    
    golesE = cantidad(listaJugadores)
    promE = promedio(golesE,partidos)

    return promE