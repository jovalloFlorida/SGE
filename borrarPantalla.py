import sys
import platform

# Borramos terminal dependiendo el Sistema Operativo
if platform.system() == "Windows":
    from os import system
    system("cls")
else:
    from os import system
    system("clear")

# Controlamos que la introduccion de datos sea la correcta
try:
    primerNumero = int(input("Introduce el primer numero: "))
except:
    print("No has intriducido los valores de forma correcta")
    sys.exit()
