# Ejercicio 4. Escriba un PROGRAMA que pida dos números enteros y que escriba si el mayor es múltiplo del menor
num1 = int(input("Escribe un numero entero: "))
num2 = int(input("Escriba un segundo numero: "))

if num1 > num2:
    multiplo = num1 % num2
    if multiplo == 0:
        print("El mayor es %s y es multiplo de %s" % (str(num1), str(num2)))
    else:
        print("El mayor es %s y no es multiplo de %s" % (str(num1), str(num2)))
elif num1 < num2:
    multiplo = num2 % num1
    if multiplo == 0:
        print("El mayor es %s y es multiplo de %s" % (str(num2), str(num1)))
    else:
        print("El mayor es %s y no es multiplo de %s" % (str(num2), str(num1)))
else:
    print("Los numeros son iguales")

