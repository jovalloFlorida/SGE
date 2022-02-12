# Escribe un programa que pida al usuario una frase y muestre por pantalla el número de veces que contiene cada vocal.

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

vocales = ["a", "e", "i", "o", "u"]
frase = input("Dime la frase: \n")

for vocal in vocales:
    print("la vocal", vocal, "aparece", frase.count(vocal), "veces...")
