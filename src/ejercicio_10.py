contador = 0
palabra = input("Escribe una palabra (escribe 'fin' para terminar): ")

while palabra.lower() != "fin":
    contador += 1
    palabra = input("Escribe otra palabra (escribe 'fin' para terminar): ")

print("Total de palabras ingresadas:", contador)
