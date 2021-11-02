# Ejercicio2 Escribe  un programa que solicite al usuario dos números enteros y calcule su división, indicando si se trata de una división exacta o no.

# Borramos la pantalla
from os import system
system("cls")

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))
division = num1 / num2
resto = num1 % num2

print(f"La division entre los dos numeros es: {division}")

if resto == 0:
    print("La division es exacta")
else:
    print("La division no es exacta")
