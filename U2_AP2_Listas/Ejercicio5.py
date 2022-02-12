# Escribe un programa en el que el usuario introduzca un número entero y el programa genere una frase con las palabras correspondientes a cada cifra.
#  Por ejemplo, 547 devolvería "cinco cuatro siete". Las palabras desde el "cero" hasta el "nueve" están almacenadas en una lista.

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

palabras = ['cero', 'uno', 'dos', 'tres', 'cuatro',
            'cinco', 'seis', 'siete', 'ocho', 'nueve']
lista_numeros = []

numero = input("Dime un numero: ")
if numero.isdecimal():
    lista_numeros.extend(numero)
    for numero in lista_numeros:
        print(palabras[int(numero)], end=" ")
print()
