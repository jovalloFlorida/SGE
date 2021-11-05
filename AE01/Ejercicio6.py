# Reescribe el programa anterior, para adivinar un número aleatorio generado por el ordenador comprendido entre un mínimo y un máximo indicados por el usuario,
#  utilizando la función random.random().

import random

# Borramos la pantalla
from os import system
system("cls")

while True:
    primerNumero = float(input("Introduce el primer numero entre 0.0 y 1.0: "))
    if (primerNumero >= 0.0 and primerNumero <= 1.0):
        break

while True:
    segundoNumero = float(
        input("Introduce el segundo numero entre 0.0 y 1.0: "))
    if (segundoNumero > primerNumero and segundoNumero <= 1.0):
        break

# random.random()
# Retorna el siguiente número en coma flotante aleatorio dentro del rango [0.0, 1.0).
numAleatorio = round(float(random.random()), 2)
print(numAleatorio)

while True:
    numElegido = float(
        input("Introduce numero a adivinar entre 0.0 y 1.0: "))
    if (numAleatorio == numElegido):
        print("\¡¡¡Has acertado!!!")
        break
