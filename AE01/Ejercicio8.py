# Escribe un programa que juegue a “Piedra, papel o tijera” contigo. Quien gane 3 tandas (la máquina o tú) gana la partida. Puedes ayudarte de la función random.choice().

# Borramos la pantalla
import random
import sys

from os import system
system("cls")

mylist = [1, 2, 3]
aleatorio = int(random.choice(mylist))
banca = ""

try:
    eleccion = int(input("Elige Piedra/Papel/Tijera (1/2/3): "))

    if eleccion == 1:
        jugador = "piedra"
    elif eleccion == 2:
        jugador = "papel"
    elif eleccion == 3:
        jugador = "tijera"
    print("\nUsuario juega: ", jugador)

    if aleatorio == 1:
        banca = "piedra"
    elif aleatorio == 2:
        banca = "papel"
    elif aleatorio == 3:
        banca = "tijera"

    print("La banca juega: ", banca)

    if banca == "piedra" and jugador == "papel":
        print("\nGanaste, papel gana piedra")
    elif banca == "papel" and jugador == "tijera":
        print("\nGanaste, Tijera gana papel")
    elif banca == "tijera" and jugador == "piedra":
        print("\nGanaste, Piedra pisa tijera")
    if banca == "papel" and jugador == "piedra":
        print("\nPerdiste, papel gana piedra")
    elif banca == "tijera" and jugador == "papel":
        print("\nPerdiste, Tijera gana papel")
    elif banca == "piedra" and jugador == "tijera":
        print("\nPerdiste, Piedra gana tijera")
    elif banca == jugador:
        print("\nBanca y jugador empatan")
except:
    print("No has intriducido los valores de forma correcta")
    sys.exit()
