palabras = []
print("Escribe FIN para finalizar.")

while True:
    palabra = str(input('Dime palabra: '))
    if palabra == 'FIN':
        break
    palabras.append(palabra)

palabras.sort()
print("Lista de palabras Ordenadas:", palabras)

palabras.reverse()
print("Lista de palabras Ordenadas al orden inverso:", palabras)
