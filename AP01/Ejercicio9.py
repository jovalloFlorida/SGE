# Escribe un programa que lea tres números por la entrada estándar (teclado) y escriba el máximo

# Borramos la pantalla
from os import system
system("cls")

primerNumero = int(input("Introduce el primer numero: "))
segundoNumero = int(input("Introduce el segundo numero: "))
tercerNumero = int(input("Introduce el tercer numero: "))

if (primerNumero > segundoNumero and (primerNumero > tercerNumero)):
    print("\nEl numero mayor es el primero: ", primerNumero)
elif (segundoNumero > primerNumero and (segundoNumero > tercerNumero)):
    print("\nEl numero mayor es el segundo: ", segundoNumero)
elif (tercerNumero > primerNumero and (tercerNumero > segundoNumero)):
    print("\nEl numero mayor es el tercero: ", tercerNumero)
else:
    print("\nHay 2 numeros mayores igual\n")
