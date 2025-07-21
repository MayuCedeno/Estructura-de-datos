def verificar_balance_parentesis(expresion):
    pila = []  # lista que usaremos como pila
    # Diccionario para pares de paréntesis
    pares = {')': '(', '}': '{', ']': '['}

    # Recorrer cada carácter
    for char in expresion:
        if char in '({[':
            pila.append(char)  # Apilar símbolo de apertura
        elif char in ')}]':
            if len(pila) == 0:
                return False  # No hay apertura para este cierre
            ultimo = pila.pop()  # Sacar último de la pila
            if pares[char] != ultimo:
                return False  # No coincide el paréntesis
    # Al final, si pila vacía, está balanceado
    return len(pila) == 0


# Programa principal para probar
def main():
    expresion = "{7 + (8 * 5) - [(9 - 7) + (4 + 1)]}"
    if verificar_balance_parentesis(expresion):
        print("Fórmula balanceada.")
    else:
        print("Fórmula no balanceada.")


main()


def mover_disco(origen, destino, torres):
    disco = torres[origen].pop()  # Quitar disco de la pila origen
    torres[destino].append(disco)  # Poner disco en la pila destino
    print(f"Mover disco {disco} de {origen} a {destino}")

def hanoi(n, origen, destino, auxiliar, torres):
    if n == 1:
        mover_disco(origen, destino, torres)
    else:
        hanoi(n-1, origen, auxiliar, destino, torres)
        mover_disco(origen, destino, torres)
        hanoi(n-1, auxiliar, destino, origen, torres)

def main():
    n = 3  # Número de discos
    # Inicializar pilas
    torres = {
        'A': list(range(n, 0, -1)),  # Discos en orden descendente, más grande abajo
        'B': [],
        'C': []
    }
    print("Estado inicial:")
    print(torres)
    print("\nMovimientos:")
    hanoi(n, 'A', 'C', 'B', torres)
    print("\nEstado final:")
    print(torres)

main()