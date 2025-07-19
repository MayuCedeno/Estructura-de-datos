# Clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Función que calcula la longitud de una lista enlazada
def longitud_lista(cabeza):
    contador = 0
    actual = cabeza
    while actual:
        contador += 1
        actual = actual.siguiente
    return contador

# Prueba
n1 = Nodo(5)
n2 = Nodo(8)
n3 = Nodo(12)
n1.siguiente = n2
n2.siguiente = n3

print("Número de elementos en la lista enlazada:", longitud_lista(n1))