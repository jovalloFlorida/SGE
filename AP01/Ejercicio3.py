# Ejericio 3. Escribe un programa que solicite al usuario el año actual y un año cualquiera y que escriba cuántos años
# han pasado desde ese año o cuántos años faltan para llegar a ese año.

# Borramos la pantalla
from os import system
system("cls")

anyoActual = int(input("Introduce el año actual: "))
otherYear = int(input("Introduce un año cualquiera: "))

if anyoActual <= otherYear:
    diferencia = otherYear - anyoActual
    print(f"Faltan {diferencia} años")
else:
    diferencia = anyoActual - otherYear
    print(f"Han pasado {diferencia} años")
