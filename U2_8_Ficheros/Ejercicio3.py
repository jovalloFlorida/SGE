# 2. Dado el fichero “mbox.txt”, determinar qué día de la semana se han recibido más correos.

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
    man = open("mbox.txt")
except:
    print("Error")
    sys.exit()

contadorlunes = contadormartes = contadormiercoles = contadorjueves = contadorviernes = contadorsabado = contadordomingo = 0
dia = None

for linea in man:  # Recorremos el fichero linea a linea
    if linea.startswith("From"):  # Si la linea empieza por From
        posarroba = linea.find("@")  # Encontramos la posicion de la @
        # Encontramos la posicion del primer espacio a partir de la @
        posespacio = linea.find(" ", posarroba)

        # Y la del siguiente espacio a partir del primer espacio
        possiguienteespacio = linea.find(" ", posespacio+1)
        # Entre el primer espacio y el segundo tenemos el dia
        diadelasemana = linea[posespacio:possiguienteespacio]
        # Limpiamos caracteres invisibles y pasamos a minusculas
        diadelasemana = diadelasemana.strip().lower()

        if diadelasemana == "mon":
            contadorlunes += 1
        if diadelasemana == "tue":
            contadormartes += 1
        if diadelasemana == "wed":
            contadormiercoles += 1
        if diadelasemana == "thu":
            contadorjueves += 1
        if diadelasemana == "fri":
            contadorviernes += 1
        if diadelasemana == "sat":
            contadorsabado += 1
        if diadelasemana == "sun":
            contadordomingo += 1

mayor = max(contadorlunes, contadormartes, contadormiercoles,
            contadorjueves, contadorviernes, contadorsabado, contadordomingo)

if mayor == contadorlunes:
    dia = "Lunes"
elif mayor == contadormartes:
    dia = "Martes"
elif mayor == contadormiercoles:
    dia = "Miercoles"
elif mayor == contadorjueves:
    dia = "Jueves"
elif mayor == contadorviernes:
    dia = "Viernes"
elif mayor == contadorsabado:
    dia = "Sabado"
elif mayor == contadordomingo:
    dia = "Domingo"

print("Contador de lunes:", contadorlunes)
print("Contador de martes:", contadormartes)
print("Contador de miercoles:", contadormiercoles)
print("Contador de jueves:", contadorjueves)
print("Contador de viernes:", contadorviernes)
print("Contador de sabado:", contadorsabado)
print("Contador de domingo:", contadordomingo)

print("\nEl dia de la semana con mas correos es:", dia)
