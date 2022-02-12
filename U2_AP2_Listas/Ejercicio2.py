# Escribe un programa que vaya preguntando al usuario los números ganadores de la lotería de Navidad, los vaya almacenando en una lista y
# cuando introduzca un -1 para finalizar, los muestre por pantalla ordenados de menor a mayor.

import sys
import platform
import subprocess
# Borramos terminal dependiendo el Sistema Operativo
if platform.system() == "Windows":
    from os import system
    system("cls")
else:
    from os import system
    system("clear")

numeros_ganadores = []
print("Escribe -1 para finalizar.")

while True:
    numero = str(input("Introduce un numero ganador de la loteria: "))
    if numero == "-1":
        break

    numero = numero.strip()
    if numero.isdecimal() and len(numero) == 5:
        numeros_ganadores.append(numero)
    else:
        print("El numero intorducido no es correcto...")

numeros_ganadores.sort()
print("\nLista de numeros ganadores:", numeros_ganadores)
