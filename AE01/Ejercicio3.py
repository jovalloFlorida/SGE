# Escribe un programa que pida al usuario un número N e imprima un triángulo de ancho máximo N caracteres asterisco.
import sys


def cls():
    # Borramos la pantalla
    from os import system
    system("cls")


cls()
try:
    numero = int(input("Introduce un numero positivo: "))

    for i in range(1, numero + 1):
        for j in range(i):
            print("* ", end="")
        print()

    for i in range(1, numero):
        for j in range(numero - i):
            print("* ", end="")
        print()
except:
    print("No has intriducido los valores de forma correcta")
    sys.exit()
