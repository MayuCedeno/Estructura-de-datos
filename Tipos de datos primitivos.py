import math

# Clase Circulo que encapsula el radio como dato primitivo
class Circulo:
    # Constructor que recibe el radio como argumento y lo encapsula
    def __init__(self, radio):
        self.__radio = radio  # variable privada

    # Método para calcular el área del círculo
    def calcular_area(self):
        # Área = π * r^2
        return math.pi * self.__radio ** 2

    # Método para calcular el perímetro del círculo
    def calcular_perimetro(self):
        # Perímetro (circunferencia) = 2 * π * r
        return 2 * math.pi * self.__radio

    # Método para obtener el radio actual
    def obtener_radio(self):
        return self.__radio

    # Método para establecer un nuevo radio
    def establecer_radio(self, nuevo_radio):
        self.__radio = nuevo_radio


# Clase Rectangulo que encapsula la base y altura como datos primitivos
class Rectangulo:
    # Constructor que inicializa base y altura
    def __init__(self, base, altura):
        self.__base = base    # atributo privado
        self.__altura = altura

    # Método para calcular el área del rectángulo
    def calcular_area(self):
        # Área = base * altura
        return self.__base * self.__altura

    # Método para calcular el perímetro del rectángulo
    def calcular_perimetro(self):
        # Perímetro = 2 * (base + altura)
        return 2 * (self.__base + self.__altura)

    # Getters y setters (accesores y modificadores)
    def obtener_base(self):
        return self.__base

    def obtener_altura(self):
        return self.__altura

    def establecer_base(self, nueva_base):
        self.__base = nueva_base

    def establecer_altura(self, nueva_altura):
        self.__altura = nueva_altura


# Bloque de prueba para demostrar el uso de las clases
if __name__ == "__main__":
    # Crear un objeto Círculo con radio 5
    circulo = Circulo(5)
    print("CÍRCULO")
    print("Radio:", circulo.obtener_radio())
    print("Área:", round(circulo.calcular_area(), 2))
    print("Perímetro:", round(circulo.calcular_perimetro(), 2))

    print("\nRECTÁNGULO")
    # Crear un objeto Rectángulo con base 10 y altura 4
    rectangulo = Rectangulo(10, 4)
    print("Base:", rectangulo.obtener_base())
    print("Altura:", rectangulo.obtener_altura())
    print("Área:", rectangulo.calcular_area())
    print("Perímetro:", rectangulo.calcular_perimetro())