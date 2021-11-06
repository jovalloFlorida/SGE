# Escribe un programa que almacene en una lista todos los números introducidos por el usuario hasta que este escriba “fin”.
# El método append() puede serte de ayuda. Tras ello, el programa debe llamar a una función que calcule y devuelva el mínimo,
# el máximo y la media de la lista de números.

# Libreria statics para obtener el promedio de una lista
import statistics
import sys

# Borramos la pantalla
from os import system
system("cls")


def CalcularMaxMinMedia(lista):
    # Retornamos numero Maximo, Minimo y Promedio o media de una lista
    return (max(lista), min(lista), statistics.mean(lista))


listaNumeros = []
sumaTotal = 0
try:
    while True:
        numero = input("introduce un numero para exit escribe (fin): ")
        if numero == "fin":
            break
        else:
            listaNumeros.append(int(numero))
            sumaTotal += int(numero)

    print("Lista de numeros: ", listaNumeros)
    numeroMaximo, numeroMinimo, mediaNumeros = CalcularMaxMinMedia(
        listaNumeros)
    print("El numero maximo es: ", numeroMaximo)
    print("El numero minimo es: ", numeroMinimo)
    print("La media de la suma total de los numeros es: ", mediaNumeros)

except:
    print("No has intriducido los valores de forma correcta")
    sys.exit()
