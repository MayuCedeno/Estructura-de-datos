# Clase que representa un contacto (registro)
class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def mostrar(self):
        print(f"Nombre    : {self.nombre}")
        print(f"Teléfono  : {self.telefono}")
        print(f"Correo    : {self.correo}")
        print(f"Dirección : {self.direccion}")
        print("-" * 40)

# Clase que representa la agenda (estructura con vector de contactos)
class AgendaTelefonica:
    def __init__(self):
        self.contactos = []  # Lista de objetos Contacto

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print("Contacto agregado exitosamente.\n")

    def mostrar_todos(self):
        if not self.contactos:
            print("No hay contactos registrados.")
        else:
            print("\n Lista de contactos:")
            for contacto in self.contactos:
                contacto.mostrar()

    def buscar_contacto(self, nombre):
        encontrados = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]
        if encontrados:
            print(f"\n Contacto encontrado:")
            for c in encontrados:
                c.mostrar()
        else:
            print("No se encontró el contacto.")

# Uso del sistema
def menu_agenda():
    agenda = AgendaTelefonica()

    while True:
        print("\n📱 Agenda Telefónica")
        print("1. Agregar contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar contacto por nombre")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo electrónico: ")
            direccion = input("Dirección: ")
            contacto = Contacto(nombre, telefono, correo, direccion)
            agenda.agregar_contacto(contacto)

        elif opcion == "2":
            agenda.mostrar_todos()

        elif opcion == "3":
            nombre = input("Ingrese el nombre a buscar: ")
            agenda.buscar_contacto(nombre)

        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu_agenda()