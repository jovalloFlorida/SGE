# Escribe un programa que solicite al usuario su peso (en kilogramos) y su altura (en metros) y calcule su índice de masa corporal (IMC).
# El IMC se calcula con la fórmula IMC = peso / altura2. Los valores normales de IMC están entre 20 y 25, aunque dichos valores también se ven influidos por la edad,
# el sexo, constitución física, etc.

# Borramos la pantalla
from os import system
system("cls")

peso = float(input("Introduce tu peso en Kg: "))
altura = float(input("Introduce tu altura en metros: "))

imc = peso / altura**2

print("Su IMC es: ", imc)
