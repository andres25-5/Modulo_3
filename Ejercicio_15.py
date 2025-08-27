""" 
Ejercicio 15: Proyecto Final - Batalla Naval Simplificada
Crea una versión del juego "Batalla Naval" en una cuadrícula de 5x5:
•	El programa debe "esconder" un barco de 3 casillas en una fila o columna aleatoria.
•	El jugador tiene 10 turnos para adivinar las coordenadas (ej. "A3") y hundir el barco.
•	El programa debe gestionar el tablero (una lista de listas), validar la entrada del usuario, indicar si un disparo fue "Agua" o "Tocado", y llevar la cuenta de los turnos.

•	Al final, debe declarar si el jugador ganó o perdió.
Conceptos integrados: Lógica de juegos, listas anidadas, funciones, bucles while y for, condicionales, random, manipulación de strings.
"""

import random

# Tamaño del tablero
N = 5

def crear_tablero():
    """Crea un tablero vacío de 5x5"""
    return [["~" for _ in range(N)] for _ in range(N)]

def colocar_barco():
    """Coloca un barco de 3 casillas horizontal o vertical"""
    orientacion = random.choice(["H", "V"])
    if orientacion == "H":  # Horizontal
        fila = random.randint(0, N - 1)
        col = random.randint(0, N - 3)
        return [(fila, col + i) for i in range(3)]
    else:  # Vertical
        fila = random.randint(0, N - 3)
        col = random.randint(0, N - 1)
        return [(fila + i, col) for i in range(3)]

def imprimir_tablero(tablero):
    """Muestra el tablero con coordenadas"""
    print("   " + " ".join(str(i+1) for i in range(N)))
    for i, fila in enumerate(tablero):
        print(chr(65+i) + "  " + " ".join(fila))

def convertir_coordenada(coordenada):
    """Convierte entrada tipo 'A3' en índices (fila, columna)"""
    try:
        fila = ord(coordenada[0].upper()) - 65
        col = int(coordenada[1]) - 1
        if 0 <= fila < N and 0 <= col < N:
            return fila, col
    except:
        return None
    return None

def jugar():
    tablero = crear_tablero()
    barco = colocar_barco()
    intentos = 10
    aciertos = 0

    print(" Bienvenido a Batalla Naval (5x5)")
    print("Tienes 10 turnos para hundir un barco de 3 casillas.")
    imprimir_tablero(tablero)

    while intentos > 0 and aciertos < 3:
        disparo = input("\nIngresa coordenada (ej: A3): ").strip().upper()
        pos = convertir_coordenada(disparo)

        if not pos:
            print(" Entrada inválida. Usa formato LetraNúmero (ej: B2).")
            continue

        fila, col = pos
        if tablero[fila][col] != "~":
            print(" Ya disparaste aquí.")
            continue

        if pos in barco:
            tablero[fila][col] = "X"
            aciertos += 1
            print(" ¡Tocado!")
        else:
            tablero[fila][col] = "O"
            print(" Agua.")

        intentos -= 1
        print(f"Turnos restantes: {intentos}")
        imprimir_tablero(tablero)

    # Resultado final
    if aciertos == 3:
        print("\n ¡Felicidades! Hundiste el barco.")
    else:
        print("\n💀 Te quedaste sin turnos. El barco estaba en:")
        print([f"{chr(65+f)}{c+1}" for f, c in barco])

def main():
    jugar()

if __name__ == "__main__":
    main()
