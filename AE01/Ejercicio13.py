# Escribe un programa que solicite al usuario la URL o IP de un servidor y haga ping a dicho servidor, mostrando por pantalla el resultado.
# Puedes ayudarte de la función subprocess.run()para ejecutar comandos de Linux en Python.
# Si buscas en Internet, cuidado, ya que aparecen otras formas obsoletas y/o no recomendadas de hacerlo.
# También aparecen otras formas recomendadas, pero quizá de mayor complejidad.

# Borramos la pantalla
import subprocess
from os import system
system("cls")

url = input("Introduce la URL o IP de un servidor: ")
ping = "ping "

system(ping + url)
