
# Catálogo de Revistas - Búsqueda Recursiva
# Autor: [Tu Nombre]
# Descripción:
#   Este programa permite gestionar un catálogo de revistas y
#   realizar búsquedas de títulos usando una técnica recursiva.

# Catálogo inicial de revistas (lista de cadenas)
catalogo_revistas = [
    "National Geographic",
    "Scientific American",
    "Nature",
    "Forbes",
    "Time",
    "The Economist",
    "Harvard Business Review",
    "IEEE Spectrum",
    "Smithsonian",
    "Popular Science"
]

# Función de búsqueda recursiva

def busqueda_recursiva(lista, titulo, indice=0):
    """
    Busca un título en la lista de revistas de forma recursiva.

    Parámetros:
        lista (list): catálogo de revistas
        titulo (str): título a buscar
        indice (int): índice actual en la búsqueda

    Retorna:
        bool: True si el título fue encontrado, False en caso contrario
    """
    # Caso base: si llegamos al final de la lista y no encontramos
    if indice >= len(lista):
        return False

    # Comparamos el título actual con el buscado (ignorando mayúsculas/minúsculas)
    if lista[indice].lower() == titulo.lower():
        return True

    # Llamada recursiva al siguiente elemento
    return busqueda_recursiva(lista, titulo, indice + 1)

# Menú interactivo

def menu():
    while True:
        print("\n--- Catálogo de Revistas ---")
        print("1. Ver catálogo completo")
        print("2. Buscar revista por título")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nCatálogo de Revistas:")
            for revista in catalogo_revistas:
                print(f"- {revista}")

        elif opcion == "2":
            titulo = input("Ingrese el título de la revista a buscar: ")
            encontrado = busqueda_recursiva(catalogo_revistas, titulo)

            if encontrado:
                print(f"✔ Revista '{titulo}' encontrada en el catálogo.")
            else:
                print(f"✘ Revista '{titulo}' NO se encuentra en el catálogo.")

        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break

        else:
            print("⚠ Opción no válida. Intente de nuevo.")


# Ejecución principal del programa
if __name__ == "__main__":
    menu()