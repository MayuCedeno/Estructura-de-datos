# Clase Nodo
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

# Clase Cola basada en nodos
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamaño = 0

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, nombre):
        nuevo = Nodo(nombre)
        if self.esta_vacia():
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        self.tamaño += 1
        print(f"{nombre} ha sido agregado a la cola.")

    def desencolar(self):
        if self.esta_vacia():
            print("La cola está vacía. No hay nadie para asignar asiento.")
            return None
        persona = self.frente.nombre
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamaño -= 1
        print(f"{persona} ha sido asignado a un asiento.")
        return persona

    def mostrar_cola(self):
        actual = self.frente
        print("Personas en cola:")
        while actual:
            print(f"- {actual.nombre}")
            actual = actual.siguiente

    def longitud(self):
        return self.tamaño

# Función de simulación (fuera de la clase)
def simular_asignacion_asientos():
    cola_ingreso = Cola()
    asientos_disponibles = 30

    # Simulamos llegada de personas
    for i in range(1, 40):  # Llegan 39 personas
        nombre = f"Persona{i}"
        cola_ingreso.encolar(nombre)

    print("\n--- Inicia asignación de asientos ---\n")

    while asientos_disponibles > 0 and not cola_ingreso.esta_vacia():
        cola_ingreso.desencolar()
        asientos_disponibles -= 1

    print("\n--- Asignación finalizada ---\n")
    if not cola_ingreso.esta_vacia():
        print("Personas que no alcanzaron asiento:")
        cola_ingreso.mostrar_cola()
    else:
        print("Todos los asistentes recibieron asiento.")

# Ejecutar la función solo si el archivo se corre directamente
if __name__ == "__main__":
    simular_asignacion_asientos()