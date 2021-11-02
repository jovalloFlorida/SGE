# Escribe un programa que calcule el equivalente humano de la edad de un gato, introducida por el usuario. En este sentido, el primer año de vida del gato
# equivale a 15 años de edad en humanos, mientras que el segundo año solo equivale a 10 años humanos. Cuando el gato es completamente adulto, sin embargo,
# cada año gatuno equivale a 4 años humanos.

# Borramos la pantalla
from os import system
system("cls")

edadGato = int(input("Introduce la edad del gato: "))

primerAnyo = 15
segundoAnyo = 10
resto = 4

edadHumana = 15 + 10 + ((edadGato - 2) * 4)

print("\nLa edad Humana equivalente al gato es: ", edadHumana, "\n")
