# Escribe un programa que calcule la nota media del curso teniendo en cuenta las notas (números decimales) de la primera,
# segunda y tercera evaluación y considerando que estas tienen un peso de un 30%, 40% y 30%, respectivamente.

# Borramos la pantalla
from os import system
system("cls")

print("Introduce las notas de 2º DAM de SGE")
sge1 = float(input("Introduce la nota de la primera evaluacion: "))
sge2 = float(input("Introduce la nota de la segunda evaluacion: "))
sge3 = float(input("Introduce la nota de la tercera evaluacion: "))

media = ((sge1 * (30 / 100)) + (sge2 * (40 / 100)) + (sge3 * (30 / 100)))

print("la media de la asignatura es:", media)
