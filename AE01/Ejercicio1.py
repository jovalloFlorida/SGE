# Escribe un programa que pida al usuario dos números enteros y muestre por pantalla los números pares que hay entre ellos (incluidos ellos mismos).

# Borramos la pantalla
from os import system
system("cls")

primerNumero = int(input("Introduce el primer numero: "))
while True:
    segundoNumero = int(input("Introduce el segundo numero: "))
    if (segundoNumero > primerNumero):
        break


while primerNumero <= segundoNumero:
    if primerNumero % 2 == 0:
        print(primerNumero)
    primerNumero += 1
