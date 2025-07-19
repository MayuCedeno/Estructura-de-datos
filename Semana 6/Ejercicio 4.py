import random


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def eliminar_fuera_rango(self, minimo, maximo):
        # Eliminar nodos al principio fuera del rango
        while self.cabeza and (self.cabeza.dato < minimo or self.cabeza.dato > maximo):
            self.cabeza = self.cabeza.siguiente

        actual = self.cabeza
        while actual and actual.siguiente:
            if actual.siguiente.dato < minimo or actual.siguiente.dato > maximo:
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente


# Generar lista enlazada con 50 números aleatorios entre 1 y 999
lista = ListaEnlazada()
for _ in range(50):
    num = random.randint(1, 999)
    lista.agregar_al_final(num)

print("Lista original:")
lista.mostrar()

# Leer rango desde teclado
minimo = int(input("Ingrese el valor mínimo del rango: "))
maximo = int(input("Ingrese el valor máximo del rango: "))

# Eliminar nodos fuera del rango
lista.eliminar_fuera_rango(minimo, maximo)

print("Lista después de eliminar valores fuera del rango:")
lista.mostrar()