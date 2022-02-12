# Escribe un programa que almacene los módulos de 2º DAM (PSP, AAD, PMM, DIN, SGE, etc.) en una lista,
# pregunte al usuario la nota que ha sacado en cada módulo y elimine de la lista los módulos aprobados.
# Al final, el programa debe mostrar por pantalla los módulos que el usuario tiene que recuperar en junio

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

modulos = [['SGE,0'], ['PMM,0'], ['ADD,0'], [
    'DIN,0'], ['PSP,0'], ['EIE,0'], ['ING,0'], ]

for modulo in modulos:
    print("Dime la nota del modulo", modulo[0], ":")
    nota = input()
    try:
        nota = float(nota)
    except:
        print("La nota introducida no es correcta...")
        sys.exit()
    modulo[1] = nota

i = 0
while i < len(modulos):
    if modulos[i][1] >= 5:
        modulos.pop(i)
    else:
        i = i+1

print("Las recuperaciones son: ", modulos)
