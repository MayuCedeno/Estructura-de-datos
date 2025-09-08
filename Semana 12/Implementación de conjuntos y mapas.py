import time

# Registro de jugadores por equipo usando diccionarios y conjuntos
torneo = {}  # Mapa: clave = equipo, valor = conjunto de jugadores

# Función para agregar un jugador a un equipo
def agregar_jugador(equipo, jugador):
    if equipo not in torneo:
        torneo[equipo] = set()
    torneo[equipo].add(jugador)

# Función para mostrar todos los equipos y jugadores
def mostrar_torneo():
    for equipo, jugadores in torneo.items():
        print(f"Equipo: {equipo}")
        for jugador in jugadores:
            print(f"  - {jugador}")

# Medición de tiempo de ejecución
inicio = time.time()

# Agregar datos de ejemplo
agregar_jugador("Dragones", "Jenny")
agregar_jugador("Dragones", "Adriana")
agregar_jugador("Dragones", "Amy")  # Duplicado, no se agregará
agregar_jugador("Tigres", "Blanca")
agregar_jugador("Tigres", "Alan")
agregar_jugador("Leones", "Virjilio")

# Mostrar reporte del torneo
mostrar_torneo()

fin = time.time()
print(f"\nTiempo de ejecución: {fin - inicio:.6f} segundos")