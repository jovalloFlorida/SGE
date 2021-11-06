# Escribe un programa que solicite al usuario la URL o IP de un servidor y haga ping a dicho servidor, mostrando por pantalla el resultado.
# Puedes ayudarte de la función subprocess.run()para ejecutar comandos de Linux en Python.
# Si buscas en Internet, cuidado, ya que aparecen otras formas obsoletas y/o no recomendadas de hacerlo.
# También aparecen otras formas recomendadas, pero quizá de mayor complejidad.

import sys
# Borramos la pantalla
from os import system
system("cls")

try:
    url = input("Introduce la URL o IP de un servidor: ")
    ping = "ping "
except:
    print("No has intriducido los valores de forma correcta")
    sys.exit()

system(ping + url)
