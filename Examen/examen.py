import sys
import random

# Borramos la pantalla
from os import system
system("cls")

print("Comenzamos por 0")

#empezamos e inicializamos dede 0
numeroInicial = 0
aciertos=0

#El bucle while se ejecutara hasta que no se rompa con un break
while True:
    #Generamos un numero aleatorio entre 1 y 100
    numeroAleatorio = random.randint(1, 100)
    
    #Generamos un numero 0 y 1, donde cero sera sumar y uno sera restar
    operacion = random.randint(0, 1) 
    
    if operacion == 0:
        # Suma
        resultadoOperacion = numeroInicial + numeroAleatorio
        print (numeroInicial, "+",numeroAleatorio, " :")
        #controlamos que no introduzcamos un valor que no sea un entero
        try:
            resultadoUsuario = int(input("resultado : "))
        except:
            print("No has intriducido los valores numericos")
            sys.exit()
        numeroInicial = numeroAleatorio

        if resultadoUsuario == resultadoOperacion:
            #Si el resultado es correcto sumamos los aciertos
            aciertos= aciertos + 1
        else:
            print("\nNo es correcto. Has tenido", aciertos , "aciertos seguidos")
            break
            
    else:
        # Resta
        resultadoOperacion = numeroInicial - numeroAleatorio
        print (numeroInicial, "-",numeroAleatorio, " :")
        #controlamos que no introduzcamos un valor que no sea un entero
        try:
            resultadoUsuario = int(input("resultado : "))
        except:
            print("No has intriducido los valores numericos")
            sys.exit()
        numeroInicial = numeroAleatorio

        if resultadoUsuario == resultadoOperacion:
            #print("Has acertado")
            #Si el resultado es correcto sumamos los aciertos
            aciertos= aciertos + 1
        else:
            print("\nNo es correcto. Has tenido", aciertos , "aciertos seguidos")
            break

#try:
#    resultadoUsuario = int(input("Introduce el resultado de la operacion: "))
#except:
#    print("No has intriducido los valores de forma correcta")
#    sys.exit()

