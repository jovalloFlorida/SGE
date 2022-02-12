# Escribe un programa que vaya pidiendo palabras al usuario hasta que este introduzca "FIN" y, tras ello, muestre las palabras en orden alfabético inverso.

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

palabras = []
print("Escribe FIN para finalizar.")

while True:
    palabra = str(input('Dime palabra: '))
    if palabra == 'FIN':
        break
    palabras.append(palabra)

palabras.sort()
print("Lista de palabras Ordenadas:", palabras)

palabras.reverse()
print("Lista de palabras Ordenadas al orden inverso:", palabras)
