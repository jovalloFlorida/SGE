# 1. Dado el fichero “mbox-short.txt”, mostrar por pantalla las líneas que comienzan por “X-…” en forma de etiqueta:valor,
# que tengan valores numéricos, aplicándoles las funciones desarrolladas anteriormente.


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


def eliminar_prefijo(cad):
    if cad.startswith("X-"):
        return cad[2:]
    return cad


def redondear_en_etiqueta_valor(cad):
    posdospuntos = cad.find(":")
    etiqueta = cad[:posdospuntos]
    valor = cad[posdospuntos + 1:]
    valor = valor.strip()

    try:
        valor = float(valor)
    except:
        print("Valor decimal incorrecto")
        sys.exit()

    return etiqueta + ": " + str(round(valor, 2))


nombre = "mbox-short.txt"

try:
    man = open(nombre, "r")
except:
    print("El fichero no se ha podido abrir")
    sys.exit()

for linea in man:
    if linea.startswith("X-"):
        posiciondospuntos = linea.find(":")
        try:
            valornumerico = float(valornumerico)
        except:
            continue
        print(eliminar_prefijo(redondear_en_etiqueta_valor(linea)))
