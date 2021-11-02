# Escribe un programa que le pregunte al usuario si desea calcular el área de un triángulo o la de un círculo. Si se elige que se quiere calcular el área de un triángulo,
# el programa tiene que solicitar la base y la altura y mostrar el área como salida. Si se elige que se quiere calcular el área de un círculo, el programa solicitará
# entonces el radio y mostrará, igualmente, el área de este como salida. NOTA: El área de un triángulo es igual a la mitad de su base multiplicada por su altura.
# El área de un círculo se corresponde con Pi multiplicado por su radio al cuadrado. Nota: Utiliza como valor de Pi el valor 3.141592

# Borramos la pantalla
from os import system
system("cls")

calculo = input("Desea calcular el área de un triángulo o la de un círculo: ")
if calculo == "triangulo":
    base = float(input("Introduce la base del triangulo: "))
    altura = float(input("Introduce la altura del triangulo: "))
    print("\nEl area del triangulo es", (base*altura/2), "\n")
elif calculo == "circulo":
    import math
    radio = float(input("Introduce el radio del circulo: "))
    area = math.pi*radio*radio
    print("\nEl area del circulo es:% .2f" % area, "\n")
else:
    print("\nEsa opcion no existe\n")
