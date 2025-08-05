import random

numero_secreto = random.randint(1, 10)
adivinanza = int(input("Adivina el número (entre 1 y 10): "))

while adivinanza != numero_secreto:
    adivinanza = int(input("Incorrecto. Intenta de nuevo: "))

print("¡Felicidades! Adivinaste el número.")
