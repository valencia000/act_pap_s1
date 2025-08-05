edad = int(input("Ingresa una edad (-1 para terminar): "))
mayor = -1

while edad != -1:
    if edad > mayor:
        mayor = edad
    edad = int(input("Ingresa otra edad (-1 para terminar): "))

print("La edad mayor ingresada fue:", mayor)
