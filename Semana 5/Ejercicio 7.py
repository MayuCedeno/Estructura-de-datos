import string

# Crear una lista con el abecedario
abecedario = list(string.ascii_lowercase)

# Eliminar letras en posiciones múltiplos de 3 (índices 2, 5, 8,...)
# Se recorre en orden inverso para evitar errores al eliminar
for i in range(len(abecedario) - 1, -1, -1):
    if (i + 1) % 3 == 0:  # i + 1 porque la posición empieza en 1
        del abecedario[i]

# Mostrar la lista resultante
print("Abecedario sin letras en posiciones múltiplos de 3:")
print(abecedario)