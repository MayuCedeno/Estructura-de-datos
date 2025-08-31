# Traductor básico Español <-> Inglés con diccionario
def mostrar_menu():
    print("\n==================== MENÚ ====================")
    print("1. Traducir una frase")
    print("2. Agregar palabras al diccionario")
    print("0. Salir")
    return input("Seleccione una opción: ")

# Diccionario base (bidireccional: inglés -> español y español -> inglés)
diccionario = {
    "time": "tiempo", "tiempo": "time",
    "person": "persona", "persona": "person",
    "year": "año", "año": "year",
    "way": "camino", "camino": "way",
    "day": "día", "día": "day",
    "thing": "cosa", "cosa": "thing",
    "man": "hombre", "hombre": "man",
    "world": "mundo", "mundo": "world",
    "life": "vida", "vida": "life",
    "hand": "mano", "mano": "hand",
    "part": "parte", "parte": "part",
    "child": "niño", "niño": "child",
    "eye": "ojo", "ojo": "eye",
    "woman": "mujer", "mujer": "woman",
    "place": "lugar", "lugar": "place",
    "work": "trabajo", "trabajo": "work",
    "week": "semana", "semana": "week",
    "case": "caso", "caso": "case",
    "point": "punto", "punto": "point",
    "government": "gobierno", "gobierno": "government",
    "company": "empresa", "empresa": "company"
}

def traducir_frase(diccionario):
    frase = input("\nIngrese una frase: ").lower()
    palabras = frase.split()
    traduccion = []

    for palabra in palabras:
        palabra_limpia = ''.join([c for c in palabra if c.isalpha()])  # quitar signos
        traduccion.append(diccionario.get(palabra_limpia, palabra))  # traducir si existe

    print("\nTraducción: " + " ".join(traduccion))

def agregar_palabra(diccionario):
    palabra1 = input("\nIngrese la palabra en inglés: ").lower()
    palabra2 = input("Ingrese su traducción en español: ").lower()
    diccionario[palabra1] = palabra2
    diccionario[palabra2] = palabra1
    print(f"\nLa palabra '{palabra1}' <-> '{palabra2}' fue agregada al diccionario.")

# Programa principal
while True:
    opcion = mostrar_menu()
    if opcion == "1":
        traducir_frase(diccionario)
    elif opcion == "2":
        agregar_palabra(diccionario)
    elif opcion == "0":
        print("\n¡Gracias por usar el traductor!")
        break
    else:
        print("\nOpción no válida, intente de nuevo.")