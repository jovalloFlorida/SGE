# Escribe un programa que intercambie el valor de dos variables de tipo entero sin utilizar una variable auxiliar. Puedes investigar cómo hacerlo (hay varias formas posibles).

# Borramos la pantalla
from os import system
system("cls")

primerNumero = int(input("Introduce el primer numero entero: "))
segundoNumero = int(input("Introduce el segundo numero entero: "))

print("\nNumeros originales: ", primerNumero, segundoNumero)

# A la variable primerNumero le asigno el valor de primerNumero + segundoNumero
primerNumero = primerNumero + segundoNumero

# A segundoNumero le asigno el resultado de resta al valor calculado anteriormente de primerNumero con el valor inicial de segundoNumero
segundoNumero = primerNumero - segundoNumero

# Y una vez realizado el cálculo de segundoNumero le resto el valor a la variable de primerNumero el nuevo valor de segundoNumero
primerNumero = primerNumero - segundoNumero

print("\nIntercambio de valor a las variables: ", primerNumero, segundoNumero)
print("")
