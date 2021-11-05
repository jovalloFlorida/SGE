# Escribe una función que, dado un número n y un intervalo comprendido entre min y max, devuelva cuántos números entre min y max son múltiplos de n y la suma de todos ellos.
# Haz un programa que pruebe dicha función ante la entrada de n, min y max por parte del usuario.

# Borramos la pantalla
from os import system
system("cls")


def MultiplosIntervalo(n, min, max):
    while min <= max:
        min += 1
        if min % n == 0:
            print(min)


n = int(input("Introduce un numero: "))
min = int(input("Introduce en minimo del intervalo: "))
max = int(input("Introduce en minimo del intervalo: "))

MultiplosIntervalo(n, min, max)
