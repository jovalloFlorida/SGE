# Escribe un programa que indique cuántas palabras diferentes hay en El Quijote (archivo el_quijote.txt), mostrándolas antes en orden alfabético.

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

try:
    man = open("C:\2021-2DAM\SGE\U2_AP2_Listas\el_quijote.txt")
except:
    print("Error en la lectura del fichero")
    sys.exit()
lista_palabras = list()

for linea in man:
    lista_linea = linea.split()
    for palabra in lista_linea:
        palabra = palabra.lower()
        palabra = palabra.strip(".¿?,\"-¡!<<>>:;´¨()'[] ")
        if not palabra in lista_palabras:
            lista_palabras.append(palabra)

lista_palabras.sort()
print(lista_palabras)
print("Hay", len(lista_palabras), "palabras en El Quijote")
