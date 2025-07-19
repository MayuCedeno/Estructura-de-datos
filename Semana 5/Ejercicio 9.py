# Solicitar una palabra al usuario
palabra = input("Ingresa una palabra: ").lower()

# Inicializar un diccionario para contar las vocales
vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Recorrer cada letra de la palabra
for letra in palabra:
    if letra in vocales:
        vocales[letra] += 1

# Mostrar la cantidad de cada vocal
print("\nCantidad de cada vocal en la palabra:")
for vocal, cantidad in vocales.items():
    print(f"{vocal}: {cantidad}")