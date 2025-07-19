# Solicitar al usuario una muestra de números separados por comas
sample = input("Introduce una muestra de números separados por comas: ")

# Dividir el string por comas y convertir cada elemento a entero
sample = sample.split(',')
n = len(sample)

for i in range(n):
    sample[i] = int(sample[i])       # Convertir cada elemento a entero

# Convertir la lista en una tupla (opcional, para hacerla inmutable)
sample = tuple(sample)

# Inicializar sumas para calcular media y desviación típica
suma = 0
suma_cuadrados = 0

# Recorrer los valores de la muestra
for i in sample:
    suma += i
    suma_cuadrados += i**2

# Calcular la media
media = suma / n

# Calcular la desviación típica (fórmula de población)
desviacion = (suma_cuadrados/n - media**2)**0.5

# Mostrar resultados
print('La media es:', media)
print('La desviación típica es:', desviacion)