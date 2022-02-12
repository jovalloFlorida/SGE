# Implementa una función que cuente las líneas de un fichero de forma “pythonica”

import sys
import platform
import subprocess

# Borramos terminal dependiendo el Sistema Operativo
if platform.system() == "Windows":
    from os import system
    system("cls")
else:
    from os import system
    system("clear")


def contar_lineas_sistema(nombreArchivo):
    try:
        resultadoComando = subprocess.run(["wc", "-l", nombreArchivo, capture_output=True, text=True])
        #resultadoComando = system("dir" + "-Recurse" + nombreArchivo)

    except:
        print("El archivo no existe...")
        sys.exit()

    posEspacio = resultadoComando.stdout.find("")

    return resultadoComando.stdout[:posEspacio]


def contar_lineas_python(nombreArchivo):
    try:
        manejador = open(nombreArchivo, 'r')
    except:
        print("El archivo no existe...")
        sys.exit()

    contador = 0

    for linea in manejador:
        contador += 1

    return contador


nombre = "mbox-short.txt"

print("En numero de lineas de la forma pythonica sobre",
      nombre, "es", contar_lineas_python(nombre))
print("En numero de lineas de la llamada al comando de shell",
      nombre, "es", contar_lineas_sistema(nombre))
