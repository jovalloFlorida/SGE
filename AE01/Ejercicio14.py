# Escriba un programa que solicite al usuario una frase y una vocal y devuelva la frase habiendo cambiado todas sus vocales por la vocal dada por el usuario.

# Borramos la pantalla
from os import system
system("cls")

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for i in vocales:
    frase = frase.replace(i, vocal)

print("\n", frase)
