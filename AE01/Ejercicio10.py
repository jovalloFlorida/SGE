# Escribe una función que calcule el factorial de un número de manera iterativa y otra función que lo calcule de manera recursiva,
# junto con un programa que pruebe ambas funciones ante la entrada del número por parte del usuario.
import sys

# Borramos la pantalla
from os import system
system("cls")


def FactorialRecursivo(n):  # función que lo calcule de manera recursiva
    if n > 1:
        return n * FactorialRecursivo(n - 1)
    else:
        return 1


def FactorialIterativo(n):  # función que lo calcule de manera iterativa
    resultado = 1
    i = 1
    while i <= n:
        resultado = resultado * i
        i = i + 1
    return resultado


try:
    numero = int(input("Introduce un numero entero y positivo: "))
    print("\nResultado del factorial de manera Recursiva: ",
          FactorialRecursivo(numero))
    print("Resultado del factorial de manera Iterativa: ",
          FactorialIterativo(numero))
    print("")
except:
    print("No has intriducido los valores de forma correcta")
    sys.exit()
