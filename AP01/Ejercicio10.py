# Hacer un programa que calcule las ayudas a la compra de la primera vivienda. Necesita saber el precio de la vivienda, la zonaVivienda a la que pertenece (A, B, C, D, E),
# y el sueldo anual y la edadComprador del comprador. El sueldo se corrige por un factor según la zonaVivienda (A: 0"85, B: 0"9, C: 0"92, D: 0"97, E: 1"00) y
# después se determina su valor proporcional al Salario Mínimo Interprofesional (SMI = 13.300 euros). Según esa proporción, la ayuda es un porcentaje
# del valor de la vivienda (<1"5: 15 %, <2"5: 10 %, <3"5: 8 %, <4"5: 5 %). Si el comprador es menor de 35 años, se le suman 3000 euros a la ayuda obtenida.

# Borramos la pantalla
from os import system
system("cls")

precioVivienda = float(input("Introduce el precio de la vivienda: "))
zonaVivienda = input("Introduce la zona de la vivienda (A/B/C/D): ")
sueldo = float(input("Introduce el sueldo anual: "))

smi = 13300

edadComprador = int(input("Edad tiene el comprador de la vivienda: "))

if zonaVivienda == "A":
    print("\nZona A: corrector sueldo 0.85")
    sueldo = 0.85 * sueldo
elif zonaVivienda == "B":
    print("\nZona B: corrector sueldo 0.9")
    sueldo = 0.9 * sueldo
elif zonaVivienda == "C":
    print("\nZona C: corrector sueldo 0.92")
    sueldo = 0.92 * sueldo
elif zonaVivienda == "D":
    print("\nZona D: Corrector sueldo 0.97")
    sueldo = 0.97 * sueldo
elif zonaVivienda == "E":
    print("\nZona E: Corrector sueldo 1")
    sueldo = 1 * sueldo
else:
    print("\n La zona de Vivienda es incorrecta")


proporcionSueldo = sueldo / smi

if proporcionSueldo < 1.5:
    ayuda = precioVivienda*0.15
elif proporcionSueldo < 2.5:
    ayuda = precioVivienda*0.1
elif proporcionSueldo < 3.5:
    ayuda = precioVivienda * 0.08
elif proporcionSueldo < 4.5:
    ayuda = precioVivienda * 0.05

if edadComprador < 35:
    ayuda += 3000

print("\nLa ayuda recibida para la compra de la vivienda es de: ", ayuda)
