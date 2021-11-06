# Escribe un programa de cambio verificado de contraseña que solicite al usuario una contraseña y vuelva a solicitársela hasta que coincida con la dada inicialmente.
# Cuando coincida se informará de que el cambio de contraseña se ha llevado a cabo con éxito. Mientras no coincida,
# se informará de que no coinciden y se le solicitará de nuevo. Hay un máximo de 5 intentos para verificar el cambio de contraseña
# y deberá informarse al usuario de los intentos que le quedan cada vez.

import sys

# Borramos la pantalla
from os import system
system("cls")
try:
    passwd = input("Introduce una contraseña: ")
    rePasswd = input("Vuelve a introducir la contraseña: ")

    intentos = 1
    while passwd != rePasswd:
        print("Llevas ", intentos, "intentos")
        rePasswd = input(
            "Las contraseñas no coinciden, Vuelve a introducir la contraseña: ")
        intentos += 1
        if intentos == 5:
            print("Has superado el maximo de intentos...")
            break
except:
    print("No has intriducido los valores de forma correcta")
    sys.exit()

if passwd == rePasswd:
    print("\nHas cambiado la contraseña correctamente...")
