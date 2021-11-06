# Escribe un programa que pida al usuario dos números enteros mínimo y máximo y genere un número aleatorio, entre el mínimo y el máximo,
# que el usuario tendrá que adivinar. Mientras no se adivine, el programa irá indicando si el número introducido por el
# usuario es menor o mayor que el número aleatorio generado. Utiliza la función random.randint().

import random
import sys

# Borramos la pantalla
from os import system
system("cls")

try:
    primerNumero = int(input("Introduce el primer numero: "))
    while True:
        segundoNumero = int(input("Introduce el segundo numero: "))
        if (segundoNumero > primerNumero):
            break

    numAleatorio = random.randint(primerNumero, segundoNumero)
    print(numAleatorio)

    while True:
        numElegido = int(input("\nIntroduce numero a adivinar: "))
        if (numAleatorio == numElegido):
            print("Has acertado")
            break
except:
    print("No has intriducido los valores de forma correcta")
    sys.exit()
